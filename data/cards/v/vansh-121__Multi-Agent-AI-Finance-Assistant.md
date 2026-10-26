# vansh-121/Multi-Agent-AI-Finance-Assistant

⭐ 28 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/vansh-121/Multi-Agent-AI-Finance-Assistant) · [官网](https://multi-agents-finance-assistant.streamlit.app) · 个人维护

**多 Agent 金融分析助手：LLM 驱动的股票研究与市场简报生成**

基于 Streamlit 前端与 FastAPI 后端的金融分析平台，由 8 个专用 Agent（API/抓取/检索/语言/分析/预测/绘图/语音）协作，接入 Google Gemini（gemini-2.0-flash-exp、gemini-2.5-pro）生成市场简报。数据来自 Yahoo Finance，覆盖 460+ 股票、98 只 ETF 与 20+ 加密货币；支持基于多项式回归的盈利预测、组合风险敞口分析与语音交互。检索用 LangChain+FAISS 实现 RAG。需自备 Gemini API key，免费额度有限制，本地运行需 Python 3.10+ 并手动启动前后端，也提供 Docker 镜像构建方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个专用 Agent 协作处理金融数据（API/抓取/检索/语言/分析/预测/绘图/语音）
- 接入 Google Gemini，配 API 限流时的智能回退机制
- 460+ 全球股票、98 只 ETF、20+ 加密货币，数据来自 Yahoo Finance
- scikit-learn 多项式回归做盈利与增长率预测

## 适用场景

- 让 AI 生成覆盖多只股票的市场简报与风险分析
- 对比全球股票走势并查看 ML 盈利预测图表
- 通过语音提问获取金融分析结果

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L15: The **Multi-Agent AI Finance Assistant** is an open-source platform designed to provide intelligent financial analy
> L68: - **Multi-Agent Collaboration**: Specialized agents (API Agent, Scraping Agent, Retriever Agent, Analysis Agent, La
> L89: - **Report Generation**: Automatically generates professional market briefs with real Yahoo Finance data and AI ana

## 星数曲线

```mermaid
xychart-beta
    title "vansh-121/Multi-Agent-AI-Finance-Assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-26 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `65e3ad6e65cb` · [字段定义](../../DATASET.md)*
