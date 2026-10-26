# agentcathq/agentcat-python-sdk

⭐ 53 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/agentcathq/agentcat-python-sdk) · [官网](https://agentcat.com) · 组织维护

**MCP 服务器分析 SDK：一行代码追踪 agent 工具调用与意图**

面向 MCP 服务器、Claude Connector 与 ChatGPT 插件开发者的分析平台 Python SDK。以中间件形式在 MCP 服务器内运行：调用 track() 后修改工具 schema，注入 session_id/agent_id/context 等参数，将相关工具调用聚合为任务、捕获 agent 调用意图，并记录 agent 找不到的功能；数据发送至 AgentCat 仪表板。同时支持向 OpenTelemetry、Datadog、Sentry 转发日志/追踪/错误。提供 redact 系列钩子做数据脱敏，内置诊断信号可用环境变量关闭。开源项目可免费使用完整平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- track() 一行接入，通过 SEP-2567 显式句柄在无状态传输下聚合会话
- 注入 context 参数让 agent 说明每次调用的意图，get_more_tools 收集缺失功能反馈
- 遥测可同时导出至 OpenTelemetry / Datadog / Sentry
- redact / redact_event 钩子支持自定义脱敏与事件丢弃

## 适用场景

- 我想看 agent 用户在我的 MCP 服务器上卡在哪一步
- 追踪多个部署中 agent 对工具的使用模式与来源客户端
- 为已有 MCP 服务器补齐日志与追踪，接入现有观测平台

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L30: AgentCat is an analytics platform for MCP server owners 🐱. It captures user intentions and behavior patterns to hel
> L50: - **Agent session replay** 🎬. Follow alongside your users and their agents to understand why they're using your MCP
> L58: AgentCat works as a lightweight middleware inside your MCP server. When you call `track()`, it seamlessly modifies 

## 星数曲线

```mermaid
xychart-beta
    title "agentcathq/agentcat-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `264c2faa7eb2` · [字段定义](../../DATASET.md)*
