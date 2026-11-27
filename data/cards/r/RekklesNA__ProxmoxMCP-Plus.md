# RekklesNA/ProxmoxMCP-Plus

⭐ — · [GitHub]() · 个人维护

**供运维通过 MCP/OpenAPI 安全控制 Proxmox VE 的控制面**

作为 AI 客户端与 Proxmox VE 之间的中间层，提供 MCP 与 OpenAPI 两种入口，操作 VM/LXC 生命周期、快照、备份、ISO 与持久化异步任务。安全机制包括 API token、OpenAPI bearer 认证、命令策略、审批 token、TLS 校验、工具白/黑名单过滤。提供 PyPI 包、Docker 部署与可选 Code Mode 沙箱及 OAuth（PKCE）浏览器授权，OAuth 状态存于 PostgreSQL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 与 OpenAPI 双入口覆盖 agent 与 HTTP 自动化场景
- 持久化 job_id/UPID 跟踪、轮询、重试、取消与审计历史
- API key、命令策略、审批 token、工具白/黑名单等安全护栏
- 可选 OAuth 授权码流（PKCE），状态持久化于 PostgreSQL

## 适用场景

- 在 Claude Desktop/Cursor 等客户端中管理 homelab 的 Proxmox 虚拟机与容器
- 通过 HTTP API 把 Proxmox 操作接入内部仪表盘与 no-code 工作流
- 对快照、备份等长耗时任务做异步跟踪与审计

## 场景标签

 · 领域:IT 基础设施/运维自动化

## 证据(README 行号)

> L5:  Operate Proxmox VE from MCP clients, AI agents, and OpenAPI tooling through one security-conscious control plane fo
> L31: ProxmoxMCP-Plus sits between AI clients and Proxmox VE so operators do not have to stitch together raw API calls, o
> L35: - `MCP` for Claude Desktop, Cursor, VS Code, Open WebUI, Codex, and other MCP-capable agents

## 星数曲线

```mermaid
xychart-beta
    title "RekklesNA/ProxmoxMCP-Plus 星数(近 21 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-25", "2026-11-26"]
    y-axis "stars" 608 --> 673
    line [613, 615, 618, 620, 624, 626, 628, 631, 634, 615, 645, 647, 648, 649, 650, 661, 662, 663, 664, 666, 668]
```

2026-10-24 613 → 2026-11-26 668（+55）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a3998c6ee6f8` · [字段定义](../../DATASET.md)*
