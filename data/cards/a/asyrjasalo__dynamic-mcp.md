# asyrjasalo/dynamic-mcp

⭐ 13 · Rust · MIT · 推送 2026-03-26 · [GitHub](https://github.com/asyrjasalo/dynamic-mcp) · [官网](https://pypi.org/project/dmcp) · 个人维护

**MCP 代理服务器：按需加载多上游 MCP 工具，降低 LLM 上下文占用**

面向使用 MCP（Model Context Protocol）的开发者的代理服务器：将多个上游 MCP 服务器的工具分组，初始只暴露两个 MCP 工具，按需加载工具 schema，以减少一次性暴露全部服务器造成的数千 token 上下文消耗。支持 stdio/HTTP/SSE 传输、OAuth 认证与令牌自动刷新、失败连接自动重试、按服务器粒度的功能开关（tools/resources/prompts）、超时配置与启用/禁用。提供 PyPI 包（uvx）、预编译二进制与 cargo 源码安装三种途径，并可从 Cursor、Claude Code、VS Code 等 10 种 AI 编码工具导入既有 MCP 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 初始仅暴露两个工具，按需加载上游工具 schema 以降低 token 占用
- 支持 stdio/HTTP/SSE 传输与 OAuth 认证（含令牌自动刷新）
- 按服务器粒度的功能开关、超时配置与启用/禁用
- 可从 Cursor、Claude Code、VS Code 等 10 种 AI 编码工具导入 MCP 配置

## 适用场景

- 接入大量 MCP 服务器时降低 LLM 上下文的工具定义开销
- 把 Cursor/Claude Code 等工具的既有 MCP 配置迁移为按需加载模式
- 统一代理多个 stdio/HTTP/SSE 上游 MCP 服务器并管理认证

## 场景标签

 · 领域:LLM 基础设施/MCP 工具

## 证据(README 行号)

> L3: MCP proxy server that reduces LLM context overhead by grouping tools from multiple upstream MCP servers and loading 
> L5: Instead of requiring you to expose all MCP servers upfront (which can consume thousands of tokens), dynamic-mcp expo

## 星数曲线

```mermaid
xychart-beta
    title "asyrjasalo/dynamic-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e83a731e12a6` · [字段定义](../../DATASET.md)*
