# intelligexhq/chronos

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-06-22 · [GitHub](https://github.com/intelligexhq/chronos) · [官网](https://intelligex.com/chronos) · 组织维护

**自托管的 Agent 与 MCP 服务控制平面**

面向团队部署和管理 AI agent 的自托管控制平面：支持在可视化画布上构建 agent，或注册任何框架的外部 HTTP agent（OpenAI API 规范）；提供 MCP 工具注册表与统一网关，为所有工具调用做凭据代理与审计；内置治理功能（SSO、RBAC、停止开关、审计日志、PII 脱敏）与基于 OpenTelemetry 的可观测性；支持 cron 式定时运行 agent。以 Docker 容器方式部署，Apache 2.0 许可，另提供专业服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化画布构建 agent 或注册外部 HTTP agent
- 统一 MCP 工具注册表与带审计的网关
- 内置 SSO/RBAC/审计日志/PII 脱敏等治理功能
- OpenTelemetry 可观测性与 cron 式定时 agent 运行

## 适用场景

- 统一托管和管理内外部 AI agent 及其工具调用
- 对 MCP 工具访问做凭据代理与审计合规
- 团队内以 RBAC 和 SSO 控制 agent 使用权限

## 场景标签

`Agent 框架` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L8: > Create agents visually on the built-in canvas, or register external agents from any framework — broker every tool 
> L14: - _Intelligex Chronos is a controll plane for agents and MCP servers_ - deploy, run and manage agents built on the 
> L15: - _MCP tool registry and gateway._ Register all MCP tools, build controll policies and expose them via unified MCP 

## 星数曲线

```mermaid
xychart-beta
    title "intelligexhq/chronos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a8b617a36f2c` · [字段定义](../../DATASET.md)*
