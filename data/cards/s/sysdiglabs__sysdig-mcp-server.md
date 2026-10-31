# sysdiglabs/sysdig-mcp-server

⭐ 14 · Go · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/sysdiglabs/sysdig-mcp-server) · 组织维护

**将 Sysdig 监控数据通过 MCP 暴露给 LLM 的服务器**

Sysdig 官方维护的 MCP Server 实现，将 Sysdig Monitor 的 Kubernetes 与容器监控能力以工具形式暴露给 LLM 客户端（如 Claude Desktop、Cursor）。提供 18 个 k8s 查询工具（集群/节点/工作负载/CPU/内存 Top、不可用 Pod、HTTP/网络错误等），基于 PromQL 聚合查询；工具列表按 API token 权限动态过滤。支持 stdio/streamable-http/sse 三种传输，可用 Go、Docker 镜像或预编译二进制运行。注意：下一主版本将移除 Sysdig Secure 专用工具，转由 @sysdig/secure-mcp-server 承接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个 Kubernetes 监控查询工具（Top CPU/内存/重启/错误/低利用率等）
- 按 API token 权限动态过滤可用工具
- 支持 stdio / streamable-http / sse 三种 MCP 传输协议
- 提供 Go、Docker 镜像与预编译二进制三种运行方式

## 适用场景

- 在 Claude Desktop 或 Cursor 中用自然语言查询 Kubernetes 集群状态
- 让 LLM 排查高 CPU/内存消耗、Pod 重启与 HTTP 错误问题
- 通过远程 MCP 部署供团队共享访问 Sysdig 监控数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: This is an implementation of an MCP (Model Context Protocol) Server that exposes Sysdig Monitor capabilities to LLM
> L16: For Sysdig Secure-specific workflows, use the dedicated @sysdig/secure-mcp-server.

## 星数曲线

```mermaid
xychart-beta
    title "sysdiglabs/sysdig-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f3d6033e67c6` · [字段定义](../../DATASET.md)*
