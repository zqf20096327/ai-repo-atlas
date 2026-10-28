# isdaniel/mcp_weather_server

⭐ 60 · Python · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/isdaniel/mcp_weather_server) · 个人维护

**基于 Open-Meteo 的天气 MCP 服务器，供 AI 客户端调用**

为 Model Context Protocol (MCP) 客户端（如 Claude Desktop、Cline）提供天气与时区工具的 Python 服务器。数据来自免费开源的 Open-Meteo API，无需 API key。提供 8 个工具：当前天气、按日期范围天气、空气质量（含污染物指标与健康建议）等结构化与文本输出，以及时区查询与转换。支持 stdio、SSE 与 Streamable HTTP 三种传输模式，后两者可服务 Web 应用；可通过 pip、Smithery（npx）或 Docker 部署。城市名仅支持英文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个天气/空气质量/时区 MCP 工具，数据源 Open-Meteo，无需 API key
- 支持 stdio、SSE、Streamable HTTP 三种传输模式，含状态/无状态选项
- 空气质量报告对比 WHO 与 EPA 标准并给出敏感人群提示
- 提供 pip、Smithery、Docker 三种安装部署途径

## 适用场景

- 为 Claude Desktop 或 Cline 等 MCP 客户端接入天气与空气质量查询能力
- 以 SSE/Streamable HTTP 模式给 Web 应用提供天气数据接口
- 通过 Docker 部署供团队共享的天气 MCP 服务

## 场景标签

 · 领域:AI 工具服务/天气数据

## 证据(README 行号)

> L15: A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API. This server suppo
> L43:  * **stdio** - Standard MCP for desktop clients (Claude Desktop, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "isdaniel/mcp_weather_server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-28 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0a98c976a68b` · [字段定义](../../DATASET.md)*
