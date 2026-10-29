# verrysimatupang99/codex-dev-mcp-suite

⭐ 96 · JavaScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/verrysimatupang99/codex-dev-mcp-suite) · 个人维护

**面向独立开发者的四个本地 MCP 服务器：持久记忆、会话交接、检查点、项目简报**

npm 发布的 MCP 服务器套件，含四个组件：project-memory（Obsidian 兼容 Markdown 知识库、wiki 链接、本地 384 维向量搜索）、devjournal（会话日志与压缩交接，宣称压缩 token 约 90%）、checkpoint（不依赖 git 的文件快照与回滚）、context-pack（token 高效项目简报、依赖影响分析、安全审计）。数据全部以本地 Markdown/JSON 存储，零遥测，支持离线模式。适用于 Codex CLI、Claude Code、Cursor、Windsurf 等 MCP 客户端，面向独立开发者与 vibe coder。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个 MCP 服务器：持久记忆、会话交接、git 无关检查点、项目简报
- 本地零依赖 384 维向量搜索，可选 OpenAI 兼容嵌入端点
- 本地 Markdown/JSON 存储，零遥测，支持完全离线（MCP_DETERMINISTIC_FALLBACK）
- 单条 npx 命令自动配置多个已安装 AI 工具

## 适用场景

- AI 编码助手跨会话保留项目上下文与架构决策
- 上下文压缩或会话重启后快速恢复工作状态
- AI 重构前做文件快照以便即时回滚

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: **Dev MCP Suite** is a suite of four local, zero-telemetry MCP (Model Context Protocol) servers built for solo deve
> L46: ### 🛠️ The 4 Superpowers (MCP Servers)

## 星数曲线

```mermaid
xychart-beta
    title "verrysimatupang99/codex-dev-mcp-suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 95 --> 97
    line [96, 96]
```

2026-10-18 96 → 2026-10-29 96（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7cf0173395bd` · [字段定义](../../DATASET.md)*
