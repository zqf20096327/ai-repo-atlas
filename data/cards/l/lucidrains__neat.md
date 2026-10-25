# lucidrains/neat

⭐ 42 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/lucidrains/neat) · 个人维护

**NEAT 神经进化算法及其衍生研究的实验代码库**

对 NEAT（增强拓扑神经进化）及相关衍生研究的探索实现，语言标签含 Nim。提供将进化得到的冠军 NEAT 网络蒸馏/行为克隆到 PyTorch MLP 的用法，附端到端示例：CartPole 与 LunarLander 的进化、行为克隆与验证流程。安装通过项目根目录的 install.sh 脚本，测试用 uv run 执行训练脚本。README 大量为论文引用（NEAT、协同进化、模块化等），标题标注 wip，属研究探索性质代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- NEAT 及衍生研究的探索实现
- 支持将进化冠军网络蒸馏/行为克隆为 PyTorch MLP
- 提供 CartPole/LunarLander 端到端训练与验证脚本

## 适用场景

- 研究神经进化算法及其衍生方向
- 将进化得到的网络蒸馏为可部署的 PyTorch 模型
- 在经典强化学习环境上运行进化与行为克隆流水线

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Explorations into NEAT and some of its derivative research
> L15: Distill / behavior-clone an evolved champion NEAT network into any barebones PyTorch MLP:

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/neat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `74f1ef53a927` · [字段定义](../../DATASET.md)*
