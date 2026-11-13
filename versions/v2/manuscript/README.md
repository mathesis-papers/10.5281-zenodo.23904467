# Counterexamples to the Section 4.4 line-subgeometry conjecture

**Authors:** Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).

**License:** Creative Commons Attribution 4.0 International, `cc-by-4.0`.

The note concerns Saniga et al., *Hexagons govern three-qubit contextuality*,
Quantum 9 (2025), 1601, arXiv:2312.07738v3, Section 4.4, p. 20.

## Mathematical content

- Every full three-qubit perp line geometry has 31 points, 75 lines, and degree 12.
- Every three-regular isotropic line family on all 63 points meets that geometry
  in 15 lines. This includes every classically embedded split Cayley hexagon.
- For every nonzero pole in `n >= 2` qubits, the full contained-line perp geometry
  has degree four times that of the full `(n-1)`-qubit line geometry.
  Every four-qubit perp therefore has degree 252.
- This degree is pole-independent. The number of negative lines for canonical
  Pauli representatives is not: it is 12 at `IIZ` and 24 at `YYY`.
- A second configuration has 19 lines and degree 1, but intersects every such
  three-regular family in at least 3 lines.
- The two-qubit base case is established by the displayed 15-line sign table
  and ten parity grids. The geometric lifting, transport, intersection count,
  and characterization of optimal assignments have written proofs.

## Build the PDF

The bibliography is contained in `note.tex`; no external bibliography or figures
are needed. With Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, with a LaTeX installation containing the packages named in the
source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

## Reproduce the finite checks

The program uses only the Python 3.10-or-later standard library:

```sh
python3 verify.py > verification.json
```

Expected SHA256 of the resulting `verification.json`:

```text
f75151048afc7642ec9550fec765e002c1d0c48906ed33f98b194fd3cf6a1a29
```

The checks cover the 15 two-qubit lines, ten grids, all 32,768 two-qubit
assignments (640 attain degree 3), all 315 three-qubit isotropic line signs,
the 31-point/75-line coordinate perp, its 12 negative lines, all 16 linear
sections and their fourfold line multiplicities, and the 19-line example.
The canonical negative-line count is also calculated at all 63 three-qubit poles.
Line signs are calculated both from direct Pauli matrix products and from
binary phase exponents. A classical coordinate model from equations (13)-(14)
of the posing paper has 63 lines and meets every one of the 63 perp hyperplanes
in 15 lines. The all-parameter degree identity is proved by double counting;
it is not extrapolated from finite examples.

## Formal statement and exact source identity

Repository: `the-omega-institute/trureturing`.

Source revision:

```text
6715a5bea38a03c80f6c4da6de93fea88798f026
```

Source path:

```text
D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean
```

Qualified declarations:

```text
D5.S3.Quantum.Contextuality.PerpHyperplaneHexagonContextualityRefutation.claim
D5.S3.Quantum.Contextuality.PerpHyperplaneHexagonContextualityRefutation.result
```

The declaration `result : not claim` refutes the universal line-family equality
through the fixed `IIZ` perp, using positive degree at most 12 and hexagon
intersection at least 15. The note's exact degree, arbitrary-pole transport,
general lifting identity, equality characterization, 19-line example, and
three-regular intersection equality have the written proofs in the note.
`metadata.json` supplies the note metadata and immutable source URL.
`verification-scope.json` supplies the statement coverage, source identity,
qualified declarations, and verification-program version and digest.

Verification program version: 2. Its SHA256 is:

```text
a0b4d421ba979da64259b90e7fa7ef3f4152aecbb73ed0fdd2483ab168ea9681
```

The source archive contains `note.tex`, `metadata.json`,
`verification-scope.json`, `verify.py`, and this README. The generated
finite-check output is reproduced by the command above.
