# agentailor/create-mcp-server

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/agentailor/create-mcp-server) · [官网](https://www.agentailor.com/) · 组织维护

**脚手架工具：快速生成生产级 MCP 服务器项目**

面向构建 MCP 服务器的开发者的 npm CLI 脚手架，通过 npx 一条命令生成基于 MCP TypeScript SDK v2 的 TypeScript 项目。生成的项目支持 HTTP（streamable）与 stdio 两种传输、可选 OIDC OAuth、内置 Dockerfile、测试套件与 MCP Inspector 调试命令，并附带工具设计技能文件与 AGENTS.md 指南。限制：仅支持 sdk 框架，FastMCP 支持已在 0.10.0 移除，--template 选项已弃用。

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

- 基于 MCP TypeScript SDK v2（拆分包结构）生成 TypeScript 项目
- HTTP（streamable）与 stdio 两种传输，可选 OIDC OAuth
- 生成的项目含 Dockerfile、开箱即绿测试套件与 MCP Inspector 调试
- 内置工具设计技能（.agents/skills/）与 AGENTS.md 指南

## 适用场景

- 快速搭建生产级 MCP 服务器项目骨架
- 为 Claude Desktop 等本地客户端生成 stdio MCP 服务器
- 搭建带 OAuth 认证的远程 HTTP MCP 服务

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L10: Scaffold production-ready MCP servers in seconds.
> L63: Projects are generated against the MCP TypeScript SDK v2 — the split `@modelcontextprotocol/server`, `@modelcontext

## 星数曲线

```mermaid
xychart-beta
    title "agentailor/create-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `48d801368b61` · [字段定义](../../DATASET.md)*
