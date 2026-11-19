# Precise results and complete proofs

This chapter makes the [story's two counts](README.md) precise. The manuscript uses a shared counter: Theorem 1, Proposition 2, Lemma 3, Corollary 4 and Corollary 5. A final, separate statement gives the negation in the public Lean declaration. That negation is a consequence of Theorem 1, distinct from the complete properties of its explicit witness.

## Objects, signs and the question

Let $\mathbb F_2=\{0,1\}$ with arithmetic modulo two, and put $V_n=(\mathbb F_2^2)^n$. Write a label as $v=((x_1,z_1),\ldots,(x_n,z_n))$, and define

$$
B(u,v)=\sum_{j=1}^n(x_jz'_j+z_jx'_j).
$$

The local labels $(0,0),(1,0),(0,1),(1,1)$ represent $I,X,Z,Y$, respectively. The canonical Pauli representative is

$$
P_v=\bigotimes_{j=1}^n i^{x_jz_j}X^{x_j}Z^{z_j}.
$$

Two observables commute exactly when $B(u,v)=0$. Points are the nonzero vectors of $V_n$. An isotropic line is $\{u,v,u+v\}$, where $u,v$ are nonzero, distinct and satisfy $B(u,v)=0$. Write $\mathcal L_n$ for all such lines. Define $s(\ell)\in\mathbb F_2$ by $\prod_{q\in\ell}P_q=(-1)^{s(\ell)}I$; commutation makes the order irrelevant.

An assignment $f(q)=0$ represents outcome $+1$, and $f(q)=1$ represents $-1$. A line fails when $\sum_{q\in\ell}f(q)\ne s(\ell)$. The degree $d(C)$ is the minimum number of failures in $C$. Every minimum is attained because the assignment set is finite. Put $d_m=d(\mathcal L_m)$.

For nonzero $p$, put $S_p=\{q\ne0:B(p,q)=0\}$, and let $C_p^{(n)}$ consist of all isotropic lines entirely contained in $S_p$. Abbreviate it to $C_p$ for three qubits.

## The five manuscript results

::: {.theorem #thm-perp title="The exact perp counterexample" mathesis="collected:hexagon-perp-line-counterexamples:2:s1" status="written-proof" proof="pf-thm-perp" doi="10.5281/zenodo.23904468" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/192"}
For every nonzero $p\in V_3$, $C_p$ has 31 points, 75 lines and $d(C_p)=12$. If $H\subseteq\mathcal L_3$ has exactly three lines through each of all 63 ambient points, then $|C_p\cap H|=15$. In particular, $d(C_p)=|C_p\cap H|$ fails for every classically embedded split Cayley hexagon.
:::

::: {.proof #pf-thm-perp}
The proposition below gives $d(C_p)=4d_2$ and the lemma gives $d_2=3$, so the degree is 12. At the coordinate pole $IIZ$, there are two copies of each of the 15 base points plus the pole, giving 31 points. There are 15 pole lines and four lifts of each of the 15 base lines, giving 75 lines. The signed Clifford correspondence in the proposition transports these counts to every pole.

Nondegeneracy of $B$ makes $B(p,-)$ a nonzero linear functional, with a 32-vector kernel. Removing zero gives $|S_p|=31$. Its restriction to the two-dimensional space underlying a line is either zero or has a one-dimensional kernel, so each line meets $S_p$ in three points or one. Three lines at each point and three points per line imply that $H$ has 63 lines. Set $k=|C_p\cap H|$. Counting incidences of $H$ with $S_p$ gives

$$
3\cdot31=3k+(63-k).
$$

Thus $k=15$. Classical embeddings meet these hypotheses (Saniga et al., Section 2, pp. 6–7), so $12<15$. The intersection proof needs neither the no-triangle condition nor local planarity.
:::

::: {.proposition #prop-lift title="The fourfold degree formula by linear sections" mathesis="collected:hexagon-perp-line-counterexamples:2:s2" status="written-proof" proof="pf-prop-lift" doi="10.5281/zenodo.23904468" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/193"}
For every integer $n\ge2$ and every nonzero $p\in V_n$, $d(C_p^{(n)})=4d_{n-1}$.
:::

::: {.proof #pf-prop-lift}
First choose $p=I^{\otimes(n-1)}Z$ and put $m=n-1$. Labels in its perp have the form $(u,t)$, representing $P_u\otimes Z^t$; the pole is $(0,1)$. There are two types of line:

$$
\{(0,1),(u,0),(u,1)\},\quad u\ne0,
$$

and the four lifts of each base line $\{u,v,u+v\}\in\mathcal L_m$:

$$
\{(u,a),(v,b),(u+v,a+b)\},\quad a,b\in\mathbb F_2.
$$

Pole lines are positive; lifted lines have their base sign since $Z^aZ^bZ^{a+b}=I$. This classification is exhaustive. A line whose projection is not injective contains the pole. Otherwise its projected labels are distinct, nonzero, sum to zero, and remain isotropic.

Every linear functional $\lambda:V_m\to\mathbb F_2$ defines a section $u\mapsto(u,\lambda(u))$ preserving every base line and sign. Any assignment fails on at least $d_m$ lines in each section. There are $2^{2m}$ sections. A fixed non-pole line specifies the values of $\lambda$ on two independent vectors, so belongs to $2^{2m-2}$ sections. Pole lines belong to none. If $N$ non-pole lines fail, then

$$
2^{2m-2}N\ge2^{2m}d_m,
$$

so $N\ge4d_m$, and the total number of failures is at least this large. For $m=1$ the base line set is empty and $d_1=0$; there is no fixed non-pole line to count, but the same double-counting inequality remains valid.

Conversely, choose a base assignment $g$ attaining $d_m$. Set $f(u,t)=g(u)$ for $u\ne0$ and $f(0,1)=0$. All pole lines are satisfied, and every failed base line has exactly four failed lifts. This attains $4d_m$, proving the reverse inequality.

For any nonzero pole, single-qubit Clifford gates turn each nonidentity factor into $Z$; controlled-NOT gates reduce the product of $Z$ factors to one, and swaps move it to the last qubit. A Clifford unitary $U$ thus induces a symplectic map $g$ taking $p$ to the coordinate pole. There is a sign function $\tau(v)\in\mathbb F_2$ with

$$
UP_vU^\dagger=(-1)^{\tau(v)}P_{gv}.
$$

Conjugating a line product gives

$$
s(g\ell)=s(\ell)+\sum_{v\in\ell}\tau(v).
$$

Consequently $f'(gv)=f(v)+\tau(v)$ preserves the failure status of each line and gives a bijection between assignments on the two perp geometries. Their degrees agree. This signed transport principle is attributed to Lemma 3 of Z. Li, A. Gupta and V. Ganesh; the assignment correction is explicit here.
:::

::: {.lemma #lem-doily title="The full two-qubit degree" mathesis="collected:hexagon-perp-line-counterexamples:2:s3" status="written-proof" proof="pf-lem-doily" doi="10.5281/zenodo.23904468" source="Lemma 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/194"}
The full two-qubit line geometry has contextuality degree $d_2=3$.
:::

::: {.proof #pf-lem-doily}
[Table 1 in the appendix](appendix.md#lines) lists all 15 lines; precisely lines 10, 13 and 14 are negative. [Table 2](appendix.md#grids) lists ten six-line grids. Each occurring point appears twice in each grid, and each grid has an odd number of negative lines. Satisfying all six equations would give $0=1$ on summing modulo two. Thus every grid needs a failed line. Each line occurs in four grids, so $k$ failed lines give $4k\ge10$. Integrality forces $k\ge3$. The zero assignment fails exactly the three negative lines and attains the bound. This known doily value appears in Saniga et al., Section 2, Figure 4; the ten-grid method also appears in Li, Gupta and Ganesh, Lemma 8 and Proposition 10.
:::

::: {.corollary #cor-optimal title="A section criterion for optimality" mathesis="collected:hexagon-perp-line-counterexamples:2:s4" status="written-proof" proof="pf-cor-optimal" doi="10.5281/zenodo.23904468" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/193"}
An assignment on $C_{IIZ}$ is optimal if and only if all 15 pole lines are satisfied and each of the 16 linear sections has exactly three failed lines.
:::

::: {.proof #pf-cor-optimal}
Every section has at least three failures. An optimal assignment has twelve failures in total. The number of section–failure incidences is at least $16\cdot3=48$ and at most $4\cdot12=48$. Equality forces exactly three in each section and forces all failed lines to avoid the pole. Conversely, satisfying all pole lines and having three failures in each section gives 48 incidences. Each non-pole line is counted four times, so there are $48/4=12$ failures in total, which is optimal.
:::

::: {.corollary #cor-small title="A nineteen-line degree-one counterexample" mathesis="collected:hexagon-perp-line-counterexamples:2:s5" status="written-proof" proof="pf-cor-small" doi="10.5281/zenodo.23904468" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/195"}
There exists a 19-line family $C$ with $d(C)=1$ and $|C\cap H|\ge3$ for every three-regular isotropic line family $H$ on all 63 ambient points.
:::

::: {.proof #pf-cor-small}
Take all 15 isotropic lines through $XII$ and add the three rows and three columns of

$$
\begin{array}{ccc}
XII&IXI&XXI\\
IZI&ZII&ZZI\\
XZI&ZXI&YYI
\end{array}
$$

Exactly two square lines pass through $XII$, so the union has $15+6-2=19$ lines. All lines through $XII$ are positive: their other two observables differ only by an $X$ factor on the first qubit and multiply to $XII$. The square has just one negative line, $\{XXI,ZZI,YYI\}$. Thus the zero assignment has one failure. Each square point occurs twice, so odd square parity forces at least one failure under every assignment. Hence $d(C)=1$. The three lines of $H$ through $XII$ all belong to $C$, giving the intersection bound. This argument is independent of the arbitrary-qubit degree identity and makes no minimum-size claim.
:::

## The separate public formal negation

For this statement, a candidate $H$ is an isotropic line family with three lines at every ambient point, no ordinary triangle joined by three distinct lines, and local planarity: any points on two lines through the same point are orthogonal. Every classical embedding satisfies these conditions. We do not need them to characterize all classical embeddings.

::: {.theorem #thm-negation title="The universal intersection equality is false" mathesis="collected:hexagon-perp-line-counterexamples:2:s1" lean="D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result"}
It is false that every $C\subseteq\mathcal L_3$ with $d(C)>0$ admits a candidate $H$ as above satisfying $d(C)=|C\cap H|$.
:::

::: proof
The public formal proof uses the full $IIZ$ perp line family. Square parity gives positive degree, the zero assignment gives an upper bound of twelve, and incidence counting gives an intersection lower bound of fifteen for every candidate. The universal equality would imply $15\le d(C)\le12$, a contradiction. This negation is a consequence of the precise theorem above.
:::

## Contributions and further scope

Each written result cites version 2 and its canonical formalization request. The fourfold formula and its equality criterion share the same section-construction request. Contributors can coordinate a focused scope in the relevant issue, reuse the existing sign and parity lemmas, and submit a contributor-fork PR to `dev` under the [upstream contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). Request registration does not change the evidence level of these statements.

The general formula and $d_3=63$ from Saniga et al., Section 4.1, give the four-qubit perp degree $4\cdot63=252$. This direct consequence makes no assertion about the full four-qubit space and leaves the earlier restricted hexagon results intact.

[Parity certificates and references](appendix.md) · [Return to the story](README.md)
