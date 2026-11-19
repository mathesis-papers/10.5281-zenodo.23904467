# Parity certificates and references

These are the complete finite certificates from manuscript Tables 1 and 2, supporting the [proof of the two-qubit degree](statements.md). Signs follow from $XY=iZ$, $YZ=iX$, $ZX=iY$, with the sign reversed on interchanging distinct nonidentity factors. The mathematical data are given here without requiring execution of the manuscript program.

<a id="lines"></a>

## Table 1: all two-qubit lines

| No. | Three observables | Sign |
|---|---|---|
| 1 | $XI, IX, XX$ | + |
| 2 | $XI, IZ, XZ$ | + |
| 3 | $XI, IY, XY$ | + |
| 4 | $ZI, IX, ZX$ | + |
| 5 | $ZI, IZ, ZZ$ | + |
| 6 | $ZI, IY, ZY$ | + |
| 7 | $YI, IX, YX$ | + |
| 8 | $YI, IZ, YZ$ | + |
| 9 | $YI, IY, YY$ | + |
| 10 | $XX, ZZ, YY$ | − |
| 11 | $XX, YZ, ZY$ | + |
| 12 | $ZX, XZ, YY$ | + |
| 13 | $ZX, YZ, XY$ | − |
| 14 | $YX, XZ, ZY$ | − |
| 15 | $YX, ZZ, XY$ | + |

<a id="grids"></a>

## Table 2: ten contradictory grids

Each row lists six line numbers. A grid means that these lines form three row contexts and three column contexts; the six numbers below are line labels, not points.

| Grid | Six lines |
|---|---|
| 1 | 1,2,4,5,10,12 |
| 2 | 1,2,7,8,11,14 |
| 3 | 1,3,4,6,11,13 |
| 4 | 1,3,7,9,10,15 |
| 5 | 2,3,5,6,14,15 |
| 6 | 2,3,8,9,12,13 |
| 7 | 4,5,7,8,13,15 |
| 8 | 4,6,7,9,12,14 |
| 9 | 5,6,8,9,10,11 |
| 10 | 10,11,12,13,14,15 |

Check each row: every occurring point appears twice and the number of negative lines is odd. Then check each line number: it occurs four times. The three negative lines make the zero assignment attain the lower bound. This certificate uses finite lists and parity. The arbitrary-$n$ conclusion instead depends on the linear-section and signed-transport arguments in the preceding chapter.

## References and source locations

Reference 2, Sections 2–3, defines the problem geometry and classical embeddings; its arXiv version 3, Section 4.4, p. 20, proposes the refuted generalization. The pole-line-only perpset in Reference 3, Section 2 and Proposition 2, differs from the full contained-line family here. Reference 4 establishes satisfiability of classical hexagon complements. Reference 5, Lemma 3, supplies signed Clifford transport; Lemma 8 and Proposition 10 use grid counting. Its Theorems 11 and 15 concern the four-qubit hyperbolic quadric and optimal-set classification; the latter uses a DRAT-certified finite enumeration.

1. Haobo Ma and Wenlin Zhang. *A degree-12 counterexample to Saniga et al.'s Section 4.4 line-subgeometry conjecture*, version 2 (2026). [DOI:10.5281/zenodo.23904468](https://doi.org/10.5281/zenodo.23904468). [PDF](https://zenodo.org/api/records/23904468/files/note-v2.pdf/content), [source](https://zenodo.org/api/records/23904468/files/source-v2.zip/content). CC BY 4.0.
2. M. Saniga, F. Holweck, C. Kelleher, A. Muller, A. Giorgetti and H. de Boutray. *Hexagons govern three-qubit contextuality*, Quantum **9** (2025), 1601. [DOI:10.22331/q-2025-01-20-1601](https://doi.org/10.22331/q-2025-01-20-1601); [arXiv:2312.07738v3](https://arxiv.org/abs/2312.07738v3).
3. A. Muller, M. Saniga, A. Giorgetti, H. de Boutray and F. Holweck. *New and improved bounds on the contextuality degree of multi-qubit configurations*, Mathematical Structures in Computer Science **34** (2024), 322–343. [DOI:10.1017/S0960129524000057](https://doi.org/10.1017/S0960129524000057); [arXiv:2305.10225](https://arxiv.org/abs/2305.10225).
4. F. Holweck, H. de Boutray and M. Saniga. *Three-qubit-embedded split Cayley hexagon is contextuality sensitive*, Scientific Reports **12** (2022), 8915. [DOI:10.1038/s41598-022-13079-3](https://doi.org/10.1038/s41598-022-13079-3).
5. Z. Li, A. Gupta and V. Ganesh. *The Four-Qubit Hyperbolic Quadric Has Contextuality Degree 315* (2026). [arXiv:2610.26465v1](https://arxiv.org/abs/2610.26465v1).

The exact-version DOI differs from the concept DOI. Cite the version DOI above for these proofs; the concept record is [10.5281/zenodo.23904467](https://doi.org/10.5281/zenodo.23904467).

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
