# mohcodes01/Multi-Agent-Research-Assistant

⭐ 17 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/mohcodes01/Multi-Agent-Research-Assistant) · 个人维护

**开源深度研究 agent：多源搜索并生成带引用的研究报告**

基于 LangGraph 的开源深度研究 agent，通过多个 LLM 角色分工（摘要、研究、压缩、最终报告）协调搜索与分析流程，支持多种模型提供商、搜索工具与 MCP 服务器，默认使用 OpenAI 模型与 Tavily 搜索。本地经 LangGraph Server 启动并在 Studio UI 交互，也可部署到 LangGraph Platform 或 Open Agent Platform 供非技术用户使用。内置 Deep Research Bench 评测流程，并保留两个早期实现（plan-and-execute 工作流与 supervisor 多 agent 架构）于 src/legacy/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型配置：摘要/研究/压缩/报告四个环节可分别指定模型
- 支持多搜索工具、MCP 兼容、Anthropic/OpenAI 原生 web search
- Deep Research Bench 评测流程与提交脚本（RACE 分数 0.4344）
- 保留两种早期实现：plan-and-execute 工作流与 supervisor 多 agent 架构

## 适用场景

- 输入一个问题，让 agent 自动搜索并生成研究报告
- 在 LangGraph Studio 中调试与配置深度研究 agent
- 部署到 Open Agent Platform 供非技术用户配置使用
- 用 Deep Research Bench 数据集评测研究 agent 表现

## 场景标签

`科研工具` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Deep research has broken out as one of the most popular agent applications. This is a simple, configurable, fully op
> L66: - **Summarization** (default: `openai:gpt-4.1-mini`): Summarizes search API results

## 星数曲线

```mermaid
xychart-beta
    title "mohcodes01/Multi-Agent-Research-Assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [18, 17, 17]
```

2026-10-18 18 → 2026-10-29 17（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `3e12803275a7` · [字段定义](../../DATASET.md)*
