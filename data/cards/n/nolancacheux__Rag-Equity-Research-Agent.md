# nolancacheux/Rag-Equity-Research-Agent

⭐ 19 · Python · MIT · 推送 2026-05-01 · [GitHub](https://github.com/nolancacheux/Rag-Equity-Research-Agent) · 个人维护

**面向个人投资者的自主股票研究 Agent：聚合多源数据生成研报**

自主执行股票研究的 AI agent：以 LangGraph 编排，从 Yahoo Finance 获取实时行情、用混合 RAG（BM25+dense+RRF）检索 SEC 10-K/10-Q 文件、分析财报电话会、聚合 Reddit 情绪，并输出 DCF 估值、1-10 级风险评分、同行对比与研究报告。通过 Telegram bot 命令或 FastAPI REST 接口交互，本地用 Docker Compose 启动 Qdrant，云端经 Terraform 部署到 Azure Container Apps。LLM 默认使用 Groq（Llama 3.3 70B 免费档），Azure OpenAI 为可选后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多源数据聚合：Yahoo Finance、SEC EDGAR、Reddit、DuckDuckGo
- 混合 RAG：BM25 稀疏 + dense 嵌入 + RRF 融合，基于 Qdrant
- DCF 估值与 10-K 风险因子评分（1-10 级）
- Telegram bot 命令与 FastAPI REST 双交互界面

## 适用场景

- 让 AI 代为完成某只股票的完整研究并生成报告
- 查询行情、DCF 估值、风险评分与同行对比
- 维护自选股清单并设置价格/市盈率预警

## 场景标签

`RAG` `金融量化` · 领域:知识与检索

## 证据(README 行号)

> L14: An autonomous AI agent that performs professional-grade equity research by aggregating and analyzing multiple data 
> L25: User: "Analyze NVIDIA's position. Compare P/E with AMD, check 10-K for China risks."
> L34: 6. Generates a professional research report

## 星数曲线

```mermaid
xychart-beta
    title "nolancacheux/Rag-Equity-Research-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `198a15522802` · [字段定义](../../DATASET.md)*
