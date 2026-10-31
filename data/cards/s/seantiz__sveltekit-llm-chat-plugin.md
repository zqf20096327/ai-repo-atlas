# seantiz/sveltekit-llm-chat-plugin

⭐ 13 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/seantiz/sveltekit-llm-chat-plugin) · 个人维护

**SvelteKit 的 LLM 流式聊天连接插件：统一 WebSocket/SSE 接口**

提供单个 newConnection() 函数，将两类流式连接组合为统一的 StreamConnection 接口：WebSocket 用于本地服务（先连接后发送），SSE 用于外部 API（POST 请求负载并通过 web Response API 消费响应流）。面向在 SvelteKit 中接入 LLM 聊天流式输出的开发者，不含客户端应用或 UI，sendChat() 仅作接线示例。README 列出常见错误类型，并说明远程函数暂不支持持久流式连接，需使用 +server.ts 端点以保障 API key 安全。目前尚无测试覆盖，作者欢迎提交测试 PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- newConnection('websocket'|'sse', url) 统一两类流式连接
- WebSocket 用于本地服务，SSE 用于外部 API（POST + Response 流）
- 提供 sendChat() 客户端接线示例
- 说明 SvelteKit 远程函数暂不支持持久流式连接，建议使用 +server.ts 端点

## 适用场景

- 在 SvelteKit 应用中接入 LLM 聊天的流式输出
- 同一接口下切换本地 WebSocket 服务与外部 SSE API
- 参考 sendChat() 示例将流连接接入自己的 UI

## 场景标签

 · 领域:Web 前端/LLM 集成

## 证据(README 行号)

> L4: One newConnection() function that composes any streaming connection: WebSocket for local services, SSE for external 
> L13: The `sendChat()` client-side task is just to give you an idea of how you'd wire up the plugin to your UI. There's n

## 星数曲线

```mermaid
xychart-beta
    title "seantiz/sveltekit-llm-chat-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a201f3b1e952` · [字段定义](../../DATASET.md)*
