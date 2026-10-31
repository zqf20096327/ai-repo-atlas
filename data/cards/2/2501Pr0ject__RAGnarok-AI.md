# 2501Pr0ject/RAGnarok-AI

⭐ 15 · Python · AGPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/2501Pr0ject/RAGnarok-AI) · [官网](https://ra-gnarok-ai-q3an.vercel.app) · 组织维护

**本地优先的 RAG 评测框架：评估、基准与监控 RAG 流水线**

面向 LLM 应用开发者的 Python RAG 评测框架，全部功能本地运行，无需 API key，数据不出本机。提供检索指标（Precision@K、Recall@K、MRR、NDCG）与基于本地 Prometheus 2 的 LLM-as-Judge 生成指标（忠实度、相关性、幻觉、完整性），支持按自有标签校准裁判。支持断点续跑的批量评测、从知识库或生产流量生成测试集、漂移检测、A/B 对比、Prometheus 指标导出与 CI 门控。通过适配器接入 LangChain、LangGraph、LlamaIndex、DSPy 等框架，以及 Ollama、vLLM、OpenAI、Anthropic 等模型后端。核心不含 torch/transformers。CLI 优先设计，提供 JSON 输出与退出码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 本地评测（Ollama + Prometheus 2），无需 API key，支持气隙部署
- LLM-as-Judge 可按自有标签校准（kappa、错误率、阈值调优）
- BatchEvaluator 按批次断点续跑，长时评测崩溃后无需重算
- 提供 LangChain/LangGraph/LlamaIndex/DSPy/vLLM/OpenAI/Anthropic 等适配器

## 适用场景

- 在 CI/CD 中对 RAG 流水线做持续质量门控
- 对医疗、法律等敏感数据做不出本机的私有 RAG 评测
- 对比不同嵌入模型或配置的 RAG 效果并检测回归
- 监控生产环境 RAG 质量与漂移

## 场景标签

`模型评测` `RAG` · 领域:评测与运维

## 证据(README 行号)

> L5:  Evaluate, benchmark, and monitor your RAG pipelines — 100% locally, no API keys required.
> L73: Excellent evaluation frameworks exist (RAGAS, DeepEval, TruLens...). ragnarok-ai doesn't try to have more metrics t
> L81: |**Engineering tool, not a notebook**|CLI-first, JSON output, exit codes, `--fail-under` CI gates, regression detec

## 星数曲线

```mermaid
xychart-beta
    title "2501Pr0ject/RAGnarok-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `9627a2c4131c` · [字段定义](../../DATASET.md)*
