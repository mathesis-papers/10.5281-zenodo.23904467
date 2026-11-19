# 精确结果与完整证明

本章把[故事中的两次计数](README.md)写成精确陈述。结果按原文共用计数器的顺序排列：定理 1、命题 2、引理 3、推论 4、推论 5。最后单列公开 Lean 声明的否定命题；它是定理 1 的一个结论，不与显式反例的完整性质混作同一陈述。

## 对象、符号与问题

令 $\mathbb F_2=\{0,1\}$，加法与乘法按模二计算；$V_n=(\mathbb F_2^2)^n$。一个标签写成 $v=((x_1,z_1),\ldots,(x_n,z_n))$，并定义

$$
B(u,v)=\sum_{j=1}^n(x_jz'_j+z_jx'_j).
$$

每位的 $(0,0),(1,0),(0,1),(1,1)$ 分别代表 $I,X,Z,Y$，规范泡利代表为

$$
P_v=\bigotimes_{j=1}^n i^{x_jz_j}X^{x_j}Z^{z_j}.
$$

$B(u,v)=0$ 恰表示两个观测量交换。点是 $V_n$ 中的非零向量；各向同性线是 $\{u,v,u+v\}$，其中 $u,v$ 非零、相异且 $B(u,v)=0$。全部线组成 $\mathcal L_n$。线的符号 $s(\ell)\in\mathbb F_2$ 由 $\prod_{q\in\ell}P_q=(-1)^{s(\ell)}I$ 决定；交换性保证乘积顺序无关。

赋值 $f(q)=0$ 代表结果 $+1$，$f(q)=1$ 代表 $-1$。若 $\sum_{q\in\ell}f(q)\ne s(\ell)$，称线被违反。$d(C)$ 是线族 $C$ 的最少违反线数；赋值集合有限，所以最小值必定达到。记 $d_m=d(\mathcal L_m)$。

对非零 $p$，令 $S_p=\{q\ne0:B(p,q)=0\}$，并令 $C_p^{(n)}$ 为完全包含在 $S_p$ 中的全部各向同性线。三比特时简写 $C_p$。

## 原文五项结果

::: {.theorem #thm-perp title="极超平面的精确反例" mathesis="collected:hexagon-perp-line-counterexamples:2:s1" status="written-proof" proof="pf-thm-perp" doi="10.5281/zenodo.23904468" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/192"}
对每个非零 $p\in V_3$，$C_p$ 使用 31 个点、包含 75 条线，且 $d(C_p)=12$。若 $H\subseteq\mathcal L_3$ 在全部 63 个环境点上每点恰有三条线，则 $|C_p\cap H|=15$。因此对每个经典嵌入的分裂 Cayley 六边形，等式 $d(C_p)=|C_p\cap H|$ 都失败。
:::

::: {.proof #pf-thm-perp}
以下命题给出 $d(C_p)=4d_2$，引理给出 $d_2=3$，故度数为 12。在坐标极点 $IIZ$，点为极点加上 15 个底层点的两个副本，共 31 点；线为 15 条极点线加上 15 条底层线各自的四次提升，共 75 条。命题中的有符号 Clifford 对应把这些计数搬到每个极点。

非退化形式 $B$ 使非零线性函数 $B(p,-)$ 的核有 32 个向量，去掉零得 $|S_p|=31$。在一条线对应的二维空间上，该函数或恒为零，或有一维核，所以每条线与 $S_p$ 相交于三点或一点。由每点三线，每线三点，$H$ 有 63 条线。设 $k=|C_p\cap H|$，对 $H$ 与 $S_p$ 的关联作双重计数：

$$
3\cdot31=3k+(63-k).
$$

故 $k=15$。经典嵌入六边形满足这些假设（Saniga 等，第 2 节，第 6–7 页），因而有 $12<15$。这个交集论证并未使用无三角形或局部平面性条件。
:::

::: {.proposition #prop-lift title="线性截面的四倍公式" mathesis="collected:hexagon-perp-line-counterexamples:2:s2" status="written-proof" proof="pf-prop-lift" doi="10.5281/zenodo.23904468" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/193"}
对每个整数 $n\ge2$ 及每个非零 $p\in V_n$，$d(C_p^{(n)})=4d_{n-1}$。
:::

::: {.proof #pf-prop-lift}
先取 $p=I^{\otimes(n-1)}Z$，记 $m=n-1$。其正交空间中的标签写成 $(u,t)$，代表 $P_u\otimes Z^t$；极点为 $(0,1)$。线分成两类：

$$
\{(0,1),(u,0),(u,1)\},\quad u\ne0,
$$

以及每条底层线 $\{u,v,u+v\}\in\mathcal L_m$ 的四种提升

$$
\{(u,a),(v,b),(u+v,a+b)\},\quad a,b\in\mathbb F_2.
$$

第一类符号为正；第二类符号等于底层线，因为末尾的 $Z^aZ^bZ^{a+b}=I$。这份分类是穷尽的：若投影不单射，该线含极点；否则投影的三个非零相异标签相加为零，且仍各向同性。

每个线性函数 $\lambda:V_m\to\mathbb F_2$ 的截面 $u\mapsto(u,\lambda(u))$ 都保留全部底层线及其符号。对任意赋值，每个截面至少有 $d_m$ 条错线。共有 $2^{2m}$ 个截面；一条固定的非极点线给两个线性无关向量指定了 $\lambda$ 值，所以属于 $2^{2m-2}$ 个截面。极点线不属于截面。若 $N$ 是非极点错线数，则

$$
2^{2m-2}N\ge2^{2m}d_m,
$$

故 $N\ge4d_m$，总错线数更不少于此。$m=1$ 时底层没有线，$d_1=0$；虽然没有固定非极点线可数，同一个双重计数不等式仍成立。

反向地，取达到 $d_m$ 的赋值 $g$。令 $f(u,t)=g(u)$（$u\ne0$），$f(0,1)=0$。每条极点线满足，每条底层错线恰好产生四条提升错线，所以总数为 $4d_m$，得到相反不等式。

最后处理任意非零极点。单比特 Clifford 门把非恒等因子变为 $Z$；受控非门把多个 $Z$ 因子约去至一个；交换门把它移至最后一位。于是某个 Clifford 酉变换 $U$ 诱导辛变换 $g$，把 $p$ 送至坐标极点。存在 $\tau(v)\in\mathbb F_2$ 使

$$
UP_vU^\dagger=(-1)^{\tau(v)}P_{gv}.
$$

对线的乘积共轭可得

$$
s(g\ell)=s(\ell)+\sum_{v\in\ell}\tau(v).
$$

因此赋值对应 $f'(gv)=f(v)+\tau(v)$ 保持每条线是否被违反，并把两种极超平面线族双射对应。其度数相同。此有符号搬运原理归于 Z. Li、A. Gupta 与 V. Ganesh 的引理 3；这里显式写出了赋值修正。
:::

::: {.lemma #lem-doily title="完整两比特几何的度数" mathesis="collected:hexagon-perp-line-counterexamples:2:s3" status="written-proof" proof="pf-lem-doily" doi="10.5281/zenodo.23904468" source="Lemma 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/194"}
完整两比特线几何的情境性度数为 $d_2=3$。
:::

::: {.proof #pf-lem-doily}
[附录的表 1](appendix.md#lines)列出全部 15 条线，其中第 10、13、14 条为负。[表 2](appendix.md#grids)列出十个六线方阵：每个方阵的每个点出现两次、负线数为奇数。若方阵全部满足，把六条模二方程相加会得到 $0=1$，所以每个方阵至少有一条错线。每条线属于四个方阵，若错 $k$ 条，$4k\ge10$；$k$ 是整数，故 $k\ge3$。零赋值只违反那三条负线，达到下界。这个已知 doily 值见 Saniga 等第 2 节图 4；十方阵方法亦见 Li、Gupta 与 Ganesh 的引理 8、命题 10。
:::

::: {.corollary #cor-optimal title="最优赋值的截面判据" mathesis="collected:hexagon-perp-line-counterexamples:2:s4" status="written-proof" proof="pf-cor-optimal" doi="10.5281/zenodo.23904468" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/193"}
$C_{IIZ}$ 上的赋值最优，当且仅当全部 15 条极点线满足，而且 16 个线性截面中的每一个都恰有三条错线。
:::

::: {.proof #pf-cor-optimal}
每个截面至少错三条。最优赋值总共错 12 条，故截面错线关联数至少为 $16\cdot3=48$，又至多为 $4\cdot12=48$。等号迫使每个截面恰错三条，并且每条错线都不经过极点。反之，若全部极点线满足且每个截面恰错三条，就有 48 次关联。每条非极点线出现四次，因此总错线数为 $48/4=12$，赋值最优。
:::

::: {.corollary #cor-small title="十九线的度数一反例" mathesis="collected:hexagon-perp-line-counterexamples:2:s5" status="written-proof" proof="pf-cor-small" doi="10.5281/zenodo.23904468" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/195"}
存在一个 19 条线的线族 $C$，使 $d(C)=1$，且对每个在全部 63 点上每点三线的各向同性线族 $H$，都有 $|C\cap H|\ge3$。
:::

::: {.proof #pf-cor-small}
取经过 $XII$ 的全部 15 条各向同性线，再加入下面方阵的三行与三列：

$$
\begin{array}{ccc}
XII&IXI&XXI\\
IZI&ZII&ZZI\\
XZI&ZXI&YYI
\end{array}
$$

方阵恰有两条线经过 $XII$，故并集有 $15+6-2=19$ 条线。经过 $XII$ 的线全部为正：其余两观测量只在第一位相差一个 $X$ 因子，乘积为 $XII$。方阵只有 $\{XXI,ZZI,YYI\}$ 为负，故零赋值恰错一条。每个方阵点出现两次，奇数负号迫使任意赋值至少错一条。因此 $d(C)=1$。$H$ 有三条经过 $XII$ 的线，它们全部在 $C$ 中，给出交集下界。这里不需要先证明任意比特数的四倍公式，也不含最小反例断言。
:::

## 单列的公开形式否定

这里把候选 $H$ 定义为：各向同性线族、全部环境点每点三线、不含由三条不同线连接的普通三角形、且任意同过一点的两线上的各点互相正交。每个经典嵌入六边形满足这些条件；无需声称这些条件刻画了所有经典嵌入。

::: {.theorem #thm-negation title="普遍交集等式的否定" mathesis="collected:hexagon-perp-line-counterexamples:2:s1" lean="D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result"}
并非每个满足 $C\subseteq\mathcal L_3$ 且 $d(C)>0$ 的线族，都存在上述候选 $H$ 使 $d(C)=|C\cap H|$。
:::

::: proof
公开形式证明使用 $IIZ$ 的全部极超平面线族：方阵保证正度数，零赋值给出至多 12，关联计数给出每个候选交集至少 15。若普遍等式成立，将推出 $15\le d(C)\le12$，矛盾。这个否定是上面精确定理的推论。
:::

## 贡献与后续范围

上面书面证明的来源均为第二版 DOI；每个结果附有其规范形式化请求。四倍公式与其等号判据共享同一个截面构造请求。贡献者可在对应请求中协调范围，在自己的分支上复用现有符号与奇偶引理，并按[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)向 `dev` 提交有针对性的 PR。请求登记不改变这些结果的证据层级。

一般公式连同 Saniga 等第 4.1 节的 $d_3=63$，给出四比特极超平面度数 $4\cdot63=252$。这里没有把这个直接推论扩展为完整四比特空间的结论，也没有把此前的六边形特殊情形降为未解问题。

[奇偶证书与文献](appendix.md) · [回到故事](README.md)
