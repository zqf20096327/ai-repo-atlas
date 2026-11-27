# zrg-team/memorall

⭐ 10 · TypeScript · MIT · 推送 2026-11-09 · [GitHub](https://github.com/zrg-team/memorall) · [官网](https://chromewebstore.google.com/detail/memorall/kcienfpnencfkniagcjlpaehofblfhab) · 组织维护

**本地优先的浏览器 Agent 工作台：把浏览内容变成可检索记忆**

一个本地优先的 agent 工作区，同一套 React 代码以 Chrome/Edge 扩展、静态 Web 应用和 Tauri 桌面应用（Windows/macOS/Linux）三种形态发布。核心机制是把页面、选区、文档转为可搜索的持久记忆，配 Flow Engine agent 运行时（图、中间件、工具、记忆检索、流式活动）。浏览器内可用 Wllama/WebLLM/Transformers 运行时，也可接外部模型服务。MemonOS 为 agent 提供共享桌面（Browser/Files/Terminal/Tasks），用户可随时接管。MIT 许可，核心可纯本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一代码库产出扩展、Web、桌面三端应用
- Flow Engine：图式流程、中间件、工具执行、记忆检索、流式活动
- 浏览器内运行时（Wllama/WebLLM/Transformers）与外部/本地服务器模型均可选
- MemonOS 共享桌面：agent 操作 Browser/Files/Terminal/Tasks，用户可接管

## 适用场景

- 把浏览过的页面和文档积累成可对话、可检索的知识库
- 在浏览器内描述并运行 agent 完成网页操作类任务
- 隐私敏感场景下全程本地运行 agent

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L37: - 🏠 Local-first by default. The app can run with in-browser runtimes such as Wllama, WebLLM, and Transformers, whil
> L103: Memorall's agent behavior runs on the **Flow Engine**, which now lives outside the
> L166: |`agent-harness-langgraph`|🔁 ReAct loops and ordered step pipelines backed by LangGraph|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `9c79bbf447e3` · [字段定义](../../DATASET.md)*
