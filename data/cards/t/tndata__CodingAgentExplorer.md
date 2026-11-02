# tndata/CodingAgentExplorer

⭐ 53 · JavaScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/tndata/CodingAgentExplorer) · [官网](https://nestenius.se/ai/introducing-the-coding-agent-explorer-net/) · 个人维护

**给开发者的 .NET 实时代理与仪表盘，检视 Claude Code API 调用**

基于 ASP.NET Core 与 YARP 反向代理的本地观测工具：设置 ANTHROPIC_BASE_URL 指向 8888 端口代理，实时捕获并展示 Claude Code 与 Anthropic API 之间的请求/响应、SSE 流事件、token 用量与首 token 时间；MCP Observer 在 9999 端口代理任意 HTTP MCP 服务器流量，配套 HookAgent CLI 将 15 种 Claude Code hook 事件推送到仪表盘。API key 自动脱敏，数据仅存内存（上限 1000 条），代理只监听 localhost。运行需 .NET 10 SDK，从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向代理捕获 Claude Code 与 Anthropic API 的全部请求/响应与 SSE 流
- MCP Observer 代理并检视任意 HTTP MCP 服务器流量（JSON-RPC 方法级展示）
- HookAgent 桥接 15 种 Claude Code hook 事件到对话时间线
- API key 自动脱敏、仅监听 localhost、数据仅存内存不持久化

## 适用场景

- 调试或学习 AI 编程 agent 的 API 交互与工具调用细节
- 分析 token 用量、模型选择与首 token 延迟
- 检视 Claude Code 与 MCP 服务器之间的 JSON-RPC 流量
- 作为演示编码 agent 内部机制的教具

## 场景标签

 · 领域:AI 编程代理/可观测性工具

## 证据(README 行号)

> L3: A real-time .NET proxy and dashboard for inspecting Claude Code API calls. Intercept, visualize, and analyze every r
> L297: - ASP.NET Core with YARP reverse proxy
> L313: - API keys (`x-api-key` and `Authorization` headers) are automatically redacted from stored request data


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `490ec6e061e3` · [字段定义](../../DATASET.md)*
