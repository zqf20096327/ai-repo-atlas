# langchain-ai/data-enrichment-js

⭐ 28 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/langchain-ai/data-enrichment-js) · 组织维护

**LangGraph 数据富集 agent 模板：开放式网络调研生成结构化 JSON**

基于 LangGraph.js 的 agent 模板，运行于 LangGraph Studio：输入研究主题与用户定义的 extractionSchema，agent 自动搜索网络（Tavily）、读取网页提取关键信息、按 schema 组织结果并校验完整性。模型默认 anthropic/claude-3-5-sonnet-20240620，可切换 OpenAI、Fireworks 等兼容模型；支持自定义 prompt、扩展工具（TypeScript 函数）与图节点。需在 .env 配置 Tavily 与模型 API key，依赖 @langchain/langgraph 与 @langchain/core。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入主题+JSON schema，自动网络调研并输出结构化结果
- 默认 Anthropic 模型，支持 provider/model-name 格式切换模型
- 可在 src/enrichment_agent/tools.ts 添加工具、graph.ts 扩展节点
- LangGraph Studio 中可视化调试，支持状态回放与热重载

## 适用场景

- 从开放式网络调研结果填充数据库或表格
- 按自定义 schema 批量提取主题相关信息
- 作为 LangGraph.js agent 开发的起点模板进行改造

## 场景标签

`Agent 框架` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L7: Producing structured results (e.g., to populate a database or spreadsheet) from open-ended research (e.g., web resea
> L25: You will need the latest versions of `@langchain/langgraph` and `@langchain/core`. See these instructions for help 

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/data-enrichment-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `60e0d9cc684d` · [字段定义](../../DATASET.md)*
