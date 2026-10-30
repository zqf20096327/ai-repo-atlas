# kyegomez/VortexFusion

⭐ 15 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/VortexFusion) · [官网](https://discord.com/servers/agora-999382051935506503) · 个人维护

**Transformer+Mamba+LSTM 串联架构的 PyTorch 模型实现**

提供将 Mamba、Transformer、LSTM 按 mamba→transformer→lstm 循环串联的联合架构实现，以 Python 包形式发布，可直接 pip 安装后用 torch 调用进行训练。README 声明模型尚未在大规模数据上训练，Todo 中列出计划在与 Llama 相同的数据集上训练并实验性能指标。采用 MIT 许可，作者邀请感兴趣者通过 Discord 参与模型训练与新架构研究。

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

- Mamba→Transformer→LSTM 循环串联的联合架构
- pip 安装即用，可直接开始训练
- 多模态能力（Multi-Modality）

## 适用场景

- 实验混合架构（SSM/Transformer/LSTM）的模型设计
- 作为新架构研究的起点自行训练
- 学习 Mamba 与传统模块的组合实现方式

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: This is the first ever implementation of a joint Transformer + Mamba + LSTM architecture. The flow is the following:
> L15: import torch

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/VortexFusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c3753504fc00` · [字段定义](../../DATASET.md)*
