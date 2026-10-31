# fastn-ai/fastn-mcp

⭐ 23 · Python · MIT · 推送 2026-06-07 · [GitHub](https://github.com/fastn-ai/fastn-mcp) · [官网](https://fastn.ai) · 组织维护

**面向 SaaS 的多租户 MCP 网关：给 AI agent 受控接入 250+ 集成**

Fastn 平台的 Model Context Protocol（MCP）服务器：通过单一多租户端点把 AI agent 与应用连接到 Slack、Jira、GitHub、Salesforce 等 250+ 服务，提供 OAuth 2.1 托管认证、基于角色的权限、审计日志与多步 Flow 自动化。面向构建 AI agent 的 SaaS 开发团队。支持 stdio/SSE/Streamable HTTP 三种传输；提供托管端点 mcp.live.fastn.ai，也可 pip 安装或 Docker 自部署。create_flow/update_flow 工具标注为开发中。

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

- 250+ 连接器，统一 MCP 端点暴露 11 个工具
- OAuth 2.1 托管认证与基于角色的治理、审计
- stdio / SSE / Streamable HTTP 多传输，Docker 自部署
- 多步工作流（Flow）创建、运行与管理

## 适用场景

- 让 Claude Desktop / Cursor 等 MCP 客户端直接操作 Slack、Jira、GitHub 等客户系统
- SaaS 产品为终端客户的 AI agent 提供受治理的集成访问
- 自托管 MCP 网关并用 Docker 部署到生产环境

## 场景标签

 · 领域:AI agent 基础设施/集成平台

## 证据(README 行号)

> L3: **Give your AI agents and apps secure, governed access to your customers' tools and systems through one multi-tenant
> L5: Part of Fastn, the embedded integration platform for SaaS products and AI agents. Fastn MCP Server is a production-r

## 星数曲线

```mermaid
xychart-beta
    title "fastn-ai/fastn-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9062b613d7b5` · [字段定义](../../DATASET.md)*
