# shinzo-labs/shinzo

⭐ 32 · TypeScript · NOASSERTION · 推送 2026-02-06 · [GitHub](https://github.com/shinzo-labs/shinzo) · [官网](https://shinzo.ai) · 组织维护

**AI agent 与 MCP 服务器的可观测性平台**

开源可观测性平台，供开发者采集和分析 agentic AI 系统与 MCP 服务器的性能数据。架构含 OpenTelemetry Collector、Postgres 数据库和分析 Web 前端，数据符合 OpenTelemetry 规范，可接入其他 OTel 兼容软件；提供 TypeScript 与 Python 插桩 SDK，路线图含 Token 分析、会话管理洞察及多语言 SDK。部署要求外部 PostgreSQL 15+（不跑在 Docker 内），支持 Docker Compose 或 Node.js 18+/pnpm 本地开发。采用 fair-code 许可（Sustainable Use License + Shinzo Enterprise License），另有企业许可可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenTelemetry Collector + Postgres + 分析前端的平台架构
- 数据符合 OpenTelemetry 规范，可接入其他 OTel 兼容软件
- TypeScript 与 Python 插桩 SDK（Go/C#/Java/Rust SDK 在路线图中）
- fair-code 双许可：Sustainable Use License 与 Shinzo Enterprise License

## 适用场景

- 采集并分析 AI agent 与 MCP 服务器的性能遥测数据
- 在仪表盘中查看实时分析、trace 分析与工具使用统计
- 排查推理低效与真实 agent 使用模式

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L25:  Shinzo is an open source observability platform that enables developers to ingest and analyze the performance data
> L29: - **OpenTelemetry Collector**: High-performance OpenTelemetry backend service that ingests and serves telemetry dat

## 星数曲线

```mermaid
xychart-beta
    title "shinzo-labs/shinzo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fb226b52e58e` · [字段定义](../../DATASET.md)*
