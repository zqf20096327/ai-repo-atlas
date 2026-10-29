# DevilsAutumn/quater

⭐ 20 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/DevilsAutumn/quater) · [官网](https://quater.devilsautumn.com) · 个人维护

**给后端开发者：一个 handler 同时暴露为 HTTP、MCP 工具与 CLI 的 Python 框架**

Python 3.11+ 后端 Web 框架。核心机制：路由只需注解一次，同一 handler 即可作为 HTTP 接口、MCP 工具（tool=True）与本地/远程 CLI 动作（cli=True）供人或 AI agent 调用，认证按暴露面分别配置。默认启用主机检查、CORS、请求体限制与请求 ID，每个请求携带来源与入口元数据用于审计。基于 Granian/RSGI 与 msgspec JSON。版本为 0.x.x，作者声明可能含破坏性变更，需锁定版本并阅读发布说明。通过 pip/uv 安装，附 CLI 开发命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一视图同时服务 HTTP、MCP 与 CLI，三个入口共享同一 handler
- tool=True / cli=True 单个标志即可将路由暴露给 MCP 客户端或 AI agent
- 默认启用请求安全检查（主机校验、CORS、请求体限制、请求 ID）
- 每个请求携带来源与入口元数据，审计日志可区分人类与 AI agent

## 适用场景

- 构建可同时供前端和 AI agent 使用的后端服务
- 将选定后端操作以 MCP 工具形式暴露给 MCP 客户端
- 让 AI agent 通过带审批钩子与 dry-run 的 CLI 操作生产应用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L31: Quater is a Python backend framework built for this shift. You build a normal
> L42: - One view serves HTTP, MCP, and CLI. You annotate the route once and all three entry points share the same handler
> L153: - **For MCP Clients:** `tool=True` exposes selected routes through MCP with

## 星数曲线

```mermaid
xychart-beta
    title "DevilsAutumn/quater 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `14c8e05cbd31` · [字段定义](../../DATASET.md)*
