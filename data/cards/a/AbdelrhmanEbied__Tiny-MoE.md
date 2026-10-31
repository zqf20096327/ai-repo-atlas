# AbdelrhmanEbied/Tiny-MoE

⭐ 21 · Python · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/AbdelrhmanEbied/Tiny-MoE) · 个人维护

**纯 PyTorch 从零实现的轻量 MoE 语言模型及训练管线**

从零用原生 PyTorch 实现的 Mixture-of-Experts decoder-only Transformer，总参数约 150M–200M、每 token 激活 70M–90M，含 MLA、RoPE、YaRN 长上下文扩展、Top-2 路由与权重吸收推理优化。在 Kaggle 免费 2×T4 GPU 上端到端预训练，数据管线基于 Hugging Face 流式数据集（FineWeb-Edu/Cosmopedia/Open-Web-Math），训练集成 DeepSpeed ZeRO-2 与 8-bit AdamW。定位为研究与学习项目，README 声明其对话能力有限，不以聊天性能为目标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MLA、RoPE、YaRN、MoE 路由全部从零实现，无模型框架依赖
- 流式数据管线 + 序列 packing + DeepSpeed ZeRO Stage 2 分布式训练
- 推理支持温度/Top-k/Top-p 采样、重复惩罚、n-gram 阻断与权重吸收
- 全部训练在 Kaggle 免费 2× NVIDIA T4 上完成

## 适用场景

- 学习现代 LLM 架构（MLA/MoE/YaRN）的底层实现
- 在免费 GPU 资源上复现小规模 MoE 预训练流程
- 作为 MoE 训练与路由优化的参考工程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: A lightweight Mixture-of-Experts language model implemented from scratch in native PyTorch.
> L24: The primary motivation behind Tiny-MoE is to demystify the internal mechanics of state-of-the-art MoE models and ta
> L399: > Tiny-MoE is primarily a research and learning project.

## 星数曲线

```mermaid
xychart-beta
    title "AbdelrhmanEbied/Tiny-MoE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7aaac719da3e` · [字段定义](../../DATASET.md)*
