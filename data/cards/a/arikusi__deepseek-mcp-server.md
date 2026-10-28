# arikusi/deepseek-mcp-server

⭐ 26 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/arikusi/deepseek-mcp-server) · [官网](https://mcp.tahirl.com) · 个人维护

**面向 MCP 客户端的 DeepSeek 模型接入服务器**

以 TypeScript 实现的 MCP server，把 DeepSeek V4.1（deepseek-flash、deepseek-v4-pro，1M 上下文）封装为 deepseek_chat、deepseek_fim、deepseek_sessions 三个工具与 3 个只读 MCP 资源，供 Claude Code、Gemini CLI、Cursor、Windsurf 等 MCP 兼容客户端调用。功能包括多轮会话（session_id）、函数调用（最多 128 个工具定义）、思维链模式、JSON 输出与 schema 校验（含修复重试与 ReDoS 防护）、峰值感知成本追踪、模型回退与熔断。提供托管端点（BYOK）、npx 本地 stdio、Docker 多阶段构建三种运行方式；需 Node.js 22+ 与 DeepSeek API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- deepseek_chat / deepseek_fim / deepseek_sessions 三个工具，支持多轮会话与函数调用
- schema 校验 JSON 输出：修复重试（默认 2 次）与 ReDoS 模式防护
- 缓存感知成本追踪，按峰值/谷值费率计价
- 托管端点 BYOK、npx stdio、Docker 三种部署方式

## 适用场景

- 在 Claude Code / Gemini CLI 等客户端中直接调用 DeepSeek 模型
- 为编辑器 agent 配置带成本统计的 DeepSeek 后端
- 通过 FIM 工具做代码补全（前缀+后缀填中间）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5:  MCP server for DeepSeek (deepseek-flash and deepseek-v4-pro, 1M context) with multi-turn sessions, function calling
> L15:  Compatible with Claude Code, Gemini CLI, Cursor, Windsurf, and any MCP-compatible client.
> L52: claude mcp add -s user deepseek npx @arikusi/deepseek-mcp-server -e DEEPSEEK_API_KEY=your-key-here

## 星数曲线

```mermaid
xychart-beta
    title "arikusi/deepseek-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `26bb4103e540` · [字段定义](../../DATASET.md)*
