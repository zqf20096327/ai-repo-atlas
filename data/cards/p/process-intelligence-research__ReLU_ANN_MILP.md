# process-intelligence-research/ReLU_ANN_MILP

⭐ 67 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/process-intelligence-research/ReLU_ANN_MILP) · 组织维护

**将训练好的 ReLU 神经网络编码为混合整数线性规划模型**

读取用户预先训练的 TensorFlow 序列模型（ReLU 激活），采用渐进式界收紧过程生成 ReLU 网络的 MIP 编码，使非线性函数可嵌入混合整数规划问题；提供 Pyomo 与 Gurobi 两种建模接口。训练不属于本包功能，需用户自行完成。需要外部安装兼容求解器（Gurobi 需有效许可，或任一兼容 Pyomo 的 MIP 求解器）。附带两个 Jupyter 示例，演示用 MIP 公式寻找网络响应面的全局最小值。

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

- 渐进式界收紧生成 ReLU 网络的 MIP 编码
- 支持 Pyomo 与 Gurobi 两种建模接口
- 仅支持 TensorFlow 序列模型，训练需用户事先完成
- 提供 Jupyter 示例（求网络响应面全局最小值）

## 适用场景

- 把已训练的 ReLU 网络作为代理模型嵌入优化问题
- 用 MIP 求解器寻找神经网络响应面的全局最小值
- 在流程系统工程中做基于数据的非线性函数优化

## 场景标签

 · 领域:优化/化工过程系统工程

## 证据(README 行号)

> L5: With this package, you can generate mixed-integer linear programming (MIP) models of trained artificial neural netwo
> L7: ReLU ANNs can be used to approximate complex functions from data. In order to embed these functions into optimizatio

## 星数曲线

```mermaid
xychart-beta
    title "process-intelligence-research/ReLU_ANN_MILP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2bd8131fae70` · [字段定义](../../DATASET.md)*
