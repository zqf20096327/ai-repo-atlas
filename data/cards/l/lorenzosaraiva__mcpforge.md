# lorenzosaraiva/mcpforge

⭐ 18 · TypeScript · 推送 2026-10-30 · [GitHub](https://github.com/lorenzosaraiva/mcpforge) · 个人维护

**从 OpenAPI 规格或文档页生成并验证 MCP 服务器的 CLI 工具**

面向需要把 REST API 接入模型上下文协议（MCP）的开发者的 npm 命令行工具：解析 OpenAPI 3.0/3.1 与 Swagger 2.0 规格，或从文档页推断 API 形态，生成含 OAuth 鉴权脚手架的 TypeScript MCP 服务器。提供 Claude 驱动的端点精选（--optimize，严格模式默认 ≤25 个工具）与面向任务的工作流工具规划（--workflows）。生成后可通过 mcpforge test 对本地 mock 上游验证请求兼容性，diff/update 跟踪上游规格漂移，并配套社区注册表用于搜索、安装与发布。优化功能需要 ANTHROPIC_API_KEY，缺失时跳过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 OpenAPI 3.0/3.1 与 Swagger 2.0 规格，或从文档 URL 推断 API 形态
- 生成含 OAuth token 生命周期处理的 TypeScript MCP 服务器
- diff/update 检测上游规格漂移并报告工作流影响
- mcpforge test 通过本地 mock 上游验证生成服务器的请求兼容性

## 适用场景

- 把已有 REST API 封装成 LLM 可调用的 MCP 工具集
- 从注册表一键安装社区精选的 MCP 服务器（如 Stripe）
- API 规格变更后检测对已生成 MCP 服务器的影响并重新生成

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: Generate MCP servers from OpenAPI specs or docs pages, then verify generated request compatibility before you publis
> L77: - Generates a complete TypeScript MCP server with auth scaffolding and docs

## 星数曲线

```mermaid
xychart-beta
    title "lorenzosaraiva/mcpforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b2209be3f9a6` · [字段定义](../../DATASET.md)*
