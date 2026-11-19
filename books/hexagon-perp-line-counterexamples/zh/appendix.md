# 奇偶证书与文献

本附录保留原文表 1、表 2 的完整有限证书，支撑[两比特度数的证明](statements.md)。符号可由 $XY=iZ$、$YZ=iX$、$ZX=iY$ 及反向交换时变号直接计算。这里给出数学数据，不把论文附带程序的运行视为证明前提。

<a id="lines"></a>

## 表 1：全部两比特线

| 编号 | 三个观测量 | 符号 |
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

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>

<a id="grids"></a>

## 表 2：十个矛盾方阵

每行列出六条线的编号；“方阵”指这些线可以排成三行三列的情境结构，不是把下面六个编号当作点。

| 方阵 | 六条线 |
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

逐行核对：每个点出现两次，每行只有奇数条负线；再逐编号核对：每条线出现四次。三条负线使全零赋值达到下界。这个证书只用有限列表和奇偶性。一般 $n$ 的结论则依赖正文中的线性截面与有符号搬运论证。

## 文献与定位

原问题与候选六边形定义见文献 2，第 2–3 节；被否定的推广见其 arXiv 第三版第 4.4 节第 20 页。文献 3 中只含经过极点的线的 perpset（第 2 节、命题 2），与这里的全部包含线不同。文献 4 给出经典六边形补集的可满足性。文献 5 的引理 3 支持有符号 Clifford 搬运，引理 8 与命题 10 使用方阵计数；其定理 11、15 处理四比特双曲二次曲面及最优集合分类，后者使用 DRAT 证书的有限枚举。

1. Haobo Ma and Wenlin Zhang. *A degree-12 counterexample to Saniga et al.'s Section 4.4 line-subgeometry conjecture*, version 2 (2026). [DOI:10.5281/zenodo.23904468](https://doi.org/10.5281/zenodo.23904468). [PDF](https://zenodo.org/api/records/23904468/files/note-v2.pdf/content), [source](https://zenodo.org/api/records/23904468/files/source-v2.zip/content). CC BY 4.0.
2. M. Saniga, F. Holweck, C. Kelleher, A. Muller, A. Giorgetti and H. de Boutray. *Hexagons govern three-qubit contextuality*, Quantum **9** (2025), 1601. [DOI:10.22331/q-2025-01-20-1601](https://doi.org/10.22331/q-2025-01-20-1601); [arXiv:2312.07738v3](https://arxiv.org/abs/2312.07738v3).
3. A. Muller, M. Saniga, A. Giorgetti, H. de Boutray and F. Holweck. *New and improved bounds on the contextuality degree of multi-qubit configurations*, Mathematical Structures in Computer Science **34** (2024), 322–343. [DOI:10.1017/S0960129524000057](https://doi.org/10.1017/S0960129524000057); [arXiv:2305.10225](https://arxiv.org/abs/2305.10225).
4. F. Holweck, H. de Boutray and M. Saniga. *Three-qubit-embedded split Cayley hexagon is contextuality sensitive*, Scientific Reports **12** (2022), 8915. [DOI:10.1038/s41598-022-13079-3](https://doi.org/10.1038/s41598-022-13079-3).
5. Z. Li, A. Gupta and V. Ganesh. *The Four-Qubit Hyperbolic Quadric Has Contextuality Degree 315* (2026). [arXiv:2610.26465v1](https://arxiv.org/abs/2610.26465v1).

本文版本 DOI 与概念 DOI 不同：引用本证明使用上述版本 DOI；概念记录为 [10.5281/zenodo.23904467](https://doi.org/10.5281/zenodo.23904467)。

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
