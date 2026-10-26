# daekeun-ml/evaluate-llm-on-korean-dataset

⭐ 49 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/daekeun-ml/evaluate-llm-on-korean-dataset) · 个人维护

**韩语 LLM/SLM 基准评测套件：9 个韩文数据集多供应商批量跑分**

在韩语能力、推理与专业知识上评测 LLM/SLM 的基准套件，覆盖 CLIcK、KMMLU 系列、KoBALT-700、KorMedMCQA 等 9 个数据集。支持多供应商接入（Azure OpenAI、Amazon Bedrock、OpenAI 兼容/自托管、Azure ML、Hugging Face），并行批量评估并生成排行榜表格。通过 uv sync 与 run.sh 快速启动，也可用 GitHub Codespaces。作者声明结果为个人跑分、非官方数据，单次运行存在采样噪声，不应用于采购或发表决策。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个韩语基准数据集（含 KMMLU/KMMLU-Pro/MuSR(Ko) 等）
- 多供应商接入：Azure OpenAI、Bedrock、OpenAI 兼容/自托管 vLLM、Azure ML、Hugging Face
- 并行批量评估（多个 env 文件同时跑）与现成排行榜表格
- reasoning 档位对比列与 token 预算规避空响应的测量说明

## 适用场景

- 给自己的模型在韩语基准上跑分并生成排行榜
- 对比不同供应商/推理档位模型的韩语能力
- 在 Codespaces 中零配置复现评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmark LLMs/SLMs on Korean-language proficiency, reasoning, and professional-domain knowledge
> L5: Azure ML, Hugging Face), parallel batch evaluation, and ready-made leaderboard tables.

## 星数曲线

```mermaid
xychart-beta
    title "daekeun-ml/evaluate-llm-on-korean-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-26 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d9ac236af75f` · [字段定义](../../DATASET.md)*
