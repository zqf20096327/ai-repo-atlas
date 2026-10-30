# Markgatcha/universal-mcp-toolkit

⭐ 15 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/Markgatcha/universal-mcp-toolkit) · [官网](https://context-core.dev/umt/) · 个人维护 · 中文 README

**为 AI agent 提供 31 个生产级 MCP 服务器的 monorepo 与统一 CLI**

以 Turborepo 组织的 MCP 服务器集合与配套工具链：内置 GitHub、Slack、Notion、PostgreSQL、Stripe 等 31 个服务器，共享 strict-mode TypeScript 核心运行时（Zod 校验、pino 日志、stdio 与 HTTP+SSE 传输）。统一 CLI `umt` 支持安装、配置生成、运行、工具发现、工作流执行与诊断（doctor），并提供 TTL+LRU 缓存、懒加载工具注册、熔断器与 Token 预算管理等机制。面向需要为 Claude Desktop、Cursor 等 MCP 客户端配置服务器的开发者；每个服务器按环境变量配置所需凭证。

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

- 31 个生产级 MCP 服务器（GitHub/Slack/Notion/PostgreSQL/Stripe 等）
- `umt` CLI 提供 list/config/install/run/tools/workflow/discover/doctor 命令
- TTL+LRU 结果缓存、懒加载工具注册、熔断器与 Token 预算管理
- MCP Registry 兼容的远程服务发现与 `.well-known/mcp-server.json` 服务卡片

## 适用场景

- 为 Claude Desktop / Cursor 等 MCP 客户端一站式配置多台服务器
- 跨多个 MCP 服务器发现并调用工具、编排版本化 JSON 工作流
- 作为 MCP monorepo 的参考实现学习架构并扩展自定义服务器

## 场景标签

 · 领域:AI 开发者工具/MCP 生态

## 证据(README 行号)

> L63: `universal-mcp-toolkit` fixes that with one opinionated, high-quality Turborepo:
> L98: |Unified CLI|`universal-mcp-toolkit` with `list`, `config`, `install`, `run`, `tools list`, `workflow`, `compose`, 

## 星数曲线

```mermaid
xychart-beta
    title "Markgatcha/universal-mcp-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a638e4d9a135` · [字段定义](../../DATASET.md)*
