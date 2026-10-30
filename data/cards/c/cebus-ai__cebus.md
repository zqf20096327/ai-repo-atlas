# cebus-ai/cebus

⭐ 29 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/cebus-ai/cebus) · [官网](https://www.cebus.ai/) · 组织维护

**多模型群聊编排平台：单会话同时对话多个 AI 模型**

基于 LangGraph hub-and-spoke 架构的多模型群聊平台，提供终端 CLI、Web UI 与 VS Code 扩展三种界面。用户可在同一会话中与 OpenAI、Anthropic、Gemini、GitHub Copilot、Ollama、OpenRouter 等模型对话，支持全部同时响应、逐个响应、@提及、角色分工等聊天模式，以及 AI 编排者与 Team Leader 多轮协作模式。推荐搭配 Copilot CLI SDK 使模型具备文件编辑、终端访问等 agent 能力，也支持 MCP 工具服务器。需 Node.js ≥24 运行，better-sqlite3 原生模块需与 Node 版本匹配。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一会话接入 OpenAI/Anthropic/Gemini/Copilot/Ollama/OpenRouter 多模型
- LangGraph hub-and-spoke 编排，含 AI Orchestrator 与 Team Leader 多轮协作模式
- 三种界面：终端 CLI、Web UI（频道/线程/富内容块）、VS Code 扩展
- Copilot SDK 集成内置文件编辑、shell、搜索等工具，无需 MCP 配置

## 适用场景

- 提问一次同时获取多个模型的回答对比
- 给不同模型分配开发者/QA/设计等角色协同处理任务
- 配合 Copilot SDK 让多个模型以团队形式操作代码库

## 场景标签

`聊天机器人` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: Built on LangGraph for orchestration with a hub-and-spoke architecture.
> L42: - **LangGraph Orchestration** — Hub-and-spoke architecture with sequential, tag-only, free-chat, raw, dynamic orche
> L46: - **Copilot SDK Integration** — Native integration with GitHub Copilot via `@github/copilot-sdk`. SDK-managed sessi

## 星数曲线

```mermaid
xychart-beta
    title "cebus-ai/cebus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2c2a2b63beaa` · [字段定义](../../DATASET.md)*
