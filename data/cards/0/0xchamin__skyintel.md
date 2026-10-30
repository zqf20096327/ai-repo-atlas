# 0xchamin/skyintel

⭐ 19 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/0xchamin/skyintel) · [官网](https://voyage.skyintel.dev/) · 个人维护

**给 AI agent 的空海天实时追踪 MCP 服务器，含 3D 地球与 CLI**

Python/Starlette 后端 + CesiumJS 前端的实时追踪平台：通过 ADSB.lol 轮询航班、aisstream.io WebSocket 接收 AIS 船舶、Celestrak+SGP4 计算卫星位置，数据落入 SQLite（WAL、R*Tree 空间索引）。以 FastMCP 暴露 25+ 工具（streamable HTTP 与 stdio 两种传输），供 Claude Desktop / Claude Code / VS Code / Cursor 等 MCP 客户端调用；另提供 REST API、BYOK LLM 网关聊天（LiteLLM，SSE 流式）、CLI 与 /playground 可观测面板。零配置即可用航班+卫星，船舶/地形/地理编码需各自 API key，缺失时对应域禁用。限制：仅陆基 AIS（离岸约 50-70 海里），卫星 AIS 未集成；MCP 仅限本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25+ MCP 工具，支持 streamable HTTP 与 stdio 两种传输
- 空（ADSB.lol）海（AIS WebSocket）天（Celestrak+SGP4）三域数据统一入 SQLite
- BYOK AI 聊天网关经 LiteLLM 支持 Claude/OpenAI/Gemini，SSE 流式输出
- 零配置可用（航班+卫星），API key 缺失时按域优雅降级

## 适用场景

- 让 Claude Desktop / VS Code / Cursor 等 agent 查询实时航班、船舶、卫星位置
- 在 3D 地球上可视化查看军事/民用航空器与各类船舶动态
- 通过 CLI 或 REST API 获取港口、天气、ISS 过境等空间查询结果

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L27: - 🤖 **MCP Server** — 25+ tools via FastMCP, streamable HTTP + stdio for Claude Desktop / VS Code / Cursor
> L141: VoyageIntel is a **Python/Starlette backend** with a **vanilla JS + CesiumJS frontend** and no build step. Three b
> L163: VoyageIntel exposes 25+ MCP tools via **two transports**:

## 星数曲线

```mermaid
xychart-beta
    title "0xchamin/skyintel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0cda45e605f2` · [字段定义](../../DATASET.md)*
