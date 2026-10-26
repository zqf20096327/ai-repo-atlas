# Clivern/Sloth

⭐ 197 · Go · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Clivern/Sloth) · [官网](https://sloth.clivern.com) · 个人维护

**面向 AI agent、API 与 MCP 服务器的网关和服务发现注册中心**

Sloth 是一个网关与服务发现注册中心，面向 AI agent、API 和 MCP 服务器。用户注册自己的 AI agent 后，各 agent 之间可以相互发现，所有调用经由单一网关路由，由网关处理负载均衡、健康检查与策略。项目遵循语义化版本管理，以 MIT 许可证发布，通过 GitHub Releases 提供版本变更记录。README 未提供安装与运行说明。

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

- AI agent、API 与 MCP 服务器的统一网关与服务发现注册
- 通过单一网关路由调用，处理负载均衡、健康检查与策略
- 遵循语义化版本管理，MIT 许可证发布

## 适用场景

- 多个 AI agent 之间做服务发现与相互调用
- 将 agent/API/MCP 调用统一经网关路由并施加策略
- 对后端服务做负载均衡与健康检查

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: Sloth is a gateway and service discovery registry for AI agents, APIs and MCP servers. Register your AI agent, let 

## 星数曲线

```mermaid
xychart-beta
    title "Clivern/Sloth 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-26"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-24 197 → 2026-10-26 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1af3974dcf80` · [字段定义](../../DATASET.md)*
