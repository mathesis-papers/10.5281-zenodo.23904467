# A degree-12 counterexample to Saniga et al.'s Section 4.4 line-subgeometry conjecture

**Authors:** Haobo Ma, Wenlin Zhang

We refute the line-subgeometry conjecture in Section 4.4, p. 20 of Saniga et al., Hexagons govern three-qubit contextuality, arXiv:2312.07738v3 (Quantum 9 (2025), 1601). The 75-line geometry contained in any three-qubit perp hyperplane has contextuality degree 12 but meets every classically embedded split Cayley hexagon in 15 lines. A 19-line configuration has degree 1 and intersection at least 3. Linear sections and signed Clifford transport prove that every perp in n >= 2 qubits has four times the degree of the full (n-1)-qubit line geometry; every four-qubit perp consequently has degree 252.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23904468](https://doi.org/10.5281/zenodo.23904468)
- Concept DOI: [https://doi.org/10.5281/zenodo.23904467](https://doi.org/10.5281/zenodo.23904467)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [hexagon-perp-line-counterexamples](https://mathesis-omega-research.apps.chrono-ai.fun/papers/hexagon-perp-line-counterexamples?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). A degree-12 counterexample to Saniga et al.'s Section 4.4 line-subgeometry conjecture. Mathesis, version 2. https://doi.org/10.5281/zenodo.23904468

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6715a5bea38a03c80f6c4da6de93fea88798f026/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) | No public receipt |
| Proposition (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6715a5bea38a03c80f6c4da6de93fea88798f026/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) | No public receipt |
| Lemma (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6715a5bea38a03c80f6c4da6de93fea88798f026/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6715a5bea38a03c80f6c4da6de93fea88798f026/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6715a5bea38a03c80f6c4da6de93fea88798f026/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23904467/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23904467/hexagon-perp-line-counterexamples/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23904467/hexagon-perp-line-counterexamples/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23904467/hexagon-perp-line-counterexamples/slides/) ([sources](books/hexagon-perp-line-counterexamples/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23904467/hexagon-perp-line-counterexamples/films/) ([sources](books/hexagon-perp-line-counterexamples/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23904467/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `thm-perp` | variant | `D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result` |
| `prop-lift` | none | — |
| `lem-doily` | variant | `D5/S3/Quantum/Contextuality/LinearDoilyNegativeLineParity.result` |
| `cor-optimal` | none | — |
| `cor-small` | variant | `D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result` |
| `thm-negation` | same | `D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/hexagon-perp-line-counterexamples/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
