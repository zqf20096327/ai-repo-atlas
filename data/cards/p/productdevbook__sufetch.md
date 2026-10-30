# productdevbook/sufetch

⭐ 19 · TypeScript · MIT · 推送 2025-11-04 · [GitHub](https://github.com/productdevbook/sufetch) · 组织维护

**从 OpenAPI 规范生成 TypeScript 类型安全客户端，并附 MCP 服务器**

由 productdevbook 团队维护的 TypeScript 库，结合两部分能力：从 OpenAPI 规范生成全类型 API 客户端（内置 DigitalOcean、Hetzner Cloud、Ory Kratos/Hydra 等服务），以及一个 MCP 服务器，让 Claude 等 AI 助手浏览端点、查询 schema 并生成代码。基于 apiful 构建，支持类型提取工具按请求/响应/参数提取类型。通过 npm 安装客户端，或全局安装/npx 运行 MCP 服务器。用户可自行添加 OpenAPI 规范扩展新 API。

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

- 从 OpenAPI 规范生成全类型 TypeScript 客户端，内置 4 类服务的 API（200+/100+/50+/40+ 端点）
- MCP 服务器提供 7 个工具：列出 API、搜索端点、获取 schema、生成代码示例等
- 类型助手可提取请求体/响应/查询/路径参数类型
- 可添加自有 OpenAPI 规范扩展新 API

## 适用场景

- 在 TypeScript 项目中以类型安全方式调用云平台 API
- 让 AI 助手通过 MCP 浏览并生成指定 API 的调用代码
- 将自有服务的 OpenAPI 规范接入供 AI 助手查询

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L19: 1. **Type-Safe API Clients** - Generate fully-typed TypeScript clients from OpenAPI specifications
> L20: 2. **MCP Server** - Let AI assistants (like Claude) explore your APIs and generate code

## 星数曲线

```mermaid
xychart-beta
    title "productdevbook/sufetch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7b46e405db74` · [字段定义](../../DATASET.md)*
