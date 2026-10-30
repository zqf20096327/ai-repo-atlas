# MiXaiLL76/n8n-nodes-sgr-tool-calling

⭐ 26 · TypeScript · GPL-3.0 · 推送 2025-12-04 · [GitHub](https://github.com/MiXaiLL76/n8n-nodes-sgr-tool-calling) · [官网](https://www.npmjs.com/package/n8n-nodes-sgr-tool-calling) · 个人维护

**面向 n8n 的 SGR 深度研究 Agent 节点（Python 项目移植）**

将 sgr-agent-core Python 项目移植为 n8n 社区节点的 AI 研究 Agent：基于 OpenAI function calling，内置 6 个系统工具（推理、最终回答、带引用的报告生成、澄清提问、计划生成与调整），可连接 OpenAI/Anthropic 等语言模型、Tavily 搜索、MCP 与 LangChain 工具及记忆节点。支持澄清流程（暂停等待用户补充答案）、可配置最大迭代/搜索/澄清次数、自定义最终回答 JSON Schema 与提示词。通过 n8n 社区节点文档指引安装，AGPL-3.0 许可并另售商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 6 个研究用系统工具（推理/最终回答/带引用报告/澄清/计划生成与调整）
- 可连接 OpenAI/Anthropic 模型、Tavily 搜索、MCP Client、LangChain 工具与记忆节点
- 澄清流程：暂停执行等待用户补充答案后带上下文继续
- 自定义最终回答 JSON Schema，含校验与字段提取

## 适用场景

- 在 n8n 工作流中搭建带计划与澄清能力的深度研究 Agent
- 生成带引用的结构化研究报告
- 通过 MCP/LangChain 工具扩展 Agent 的检索与计算能力

## 场景标签

`Agent 框架` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L5: AI research agent with OpenAI function calling for n8n. Port of sgr-agent-core Python project.
> L17: 1. Add **SGR Agent** node to your workflow

## 星数曲线

```mermaid
xychart-beta
    title "MiXaiLL76/n8n-nodes-sgr-tool-calling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f93582d10073` · [字段定义](../../DATASET.md)*
