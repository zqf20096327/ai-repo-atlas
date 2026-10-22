# pab1it0/prometheus-mcp-server

⭐ 519 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/pab1it0/prometheus-mcp-server) · 个人维护

**让 AI 助手查询分析 Prometheus 指标的 MCP 服务器**

基于 Model Context Protocol 的服务器，为 Claude Desktop、VS Code、Cursor、Windsurf 等 MCP 客户端提供访问 Prometheus 的标准化接口：AI 助手可执行 PromQL 即时/区间查询、列出与检索指标元数据、查看抓取目标。支持 Basic/Bearer/mTLS 等多种认证、stdio/http/sse 三种传输模式，工具集可配置以控制上下文占用。提供 Docker、Helm Chart（Kubernetes）与源码（uv）三种安装方式，需已有可达的 Prometheus 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 MCP 工具：PromQL 即时/区间查询、指标列举、元数据、抓取目标、健康检查
- 支持 Basic/Bearer token/mTLS/多租户 ORG_ID 等认证方式
- stdio/http/sse 三种传输模式，HTTP 可无状态多副本部署
- Docker、Helm Chart、源码三种安装途径，工具集可按需裁剪

## 适用场景

- 在 Claude Desktop 等 MCP 客户端中直接用自然语言查询监控指标
- 让 AI 助手分析 Prometheus 指标数据定位系统问题
- Kubernetes 环境通过 Helm 部署供多个 AI 客户端共用

## 场景标签

 · 领域:DevOps/可观测性工具

## 证据(README 行号)

> L12: A [Model Context Protocol][mcp] (MCP) server that provides access to your Prometheus metrics and queries through st
> L19: - MCP-compatible client (Claude Desktop, VS Code, Cursor, Windsurf, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "pab1it0/prometheus-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 518 --> 520
    line [519, 519]
```

2026-10-18 519 → 2026-10-22 519（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `cf46b284021f` · [字段定义](../../DATASET.md)*
