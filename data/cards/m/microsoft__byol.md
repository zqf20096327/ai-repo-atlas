# microsoft/byol

⭐ 14 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/microsoft/byol) · 组织维护

**微软工具包：把低资源语言适配进 LLM 的全流程框架**

BYOL 面向低资源与极低资源语言，提供从语言数字资源评估、双语训练数据准备（CPT/SFT）、基于 LlamaFactory 的持续预训练与指令微调、模型合并到 lm-evaluation-harness 多语评测的 13 步流水线，各步可独立运行或单命令全流程执行。附带 30+ 翻译模型的统一接口、已发布 Chichewa 与 Māori 的 1B/4B/12B 适配模型，以及人工翻译的 Global MMLU-Lite 评测集（Inuktitut/Chichewa/Māori）。安装详情在 SETUP.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 步流水线：语言资源评估→数据准备→训练→合并→多语评测，支持单命令全流程
- 统一接口调用 30+ 翻译模型（含 gpt-5-chat、nllb-200-3.3b）
- 已发布 Chichewa/Māori 的 1B/4B/12B 适配模型
- 人工翻译 Global MMLU-Lite 扩展 3 种低资源语言

## 适用场景

- 为我使用的低资源语言定制并评测 LLM
- 构建双语翻译训练语料并做持续预训练
- 扩展 lm-evaluation-harness 支持新语言的基准评测

## 场景标签

`模型训练` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: BYOL is a scalable framework for extending LLMs to low- and extreme-low-resource languages based on each language's
> L52: The BYOL pipeline takes any language from assessment to evaluation: classify the language's digital footprint, find

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/byol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `68d87831fb99` · [字段定义](../../DATASET.md)*
