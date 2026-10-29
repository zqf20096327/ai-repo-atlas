# stacklok/toolhive-registry-server

⭐ 29 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/stacklok/toolhive-registry-server) · [官网](https://docs.stacklok.com/toolhive/guides-registry/) · 组织维护

**组织级 MCP 服务器/技能/插件的注册表与治理服务**

由 Stacklok 维护的 Go 服务，实现官方 MCP Registry API 规范，把来自 Git 仓库、Kubernetes 集群、上游注册表、本地文件与 Admin API 的 MCP 服务器、技能和插件聚合成多个命名目录（registry），供团队和 AI 客户端查询。治理机制包括基于 JWT claim 的条目可见性控制、OAuth 2.0/OIDC 认证、角色管理以及符合 NIST SP 800-53 AU-3 的审计日志。依赖 PostgreSQL 16+，提供 Docker 与源码构建两种运行方式，可作为独立服务或 ToolHive 平台组件部署。

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

- 实现官方 MCP Registry API 规范，兼容客户端开箱即用
- 五类来源聚合（Git/API/File/Managed/Kubernetes）与后台自动同步
- JWT claim 级可见性控制、OAuth 2.0/OIDC 认证与角色管理
- SIEM 合规审计日志与 OpenTelemetry 可观测性

## 适用场景

- 组织内统一发现与管控 MCP 服务器、技能和插件
- 按团队设置不同可见性的多目录组合
- 审计记录谁访问了哪些 MCP 资源
- 通过 Kubernetes CRD 自动发现集群内 MCP 服务器

## 场景标签

 · 领域:AI 基础设施/MCP 治理

## 证据(README 行号)

> L12: The ToolHive Registry Server aggregates MCP servers, skills, and plugins from Git repos, Kubernetes clusters, upstr
> L14: It implements the official Model Context Protocol (MCP) Registry API specification. If you're not familiar with MCP
> L41: - **Standards-compliant**: Implements the official MCP Registry API specification. Clients that speak the spec work

## 星数曲线

```mermaid
xychart-beta
    title "stacklok/toolhive-registry-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `df599c54c71a` · [字段定义](../../DATASET.md)*
