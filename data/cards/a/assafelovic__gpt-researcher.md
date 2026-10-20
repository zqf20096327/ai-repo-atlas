# assafelovic/gpt-researcher

⭐ 30,158 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/assafelovic/gpt-researcher) · [官网](https://gptr.dev) · 个人维护

**为研究任务生成带引文报告的自主深度研究 Agent**

面向个人与组织的自动化研究 Agent：将任务拆解为研究问题，由 planner 与 execution 多智能体分工检索、汇总并生成超过 2,000 词、引用 20+ 来源的报告。支持网页与本地文档（PDF、CSV、Excel、Markdown、Word 等）两类数据源，提供 pip 包、Docker 部署、HTML/NextJS 前端、MCP 客户端与服务端、LangGraph 多智能体助手及 LangSmith 追踪。默认依赖 OpenAI 与 Tavily API key，也可通过 OPENAI_BASE_URL 接入自定义模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 7.4 天,年发版 13,252 位贡献者
- 涨星:近 1 天 **+19**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:— · 协议:OPENAI-API / MCP

## 能力要点

- planner/execution/publisher 多智能体架构，递归式广度+深度研究
- 支持网页搜索与本地文档研究，报告可导出 PDF/Word/Markdown
- Jev 上下文过滤，无 key 时回退 BM25 关键词过滤
- 提供 MCP Server（独立仓库 gptr-mcp）与 Claude Desktop 集成

## 适用场景

- 为调研课题自动生成带引用来源的研究报告
- 基于本地文档库开展检索与汇总研究
- 通过 MCP 把深度研究能力接入 Claude 等 AI 应用
- 用 LangGraph 多智能体演示从规划到发布的协作流程

## 场景标签

`科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L20: **GPT Researcher the first open deep research agent designed for both web and local research on any given task.**
> L22: The agent produces detailed, factual, and unbiased research reports with citations. GPT Researcher provides a full 
> L51: The core idea is to utilize 'planner' and 'execution' agents. The planner generates research questions, while the e

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `c31ac8559e4e` · [字段定义](../../DATASET.md)*
