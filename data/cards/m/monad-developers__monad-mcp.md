# monad-developers/monad-mcp

⭐ 13 · TypeScript · MIT · 推送 2025-12-16 · [GitHub](https://github.com/monad-developers/monad-mcp) · [官网](https://docs.monad.xyz/guides/monad-mcp) · 组织维护

**基于 Next.js 的 MCP server 模板，用于连接 Monad**

一个用 Next.js 实现的 MCP server 示例工程：开发者编辑 app/mcp.ts 定义 tools、prompts 和 resources（遵循 MCP TypeScript SDK 文档）。支持部署到 Vercel，需附加 Redis（REDIS_URL）并启用 Fluid compute；Pro/Enterprise 账户可将 SSE 路由 max duration 调至 800。附带脚本 scripts/test-client.mjs 用于测试调用。README 未提供安装命令，主要面向熟悉 Next.js 部署流程的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Next.js 的 MCP TypeScript SDK server 模板
- 支持部署到 Vercel（需 Redis 与 Fluid compute）
- 附带示例客户端脚本 test-client.mjs 测试调用

## 适用场景

- 为 Monad 区块链交互搭建 MCP 工具服务
- 作为 Next.js 版 MCP server 的开发起点
- 在 Vercel 上托管 MCP server 并测试调用

## 场景标签

 · 领域:区块链/开发工具

## 证据(README 行号)

> L1: # Example MCP Server built on Next.js
> L5: Update `app/mcp.ts` with your tools, prompts, and resources following the MCP TypeScript SDK documentation.

## 星数曲线

```mermaid
xychart-beta
    title "monad-developers/monad-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `39400ec00216` · [字段定义](../../DATASET.md)*
