# Agnuxo1/openclaw-seed

⭐ 24 · Python · 推送 2026-10-27 · [GitHub](https://github.com/Agnuxo1/openclaw-seed) · [官网](https://github.com/Agnuxo1/OpenCLAW-P2P) · 个人维护

**自我进化的自主研究 agent：从论文数据持续 LoRA 训练自身**

P2PCLAW 生态中的自进化研究 agent 仓库：包含数据采集器（ArXiv/Semantic Scholar/GitHub，每 6h 收割，已积累 442 条训练数据）、LoRA 训练引擎、10 项基准评估器与模型自然选择机制，计划从 SmolLM2-135M 逐步进阶到 Qwen2.5-7B+。训练通过 Kaggle/Colab 免费 GPU 运行，配合 HuggingFace Space 上每小时运行的社交 agent 与 GitHub Actions 定时工作流。README 附有安全警告：部分密钥曾以明文共享需轮换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据采集器自动收割 ArXiv/Semantic Scholar/GitHub 论文与仓库
- LoRA 训练 + merge + push 流水线，支持 Kaggle T4 免费 GPU
- 评估器（10 项基准）与最佳模型自然选择机制
- HuggingFace Space 与 GitHub Actions 定时自动运行（1h/4h/6h）

## 适用场景

- 在免费 GPU（Kaggle/Colab）上运行自我训练的 agent 流水线
- 搭建持续从论文数据学习并自动发布模型的研究 agent
- 了解 P2PCLAW 生态各组件（BenchClaw/CAJAL 等）的分工

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: > **Part of the P2PCLAW ecosystem.** This repository contains the *self-evolving*
> L9: > Qwen2.5-7B+ via continuous LoRA training on harvested research data.
> L41: |Training Engine|✅ Configurado|SmolLM2-135M → LoRA → merge → push|

## 星数曲线

```mermaid
xychart-beta
    title "Agnuxo1/openclaw-seed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4cacff411329` · [字段定义](../../DATASET.md)*
