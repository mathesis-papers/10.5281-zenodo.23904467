# 书面陈述与公开 Lean 的比较

比较基于完整锁定提交 `8a24ea4e79de962725aab9d9b49cc605fcc211d8` 的实际源码、Blueprint 与冻结状态。原文保留的历史源码提交为 `6715a5bea38a03c80f6c4da6de93fea88798f026`。当前引用已通过安装的 pin --refresh 在同一完整提交解析；冻结论文与目录声明保持原样。

| Result | Verdict | Compared declaration | Commit | Scope |
|---|---|---|---|---|
| thm-perp | variant | D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文定理 1 对所有非零极点给出 31 点、75 线、精确度数 12，以及任意三正则各向同性线族的精确交集 15。公开声明是较弱的普遍否定，其证明使用固定 IIZ 的正度数、至多 12、较强候选条件下交集至少 15。私有关联计数可复用；请求 192 只补精确与全极点范围，不重复否定证明。 |
| prop-lift | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文命题 2 量化所有 n>=2 与非零极点，n=2 时 d_1=0。已检查的否定模块处理固定三比特见证；相关源码未陈述任意 n 的公式。请求 193 处理截面重数、最优值达到及有符号搬运，一般公式不依赖 d_2=3。 |
| lem-doily | variant | D5/S3/Quantum/Contextuality/LinearDoilyNegativeLineParity.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文引理 3 对全部赋值取最小值，给出 d_2=3。所比较声明给线性 doily 的规范负线数为奇数，不给这个最小值。邻近 SynchronousDoilyClassicalValue.result 给 p=1/10 的双人游戏值 22/25；其方阵方法可复用，但不能直接作为同一结论。请求 194 要求精确单赋值度数及规范符号对应。 |
| cor-optimal | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文推论 4 是每个 IIZ 赋值的充要条件：15 条极点线全满足，16 个截面各错三条。已检查源码未陈述这个充要条件。请求 193 复用母结果的截面构造；这个特化还用 d_2=3。 |
| cor-small | variant | D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文推论 5 构造 19 线并集，给出度数一和任意三正则各向同性 H 的交集至少三。公开否定使用另一 75 线见证；其私有方阵奇偶与符号引理可复用。请求 195 独立于一般搬运与 d_2=3，不含最小规模断言。 |
| thm-negation | same | D5/S3/Quantum/Contextuality/PerpHyperplaneHexagonContextualityRefutation.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 与公开声明对全部三比特线族及其赋值的普遍等式之否定完全对应。候选 H 为各向同性、每非零点三线、无普通三角形、局部平面。每个真正经典嵌入满足条件；未声称逆向刻画。此项是同一目录 s1 的较弱结论，与完整见证定理分开，故不重复登记请求。 |

检索范围：该提交的极超平面模块及 Blueprint、LinearDoilyNegativeLineParity、SynchronousDoilyClassicalValue，以及相关目录。比较只陈述已检查的数学差异；详细定义对应和索引检索记录保存在外部运行目录。

原稿五节点均已映射；s1 同时映射完整反例与其公开否定结论，各自含义不同。请求 192 处理精确与全极点性质；193 处理一般截面公式及其等号判据；194 处理两比特最小值；195 处理独立十九线构造。所有版本 DOI 均来自已核实的发现记录，登记使用公开原始源码。运行与构建证据保存在外部运行目录。
