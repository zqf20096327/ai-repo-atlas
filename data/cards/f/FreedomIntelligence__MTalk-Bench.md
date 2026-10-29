# FreedomIntelligence/MTalk-Bench

⭐ 20 · JavaScript · Apache-2.0 · 推送 2025-11-19 · [GitHub](https://github.com/FreedomIntelligence/MTalk-Bench) · [官网](https://freedomintelligence.github.io/MTalk-Bench/) · 组织维护

**多轮对话场景下评测语音到语音 LLM 的基准**

面向语音到语音（S2S）大模型的多轮对话评测基准：数据集含音频、转写文本与测试提示，覆盖语义信息、副语言信息、环境声三类维度，提供 arena 式与 rubric 式两种评测协议及对应脚本。使用流程为克隆仓库、从 Hugging Face 下载数据集、由用户自行运行待测 S2S 模型生成音频回答并整理为 JSON，再调用评测脚本（judge 模型可选 gpt-4o-audio-preview 或 gemini-2.5-pro）。数据集以研究许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖语义/副语言/环境声三类评测维度
- arena 式与 rubric 式两种评测协议及脚本
- 数据集含音频、转写文本与测试提示，研究许可发布

## 适用场景

- 评测语音到语音模型在多轮对话中的表现
- 从理解记忆、推理执行、副语言生成等维度对比 S2S 模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: **MTalk-Bench** is a benchmark designed to evaluate **speech-to-speech (S2S) large language models (LLMs)** in **rea
> L57: You can choose between **arena-style** and **rubric-based** evaluations, and select the type of information to eval

## 星数曲线

```mermaid
xychart-beta
    title "FreedomIntelligence/MTalk-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `476a0a982bcb` · [字段定义](../../DATASET.md)*
