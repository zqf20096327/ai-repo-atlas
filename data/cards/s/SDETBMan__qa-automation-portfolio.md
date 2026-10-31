# SDETBMan/qa-automation-portfolio

⭐ 38 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/SDETBMan/qa-automation-portfolio) · 个人维护

**SDET 个人作品集 monorepo：26+ 个测试自动化与 AI 评测框架**

个人维护的单体仓库，收纳 27 个独立框架，覆盖 UI/接口/合同测试（Playwright、Selenium、Cypress、Karate、Pact、Postman）、LLM 评测（DeepEval 三套：RAG/对话/Agent）、Agent 开发（LangChain RAG、LangGraph、DSPy、Claude 工具调用）、k6 性能、flakiness 检测、站点漂移监控、漏洞聚合、ISO 9001/SOC 2 合规证据收集与依赖审计，统一通过 GitHub Actions CI 驱动并上报 DataDog。另有三个独立仓库聚焦金融域对抗式 AI 测试。各框架按语言分别要求 Python 3.11+、Node.js 22、Java 17、.NET 8 等前置条件。

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

- DeepEval 驱动的三套 LLM 评测框架（RAG/对话/Agent），含成本与延迟上报 DataDog
- LangChain RAG、LangGraph 多 Agent 图、DSPy prompt 优化等 Agent 工程框架
- Playwright/Selenium/Cypress/Cucumber 的 POM、并行、自愈定位器（Healenium）、视觉回归等能力矩阵
- QMS 证据收集（ISO 9001/SOC 2/ISO 17025）与 flakiness、站点漂移、依赖审计工具链

## 适用场景

- 我作为 SDET 求职者展示测试自动化与 AI 评测工程能力
- 参考现成的 LLM 评测（RAG/对话/Agent）框架与 CI 集成方式
- 了解 Playwright/Selenium/Cypress 等框架的能力覆盖与对比
- 复用 flakiness 检测、合规证据收集等平台工程脚手架

## 场景标签

`模型评测` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L46: |`ai-eval`|Python|DeepEval · Pytest · OpenAI · ChromaDB · Python 3.11|→|
> L59: |`langchain-rag`|Python|LangChain 0.3 · LCEL · Chroma · OpenAI `gpt-4o-mini` · Langfuse · Python 3.11|→|
> L61: |`dspy-optimizer`|Python|DSPy 2.6 · BootstrapFewShot · OpenAI `gpt-4o-mini` · Python 3.11|→|

## 星数曲线

```mermaid
xychart-beta
    title "SDETBMan/qa-automation-portfolio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2497068ebb59` · [字段定义](../../DATASET.md)*
