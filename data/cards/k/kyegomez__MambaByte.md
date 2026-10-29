# kyegomez/MambaByte

⭐ 129 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/MambaByte) · [官网](https://discord.gg/Czg5rpMZaC) · 个人维护

**MambaByte 论文的 PyTorch 实现：token-free 选择性状态空间模型**

对论文 MambaByte: Token-free Selective State Space Model 的实现，基于 PyTorch 与 Zeta 库，采用并行扫描方式实现，README 声明目标是更高性能的 Mamba 实现。模型在字节级（token-free）运作，无需分词器。以 pip 包形式提供，通过 MambaConfig 与 Mamba 类在 Python 中调用，MIT 许可。

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

- MambaByte 论文的 PyTorch/Zeta 实现
- 使用并行扫描的实现方式
- token-free，在字节级直接建模

## 适用场景

- 复现或实验 MambaByte 模型
- 研究 token-free 序列建模范式
- 作为选择性状态空间模型的代码基础进行改进

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: # MambaByte
> L4: Implementation of MambaByte in "MambaByte: Token-free Selective State Space Model" in Pytorch and Zeta. Note this wi

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/MambaByte 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 128 --> 130
    line [129, 129]
```

2026-10-18 129 → 2026-10-29 129（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a450c2391a83` · [字段定义](../../DATASET.md)*
