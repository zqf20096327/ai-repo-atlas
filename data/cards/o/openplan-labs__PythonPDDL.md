# openplan-labs/PythonPDDL

⭐ 38 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/openplan-labs/PythonPDDL) · [官网](https://openplan-labs.github.io/PythonPDDL/) · 个人维护

**零依赖纯 Python 的 PDDL 自动规划框架：解析、接地、14 种规划器**

包名 jupyddl，提供手写 PDDL 解析器与接地器，覆盖 STRIPS、完整 ADL、数值流变量、持续动作等 20/21 个 requirement flag；内置 14 种规划器（BFS/A*/IDA*/beam search 等）与从经典到 LM-cut 的启发式。支持从已解规划轨迹学习启发式并按搜索展开节点数调优，含搜索预算、可复现实例生成器（7 个参数化域）、observer 观测钩子、CSV 导出的基准测试框架，以及 Pyodide 驱动的浏览器工作台。核心仅依赖标准库，Python ≥3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 种规划器与 8 类启发式（含 LM-cut）
- 从已解规划轨迹训练启发式并按搜索代价调优
- 7 个参数化可复现 PDDL 实例生成器
- 浏览器工作台（Pyodide 运行同一库）与零运行时依赖

## 适用场景

- 求解与验证 PDDL 规划实例并对比规划器性能
- 教学场景中演示搜索过程与可视化
- 生成可复现基准实例并做规划器基准测试
- 训练并调优自定义启发式

## 场景标签

 · 领域:自动规划/AI 经典搜索

## 证据(README 行号)

> L3: A dependency-free, pure-Python PDDL planning framework: parser, grounder,
> L34: - 🔎 **14 planners**: BFS, DFS, Iterative Deepening, Dijkstra, Greedy Best-First,

## 星数曲线

```mermaid
xychart-beta
    title "openplan-labs/PythonPDDL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-27 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e1425cad5bf` · [字段定义](../../DATASET.md)*
