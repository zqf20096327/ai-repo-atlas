# kyegomez/MoE-Mamba

⭐ 131 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/MoE-Mamba) · [官网](https://discord.gg/GYbXvDGevY) · 个人维护

**MoE-Mamba 论文的 PyTorch/Zeta 模型实现库**

用 PyTorch 和 Zeta 实现论文《MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts》的模型代码，包含 SwitchMoE（源自 Switch Transformer）混合专家结构与 Mamba 选择性状态空间模型，提供 MoEMambaBlock 与 MoEMamba 两种用法示例。README 注明作者仍在开发中并寻求贡献者（通过 Agora Discord 的 MoE Mamba 频道）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch + Zeta 实现 MoE-Mamba 论文模型
- 提供 MoEMambaBlock 与 MoEMamba 两种模块用法
- SwitchMoE 结构来自 Switch Transformer 论文
- 附论文引用（bibtex）与代码质量工具链

## 适用场景

- 研究者复现或实验 MoE-Mamba 架构
- 在自有训练流程中组合状态空间模型与混合专家
- 基于该实现做 MoE/Mamba 结构变体实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: Implementation of MoE Mamba from the paper: "MoE-Mamba: Efficient Selective State Space Models with Mixture of Exper
> L19: from moe_mamba import MoEMambaBlock

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/MoE-Mamba 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 130 --> 133
    line [132, 131, 131]
```

2026-10-18 132 → 2026-10-31 131（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a3fea74d5108` · [字段定义](../../DATASET.md)*
