# vignesh2027/LLM-Evaluation-Framework

⭐ 15 · Python · MIT · 推送 2026-08-29 · [GitHub](https://github.com/vignesh2027/LLM-Evaluation-Framework) · [官网](https://vignesh2027.github.io/LLM-Evaluation-Framework/) · 个人维护

**多模型 LLM 评测框架：准确率/延迟/成本/幻觉/推理五指标对比**

基于 litellm 统一接口的 LLM 评测与基准测试框架，面向需要在同一提示集上横向对比 GPT-4、Claude、Gemini、Mistral、Llama 等模型的开发者。提供 5 类指标（准确率含精确/模糊匹配、延迟分位数、按 token 计价成本、幻觉率、推理质量），内置 MMLU、TruthfulQA 基准并支持自定义 CSV/JSON 数据集。接口覆盖 CLI（7 个子命令）、FastAPI REST API（12 端点）、Streamlit 仪表盘、异步 Python API 与 PDF 报告生成；SQLite 持久化，Docker 可部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 类指标：准确率（精确/归一化/多选/模糊匹配）、延迟 p50-p99、成本、幻觉率、推理质量
- 内置 MMLU（57 学科约 1.4 万题）与 TruthfulQA（817 题），支持自定义 CSV/JSON
- CLI / FastAPI REST / Streamlit 仪表盘 / 异步 Python API 四种接口
- SQLite 持久化与多阶段 Docker 部署

## 适用场景

- 在同一提示集上横向对比多个 LLM 供应商的表现
- 用 MMLU 或自定义数据集做模型选型前的基准测试
- 生成含成本与延迟的 PDF 评测报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L23: **This framework solves all of that.** It's the only open-source tool that evaluates GPT-4, Claude, Gemini, Mistral
> L133: |litellm|1.52.x|Unified LLM API|
> L333: |`POST`|`/evaluate`|Evaluate a model on a benchmark|

## 星数曲线

```mermaid
xychart-beta
    title "vignesh2027/LLM-Evaluation-Framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `278c7039d541` · [字段定义](../../DATASET.md)*
