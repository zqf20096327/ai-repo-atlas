# Masoudjafaripour/nanochat-VLM

⭐ 26 · Python · NOASSERTION · 推送 2026-09-21 · [GitHub](https://github.com/Masoudjafaripour/nanochat-VLM) · 个人维护

**面向学习研究的极简端到端 VLM 训练代码库（nanochat 风格）**

基于 Karpathy 的 nanochat 理念扩展的多模态项目：以脚本优先方式提供 BPE 分词器训练、GPT 风格 decoder-only 语言模型预训练（Muon+AdamW 优化、FineWeb-Edu 数据流），并通过 CLIP/ViT 视觉编码器与 projector 将图像 token 融入文本序列，目标是用单 GPU 或小服务器端到端训练一个小型 VLM。视觉部分目前在 notebooks/ 中原型验证，尚未并入 src/ 训练脚本；speedrun.sh 沿用上游旧模块结构。面向学习、研究与可改写实验，非规模化用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- tokenizer → LM → 多模态训练的脚本式端到端管线
- GPT 风格模型：RoPE、QK-norm、MQA、ReLU²、Muon+AdamW 混合优化
- 单 depth 参数控制模型规模，同一脚本可跑 CPU 小模型到多 GPU 模型
- 6 个 notebooks 逐步拆解 VLM 组件（视觉 token 化、projector、融合、生成）

## 适用场景

- 学习 VLM 从分词器到多模态训练的完整流程
- 在单 GPU 上复现并魔改一个小型视觉语言模型
- 在 notebook 中单独理解验证视觉-语言桥接组件

## 场景标签

`多模态` `模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: The **primary goal** of this repo is to **train a VLM end-to-end using nanochat-style scripts** (tokenizer → LM → mu
> L41:  * Fuse image tokens with text tokens.
> L46:  * Enable image + text chat.

## 星数曲线

```mermaid
xychart-beta
    title "Masoudjafaripour/nanochat-VLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f52d513f5f10` · [字段定义](../../DATASET.md)*
