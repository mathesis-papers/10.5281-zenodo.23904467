# Why twelve is not fifteen

Can a geometric pattern tell us exactly how many quantum measurement rules must fail? Haobo Ma and Wenlin Zhang give a concrete counterexample: a family of **75 rules needs at least 12 failures**, while every classical hexagon proposed as the geometric pattern selects **15 of its rules**. The intersection remains an upper bound, but it need not be the true minimum.

The “hexagon” here is a finite incidence structure on 63 points, rather than an ordinary six-sided polygon. The question comes from Section 4.4 of M. Saniga and colleagues' *Hexagons govern three-qubit contextuality* (arXiv version 3, p. 20). After establishing geometric descriptions in special configurations, they proposed a generalization to arbitrary subgeometries whose contexts are lines. This paper refutes that generalization. The established special cases remain intact.

This explanation follows version 2 of the paper, DOI [10.5281/zenodo.23904468](https://doi.org/10.5281/zenodo.23904468). Haobo Ma is affiliated with ChronoAI Pte Ltd, Singapore; Wenlin Zhang with the National University of Singapore and ChronoAI Pte Ltd, Singapore.

## Start with a sign-filling game

Imagine putting $+1$ or $-1$ at each point. Every “line” joins three points and requires their product to be either $+1$ or $-1$. A point must keep the same value wherever it occurs.

Suppose six lines form a grid in which every point occurs twice. Multiply all six rules together: the left side must be $+1$, because every assigned sign is squared. If an odd number of rules demand a negative product, the right side is $-1$. At least one rule must fail. This is an obstruction in the rules themselves, rather than a shortage of clever assignments.

Quantum measurements supply actual rules of this kind. $X,Y,Z$ are the single-qubit Pauli observables, with outcomes $\pm1$; $I$ denotes the identity operation. $XI$ means $X$ on the first qubit and $I$ on the second. We use triples whose observables commute pairwise, so their product specifies a consistent joint measurement constraint. For instance, $XX,ZZ,YY$ commute, yet

$$
(XX)(ZZ)(YY)=-I.
$$

Their predetermined outcomes must therefore multiply to $-1$. A line represents such a three-observable context. **Contextuality** means that no single assignment satisfies all lines. The **contextuality degree** $d(C)$ is the minimum number of failed lines in the family $C$, taken over every assignment. Counting the negative lines in one particular assignment is an upper bound on this minimum, not its definition.

## What the proposed intersection would mean

Three qubits have $4^3-1=63$ nonidentity Pauli labels. Certain triples form commuting lines. A classically embedded split Cayley hexagon uses all 63 points and selects three lines through each point, with additional geometric conditions.

The proposed generalization would imply that every line family $C$ with $d(C)>0$ admits such a hexagon $H$ with

$$
d(C)=|C\cap H|.
$$

The left side asks for an optimum over assignments; the right side counts shared lines. To disprove the equality, it suffices to find one $C$ for which every candidate intersection is larger than the optimum. We need not classify all optimal assignments.

Fix a nonidentity label $p$, called the pole. Take the 31 nonidentity labels commuting with it, and then **all lines entirely contained in those points**. Call this family $C_p$. It has 75 lines, including lines that do not pass through the pole. Keeping just the 15 lines through the pole gives a different configuration of degree zero; that is not the family used here.

The main conclusion is that every nonzero pole gives $d(C_p)=12$, whereas $|C_p\cap H|=15$ for every isotropic line family $H$ with three lines through each of the 63 points. The intersection statement needs even fewer assumptions than a hexagon. See [Precise results](statements.md) for the complete statements and proofs.

## Why the minimum is exactly twelve

Begin with two qubits. Their full geometry has 15 points and 15 lines and is often called the doily. Assigning $+1$ everywhere fails exactly three negative lines, so $d_2\le3$. Why can no assignment get away with two?

The authors list ten six-line grids, each with the parity contradiction above. Every grid requires a failed line, while each line belongs to exactly four grids. If there are $k$ failed lines, they can cover at most $4k$ grids. Hence

$$
4k\ge10,\qquad k\ge3.
$$

This supplies an explicit certificate for the known value $d_2=3$. The [appendix](appendix.md) lists all lines and all ten grids, so the incidence counts can be checked without searching through every assignment.

Now choose the pole $IIZ$. Each two-qubit point $u$ has two copies, $(u,0)$ and $(u,1)$, formed by appending $I$ or $Z$. Add the pole $(0,1)$. There are $2\cdot15+1=31$ points.

Each $u$ gives a positive pole line. Every base line $\{u,v,u+v\}$ has four other lifts:

$$
\{(u,a),(v,b),(u+v,a+b)\},
$$

where $a,b\in\{0,1\}$ and addition is modulo two. The lifted sign equals the base sign: the appended $Z$ factors multiply to $I$. We obtain 15 pole lines and $4\cdot15=60$ other lines, for a total of 75.

Copy an optimal two-qubit assignment to both copies of every point and put $+1$ at the pole. Each of the three base failures now occurs four times. This constructs an assignment with twelve failures. To prove optimality, we still need to exclude eleven or fewer.

Choose one copy of every base point using a rule $\lambda$ that preserves binary addition: select $(u,\lambda(u))$. Such a rule defines a **linear section**. There are 16 sections here, and each contains a whole two-qubit geometry, requiring at least three failures. Each non-pole line occurs in four sections; pole lines occur in none. If $N$ non-pole lines fail, then

$$
4N\ge16\cdot3,
$$

so $N\ge12$. The upper and lower bounds meet. The crucial feature of this count is that **every failed non-pole line is counted equally often**.

The same argument works for $n\ge2$ qubits: a full contained-line perp geometry has four times the degree of the full $(n-1)$-qubit geometry. Moving to a different pole uses a Clifford symmetry together with sign corrections, giving a bijection between assignments that preserves each failure. It does not assume that the number of negative lines stays fixed. Since the known full three-qubit degree is $d_3=63$, every four-qubit perp has degree 252. This does not give the degree of the full four-qubit space.

## Why every intersection has fifteen lines

This count requires no optimization. Every ambient line meets the 31-point set in either one point or three. Commuting with $p$ is one binary linear equation: on the two-dimensional vector space underlying a line, its kernel is either the whole space or a one-dimensional subspace.

Let $H$ have three lines through every ambient point. Counting incidences over all 63 points gives $63\cdot3$; each line has three points, so $H$ has 63 lines. Counting only incidences at our 31 points gives $31\cdot3=93$.

If $k$ lines of $H$ lie entirely inside, they contribute three incidences each. The other $63-k$ lines contribute one each. Thus

$$
93=3k+(63-k),
$$

which gives $k=15$. The same family has $d(C_p)=12$ and $|C_p\cap H|=15$ for every candidate $H$. This is exactly where the conjectured equality breaks.

The film follows this chain from the parity puzzle through the four lifts to the intersection count.

::: {.film src="001-twelve-fifteen"}
From a sign-filling puzzle to twelve versus fifteen, with English narration and aligned Chinese and English subtitles.
:::

## A smaller example, and what the result leaves open

A second construction combines all 15 lines through $XII$ with a six-line Mermin–Peres square. Two square lines already pass through the pole, so their union has $15+6-2=19$ lines. Square parity forces one failure, and assigning $+1$ everywhere achieves exactly one. Its degree is therefore one. Every $H$ still contains three lines through $XII$, all in this union, giving intersection at least three. The paper makes no claim that 19 is the minimum possible counterexample size.

Holweck and colleagues proved that the full complement of a classical hexagon has a satisfying assignment. Apply it to any family $C$: failures can occur only in $C\cap H$, so $d(C)\le|C\cap H|$ remains an upper bound. This example makes the inequality strict for every embedding at once.

The formal evidence has a precise scope. The [public Lean source](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.lean) proves that the universal equality is false, using positivity, an upper bound of twelve at $IIZ$, and an intersection lower bound of fifteen. The exact values, all-pole conclusions and general formula retain their written proofs and focused formalization contribution links in [Precise results](statements.md).

The argument does not settle neighboring questions about skew-hexagon complements or a global description of the full four-qubit space. The degree 315 and optimal-set classification for a four-qubit hyperbolic quadric were established subsequently by Z. Li, A. Gupta and V. Ganesh; that quadric is a different object from the degree-252 perp here. A natural next question is which additional hypotheses restore equality in the intersection bound.

The seminar presentation follows the same argument, with section counting and evidence scope in its appendix.

::: {.slides src="seminar"}
Aligned Chinese and English academic slides with speaker notes.
:::

[Continue to precise results and proofs](statements.md) · [Parity certificates and references](appendix.md)
