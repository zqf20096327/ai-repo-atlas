# di37/finetuning-quantize-evaluate

⭐ 23 · Typst · MIT · 推送 2026-03-18 · [GitHub](https://github.com/di37/finetuning-quantize-evaluate) · [官网](https://di37.github.io/finetuning-quantize-evaluate/) · 个人维护

**微调/量化/评测的完整技术参考手册（PDF，6300+行）**

用 Typst 编写、编译为 PDF 的单册自包含技术参考，覆盖 LLM/VLM/嵌入模型五大主题：微调（SFT、LoRA/QLoRA、DPO/GRPO/RLHF）、量化（GPTQ/AWQ/QAT/GGUF）、评测（人工、BLEU/ROUGE、LLM-as-a-Judge、lm-evaluation-harness 基准）、嵌入基准管线与知识蒸馏。含 86 段可运行 Python 片段、23 张图、78 张表与 50+ arXiv 引文；范围限定单 GPU 训练，不含多 GPU 分布式。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 章、6300+ 行 Typst 源码、86 段可运行 Python 片段的单一参考文档
- 覆盖微调/量化/评测/嵌入基准/知识蒸馏五大主题
- 对 HuggingFace、LLaMA Factory、Unsloth、Axolotl、OpenAI API、Vertex AI 六种微调框架进行对比
- 附 23 张 PNG+SVG 图解与 45+ 术语表

## 适用场景

- 系统学习 LLM/VLM/嵌入模型的微调与量化方法
- 搭建私有嵌入模型评测与基准管线
- 选择合适的微调框架与量化方案

## 场景标签

`微调` `模型量化` `模型评测` `教程课程` · 领域:评测与运维

## 证据(README 行号)

> L9: A single, self-contained reference that covers five pillars of modern AI model development — from theory to practice
> L34: - **86 runnable code snippets** — not pseudocode. Every concept has working Python you can copy into a notebook.

## 星数曲线

```mermaid
xychart-beta
    title "di37/finetuning-quantize-evaluate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a674dc1dbe35` · [字段定义](../../DATASET.md)*
