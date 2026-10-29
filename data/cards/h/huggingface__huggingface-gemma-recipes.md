# huggingface/huggingface-gemma-recipes

⭐ 304 · Jupyter Notebook · MIT · 推送 2026-08-25 · [GitHub](https://github.com/huggingface/huggingface-gemma-recipes) · 组织维护

**Gemma 系列模型的推理与微调示例笔记本集合**

Hugging Face 维护的 Gemma 模型食谱仓库：提供最小化上手示例，覆盖 Gemma 3/3n/4 的推理（pipeline 与 transformers 详细用法，文本/音频/图像/视频多模态）、函数调用、对话与多模态微调（含 Unsloth、TRL、GRPO、音频/GUI grounding 等 notebook 与脚本）以及 RAG 示例。多数笔记本可一键在 Colab 打开，部分微调示例标注可在免费 Colab T4 上运行。面向希望快速上手 Gemma 的开发者和学习者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Gemma 3/3n/4 的多模态推理示例（视觉/视频/音频/函数调用/物体检测）
- 对话与多模态微调 notebook 与脚本（Unsloth/TRL/GRPO）
- RAG 与函数调用示例 notebook
- 多数 notebook 支持一键在 Colab 打开，部分标注免费 T4 可跑

## 适用场景

- 我想快速跑通 Gemma 模型的文本或多模态推理
- 我想在 Colab 上微调 Gemma 3n 做对话或特定模态任务
- 我想参考现成代码为 Gemma 接入函数调用或 RAG

## 场景标签

`RAG` `多模态` `微调` `强化学习` · 领域:知识与检索

## 证据(README 行号)

> L5: 🤗💎 Welcome! This repository contains *minimal* recipes to get started quickly with the Gemma family of models.
> L93: We include a series of notebook+scripts for fine tuning the models.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/huggingface-gemma-recipes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 302 --> 305
    line [303, 304, 304]
```

2026-10-18 303 → 2026-10-29 304（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `d25565c57a31` · [字段定义](../../DATASET.md)*
