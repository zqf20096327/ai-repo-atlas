# johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction

⭐ 638 · Jupyter Notebook · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction) · 个人维护

**为个人用户将银行账单 PDF 自动化抽取入库并做财务分析与问答**

上传银行账单 PDF 后经共享流水线处理：抽取→可选 OCR→PII 脱敏→解析→校验→分类→存储→报告，账目落入 Postgres 账本，脱敏片段存入 Qdrant 供 RAG 问答。提供 Pipeline（默认）、CrewAI、Deep Agents 三种可切换 harness。本地 LLM 优先，通过 LiteLLM 接入 vLLM、SGLang、LM Studio、Ollama 等运行时；Docker Compose 一键启动 Postgres/Redis/Qdrant/RustFS/API 与 worker，前端为 React+Vite。GPU 为可选，默认 CPU 镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性流水线含 PyMuPDF 抽取、PII 脱敏、余额校验与 LLM 兜底解析
- 三种可切换 harness：Pipeline、CrewAI、Deep Agents
- 通过 LiteLLM 支持本地 LLM（vLLM、SGLang、LM Studio、Ollama）
- 提供 MCP stdio 接入 Claude Desktop/Cursor 及可选 YOLO+OCR

## 适用场景

- 把银行账单 PDF 批量转成可查询的 SQL 账本
- 本地部署下对账单做隐私脱敏与归类分析
- 用 RAG 问答方式查询账单中的交易明细
- 季度/年度财务汇总报表生成

## 场景标签

`RAG` `文档解析` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: > Upload bank-statement PDFs, extract a **Postgres ledger**, and ask questions with a **shared pipeline**. Choose **
> L56: Pipeline stages (shared by every harness): extract → optional OCR → redact PII → parse → verify → categorize → stor
> L64: - **Local LLM first** — vLLM, SGLang, Strata, LM Studio, Ollama via LiteLLM; live `/v1/models`

## 星数曲线

```mermaid
xychart-beta
    title "johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction 星数(近 13 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 628 --> 639
    line [629, 630, 629, 631, 633, 634, 635, 636, 635, 636, 637, 638, 638]
```

2026-10-26 629 → 2026-11-28 638（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `af7504cdae8c` · [字段定义](../../DATASET.md)*
