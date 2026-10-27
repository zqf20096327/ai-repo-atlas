# james-bowman/sparse

⭐ 170 · Go · MIT · 推送 2026-02-16 · [GitHub](https://github.com/james-bowman/sparse) · 个人维护

**Go 语言稀疏矩阵库：供科学与机器学习线性代数运算**

Go 语言稀疏矩阵格式实现库，提供 DOK、COO、CSR、CSC、DIA 格式及稀疏向量、位向量与位矩阵，仅存储非零值以降低内存与计算开销。实现 Sparse BLAS 标准例程，支持矩阵乘法、加减法与向量点积。兼容 Gonum 包的 Matrix 接口 API，可与 Gonum 稠密矩阵类型互操作。通过 go get 安装，面向科学与机器学习应用中的稀疏数据场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Sparse BLAS 标准例程
- 提供 DOK/COO/CSR/CSC/DIA 五种稀疏格式及稀疏向量、位向量
- 兼容 Gonum API 并与 Gonum 稠密矩阵互操作
- 支持矩阵乘法、加减法与向量点积

## 适用场景

- 文本挖掘等高稀疏度数据的矩阵运算
- Go 科学计算中替代稠密矩阵以节省内存
- 与 Gonum 生态配合做线性代数计算

## 场景标签

 · 领域:科学计算/数值库

## 证据(README 行号)

> L10: Implementations of selected sparse matrix formats for linear algebra supporting scientific and machine learning app
> L14: Machine learning applications typically model entities as vectors of numerical features so that they may be compare

## 星数曲线

```mermaid
xychart-beta
    title "james-bowman/sparse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 169 --> 171
    line [170, 170]
```

2026-10-18 170 → 2026-10-27 170（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5722cdfb49f5` · [字段定义](../../DATASET.md)*
