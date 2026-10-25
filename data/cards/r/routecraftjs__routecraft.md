# routecraftjs/routecraft

⭐ 36 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/routecraftjs/routecraft) · [官网](https://routecraft.dev/) · 组织维护

**开源 AI 自动化平台：把能力写成类型化 TypeScript 路由供 agent 复用**

Routecraft 是用 TypeScript 编写的开源 AI 自动化平台：开发者将一个能力定义为从 source 经过操作到 destination 的类型化路由（pipeline），同一路由可作为 MCP 工具、本地 agent 工具、HTTP 端点或定时任务暴露，区别仅在 source。Agent 本身也是路由，模型调用可套用 authorize/throttle/retry/timeout/circuitBreaker 等守卫。提供 CLI（craft，基于 Bun>=1.1.0）、项目脚手架、插件体系、隔离 shell 执行（含每命令一次性 Docker 容器）与管理 API；附带 craft-harness 完整 agent 示例（聊天、沙箱 shell、记忆、审批等）。Node 用户可编程嵌入核心库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 能力即路由：同一类型化路由可暴露为 MCP 工具/HTTP 端点/定时任务/本地工具
- Agent 亦为路由，模型调用套用 .authorize()/.throttle()/.retry()/.circuitBreaker() 守卫
- .defer()/.resume() 支持跨重启、跨传输的持久化会话恢复
- shell() 隔离执行（含一次性 Docker 容器、默认拒绝出网）与插件扩展体系

## 适用场景

- 团队把共享能力写成路由，供各 agent、编辑器与服务凭证统一复用
- 本地先验证路由，再提升为团队 harness 运行
- 通过 MCP/ACP 让 Claude Desktop 或编辑器调用自定义工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Routecraft is the open source AI automation platform your teams build on together. A capability is a route: a typed
> L64: - **MCP both ways.** Expose routes as tools with `mcp()` and the `mcp` plugin; call other servers' tools as `MCP(se
> L98: - `packages/ai` – AI integrations: LLM providers, agents, embeddings, MCP server / client, ACP

## 星数曲线

```mermaid
xychart-beta
    title "routecraftjs/routecraft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8004b847809c` · [字段定义](../../DATASET.md)*
