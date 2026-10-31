# Amin7410/Project-Andrzej

⭐ 14 · Rust · MIT · 推送 2026-07-02 · [GitHub](https://github.com/Amin7410/Project-Andrzej) · 个人维护

**Rust/Python 符号回归库：从数据中发现闭式数学公式**

eml_sr 是一个用 Rust 编写、经 PyO3 提供 Python 接口的符号回归库，从数值数据中搜索拟合的闭式数学公式。引擎为并行 Rayon 宽度优先/束搜索，结合 EML 算子（e^x − ln(y)）与常规算子（Exp/Log/Sqrt/三角函数/算术等），用 Levenberg–Marquardt 优化数值常数，输出精度-复杂度 Pareto 前沿，并在部分 Feynman 基准上找到精确匹配。README 明确声明：原论文的连续梯度优化方法未实现，实测发现的公式几乎不直接使用 EML 算子；项目处于暂停待评审状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 并行束搜索 + Levenberg–Marquardt 常数优化的符号回归引擎
- 以 EML 算子（e^x − ln(y)）作为算子集之一，支持纯 EML 编译时构建
- 输出精度-复杂度 Pareto 前沿，Python SmartSearcher 在变换目标上重试搜索
- 在部分 Feynman 符号回归基准上找到精确或近精确公式

## 适用场景

- 从实验数据中拟合可解释的闭式数学公式
- 在精度与公式复杂度之间做权衡选择
- 以 Rust 或 Python API 嵌入科学计算流程做公式发现

## 场景标签

`数据分析` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L16: **eml_sr** is a Rust library for symbolic regression — searching for a closed-form mathematical formula that fits a
> L31: - A parallel (Rayon) breadth-first / beam-search engine (`src/engine/bfs.rs`) that searches over increasingly compl

## 星数曲线

```mermaid
xychart-beta
    title "Amin7410/Project-Andrzej 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ad036e7acce9` · [字段定义](../../DATASET.md)*
