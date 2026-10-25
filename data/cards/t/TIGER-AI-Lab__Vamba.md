# TIGER-AI-Lab/Vamba

⭐ 110 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/TIGER-AI-Lab/Vamba) · [官网](https://tiger-ai-lab.github.io/Vamba/) · 组织维护

**小时级长视频理解的混合 Mamba-Transformer 模型代码（ICCV 2025）**

ICCV 2025 论文 Vamba 的官方代码：提出混合 Mamba-Transformer 架构处理小时级长视频理解，将视频 token 的自注意力替换为以文本 token 为 query、视频 token 为 key/value 的交叉注意力层，并用 Mamba 块处理视频 token，以降低二次复杂度开销。提供基于 Qwen2-VL-7B 的模型推理、预训练与指令微调脚本（数据需自行准备 CC12M、PixelProse、LLaVA-OneVision-Data 等），以及 Video-MME 等评测脚本。通过 conda 环境 + flash-attn 安装，面向视频多模态研究场景。

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

- 文本自注意力 + 视频交叉注意力 + Mamba 块的混合架构
- 支持长视频（512 帧）推理与 Video-MME 评测脚本
- 提供预训练与指令微调训练脚本

## 适用场景

- 复现论文的长视频理解实验与评测
- 基于 Qwen2-VL 模型做视频理解微调研究
- 研究 Mamba-Transformer 混合架构的视频 token 处理方式

## 场景标签

`多模态` `微调` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repo contains code for our ICCV 2025 paper Vamba, a hybrid Mamba-Transformer model that leverages cross-attenti
> L43: The main computation overhead in the transformer-based LMMs comes from the quadratic complexity of the self-attenti

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/Vamba 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-25"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-19 110 → 2026-10-25 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `5e9731569b6a` · [字段定义](../../DATASET.md)*
