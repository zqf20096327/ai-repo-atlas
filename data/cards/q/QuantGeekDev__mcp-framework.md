# QuantGeekDev/mcp-framework

⭐ 931 · TypeScript · MIT · 推送 2026-04-16 · [GitHub](https://github.com/QuantGeekDev/mcp-framework) · [官网](https://mcp-framework.com/) · 个人维护

**用 TypeScript 构建 MCP 服务器的开发框架**

面向 TypeScript 开发者的 Model Context Protocol 服务器构建框架：基于官方 MCP SDK，提供目录式自动发现与加载 tools/resources/prompts、基类抽象、CLI 脚手架（mcp create/add/validate）。支持 stdio/SSE/HTTP Stream 三种传输，HTTP Stream 提供 batch 与 stream 两种响应模式及会话管理、流恢复。SSE/HTTP 端点可选 JWT、API Key、OAuth 2.1 认证。工具 schema 基于 Zod，在构建期、开发期、独立与运行时四级校验字段描述。通过 npm 安装，文档含 Claude Desktop 接入配置示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 目录式自动发现加载 tools/resources/prompts
- stdio/SSE/HTTP Stream 多传输支持，HTTP Stream 含会话管理与流恢复
- OAuth 2.1（RFC 9728/JWKS/Token Introspection）、JWT、API Key 可选认证
- Zod schema 定义工具输入，构建/开发/运行时四级描述校验

## 适用场景

- 用 TypeScript 快速搭建带类型安全的 MCP 服务器
- 为 Claude Desktop 等 MCP 客户端提供自定义工具服务
- 通过 CLI 生成项目骨架并逐步添加 tool/prompt/resource

## 场景标签

 · 领域:LLM 基础设施/MCP 开发框架

## 证据(README 行号)

> L3: MCP-Framework is a framework for building Model Context Protocol (MCP) servers elegantly in TypeScript.
> L12: - Built on the official MCP SDK

## 星数曲线

```mermaid
xychart-beta
    title "QuantGeekDev/mcp-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 930 --> 932
    line [931, 931]
```

2026-10-18 931 → 2026-10-28 931（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `874bded6d565` · [字段定义](../../DATASET.md)*
