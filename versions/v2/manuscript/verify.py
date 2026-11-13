import itertools
import json
from collections import Counter


PAULI = 'IXZY'
MATRICES = (
    ((1, 0), (0, 1)),
    ((0, 1), (1, 0)),
    ((1, 0), (0, -1)),
    ((0, -1j), (1j, 0)),
)


def coordinates(point, qubits):
    return tuple((point >> (2 * position)) & 3 for position in range(qubits))


def label(point, qubits):
    return ''.join(PAULI[local] for local in coordinates(point, qubits))


def symplectic(first, second, qubits):
    return sum(((left & 1) * (right >> 1) + (left >> 1) * (right & 1))
               for left, right in zip(coordinates(first, qubits), coordinates(second, qubits))) % 2


def multiply(first, second):
    return tuple(tuple(sum(first[row][inner] * second[inner][column] for inner in range(2))
                       for column in range(2)) for row in range(2))


def matrix_sign(line, qubits):
    phase = 1
    for position in range(qubits):
        product = MATRICES[0]
        for point in line:
            product = multiply(product, MATRICES[(point >> (2 * position)) & 3])
        assert product[0][1] == product[1][0] == 0
        assert product[0][0] == product[1][1]
        phase *= product[0][0]
    assert phase in (1, -1)
    return int(phase == -1)


def exponent_sign(line, qubits):
    first, second, third = line
    assert first ^ second == third
    exponent = 0
    for left, right in zip(coordinates(first, qubits), coordinates(second, qubits)):
        left_x, left_z = left & 1, left >> 1
        right_x, right_z = right & 1, right >> 1
        exponent += left_x * left_z + right_x * right_z + 2 * left_z * right_x
        exponent -= (left_x ^ right_x) * (left_z ^ right_z)
    assert exponent % 2 == 0
    return (exponent % 4) // 2


def isotropic_lines(qubits):
    return sorted({tuple(sorted((first, second, first ^ second)))
                   for first in range(1, 4 ** qubits)
                   for second in range(first + 1, 4 ** qubits)
                   if symplectic(first, second, qubits) == 0})


def classical_hexagon(lines):
    def lifted(point):
        local = coordinates(point, 3)
        binary = tuple(value >> 1 for value in local) + tuple(value & 1 for value in local)
        return binary + (sum(binary[position] * binary[position + 3] for position in range(3)) % 2,)

    def accepted(line):
        first, second = map(lifted, line[:2])

        def plucker(row, column):
            return (first[row - 1] * second[column - 1] + first[column - 1] * second[row - 1]) % 2

        return (all(plucker(*left) == plucker(*right) for left, right in (
            ((6, 2), (1, 7)), ((1, 3), (7, 2)), ((2, 4), (3, 7)),
            ((3, 5), (7, 4)), ((4, 6), (5, 7)), ((5, 1), (7, 6))))
                and (plucker(1, 4) + plucker(2, 5) + plucker(3, 6)) % 2 == 0)

    return [line for line in lines if accepted(line)]


def main():
    doily = isotropic_lines(2)
    ambient = isotropic_lines(3)
    assert len(doily) == 15 and len(ambient) == 315
    for qubits, lines in ((2, doily), (3, ambient)):
        assert all(matrix_sign(line, qubits) == exponent_sign(line, qubits) for line in lines)
    signs = [matrix_sign(line, 2) for line in doily]
    grids = []
    for selected in itertools.combinations(range(15), 6):
        incidences = Counter(point for index in selected for point in doily[index])
        if len(incidences) == 9 and set(incidences.values()) == {2}:
            assert sum(signs[index] for index in selected) % 2 == 1
            grids.append(selected)
    assert len(grids) == 10
    assert set(Counter(index for grid in grids for index in grid).values()) == {4}
    negative_doily = [index for index, sign in enumerate(signs) if sign]
    assert len(negative_doily) == 3
    masks = [sum(1 << (point - 1) for point in line) for line in doily]
    histogram = Counter(sum(((assignment & mask).bit_count() % 2) != sign
                            for mask, sign in zip(masks, signs)) for assignment in range(1 << 15))
    assert min(histogram) == 3
    pole = 2 << 4
    perp_points = {point for point in range(1, 64) if symplectic(pole, point, 3) == 0}
    perp_lines = [line for line in ambient if set(line) <= perp_points]
    pole_lines = [line for line in perp_lines if pole in line]
    nonpole_lines = [line for line in perp_lines if pole not in line]
    assert (len(perp_points), len(perp_lines), len(pole_lines), len(nonpole_lines)) == (31, 75, 15, 60)
    assert all(matrix_sign(line, 3) == 0 for line in pole_lines)
    assert sum(matrix_sign(line, 3) for line in perp_lines) == 12
    cover = Counter()
    for functional in range(16):
        def section(point):
            return point | (((functional & point).bit_count() % 2) << 5)

        for line, sign in zip(doily, signs):
            lifted = tuple(sorted(section(point) for point in line))
            assert lifted in nonpole_lines and matrix_sign(lifted, 3) == sign
            cover[lifted] += 1
    assert set(cover) == set(nonpole_lines) and set(cover.values()) == {4}
    hexagon = classical_hexagon(ambient)
    assert len(hexagon) == 63
    incidence = Counter(point for line in hexagon for point in line)
    assert len(incidence) == 63 and set(incidence.values()) == {3}
    intersection_sizes = [sum(all(symplectic(other_pole, point, 3) == 0 for point in line)
                              for line in hexagon) for other_pole in range(1, 64)]
    assert set(intersection_sizes) == {15}
    lookup = {label(point, 3): point for point in range(1, 64)}
    ambient_signs = {line: exponent_sign(line, 3) for line in ambient}
    negative_counts = {}
    for other_pole in range(1, 64):
        contained = [line for line in ambient
                     if all(symplectic(other_pole, point, 3) == 0 for point in line)]
        assert len(contained) == 75
        negative_counts[label(other_pole, 3)] = sum(ambient_signs[line] for line in contained)
    assert negative_counts['IIZ'] == 12 and negative_counts['YYY'] == 24
    square_rows = (('XII', 'IXI', 'XXI'), ('IZI', 'ZII', 'ZZI'), ('XZI', 'ZXI', 'YYI'))
    square = {tuple(sorted(lookup[point] for point in row)) for row in square_rows}
    square.update(tuple(sorted(lookup[square_rows[row][column]] for row in range(3)))
                  for column in range(3))
    star = {line for line in ambient if lookup['XII'] in line}
    small_witness = star | square
    assert len(star) == 15 and len(square) == 6 and len(star & square) == 2
    assert len(small_witness) == 19 and small_witness <= set(ambient)
    assert sum(matrix_sign(line, 3) for line in small_witness) == 1
    assert all(count == 2 for count in Counter(point for line in square for point in line).values())
    assert sum(matrix_sign(line, 3) for line in square) == 1
    result = {
        'two_qubit_geometry': {
            'points': 15, 'lines': 15, 'degree': 3, 'assignments': 32768,
            'minimum_assignments': histogram[3],
            'line_table': [{'number': index + 1, 'points': [label(point, 2) for point in line],
                            'negative': bool(signs[index])} for index, line in enumerate(doily)],
            'grid_table': [[index + 1 for index in grid] for grid in grids],
            'grids_per_line': 4,
        },
        'coordinate_perp': {'pole': 'IIZ', 'points': 31, 'lines': 75, 'pole_lines': 15,
                            'nonpole_lines': 60, 'negative_lines': 12, 'degree': 12,
                            'linear_sections': 16, 'sections_per_nonpole_line': 4},
        'classical_hexagon_example': {'lines': 63, 'lines_per_point': 3,
                                      'perp_intersection_for_each_of_63_poles': 15},
        'canonical_perp_negative_lines': {
            'poles': 63, 'lines_per_perp': 75,
            'counts_by_pole': dict(sorted(negative_counts.items())),
        },
        'nineteen_line_witness': {'pole': 'XII', 'star_lines': 15, 'square_lines': 6,
                                  'shared_lines': 2, 'union_lines': 19,
                                  'negative_lines': 1, 'degree': 1,
                                  'three_regular_intersection_lower_bound': 3},
        'proof_scope': {'written': ['perp degree multiplication for every n >= 2 and every nonzero pole',
                                    'three-regular incidence intersection equals 15'],
                        'finite': ['two-qubit sign and grid tables', 'all two-qubit assignments',
                                   'three-qubit incidence, signs, and section multiplicities',
                                   'classical coordinate example',
                                   'canonical negative-line counts for all 63 three-qubit poles']},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
