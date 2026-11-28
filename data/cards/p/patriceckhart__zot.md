# patriceckhart/zot

⭐ 371 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/patriceckhart/zot) · [官网](https://zot.sh) · 个人维护

**Go 编写的轻量 coding agent 运行工具，对接 30+ 模型服务**

用 Go 编写的编码 agent 工具，编译为单一静态二进制。内置 30 多个模型服务的接入（API key、OAuth 订阅登录、自动刷新令牌）、读写/编辑/bash 等内置工具、三种运行模式（TUI/print/json）、Telegram bot，以及通过子进程 + JSON-RPC 的多语言扩展机制。支持 AGENTS.md 常驻指令与 SKILL.md 复用指令；`zot continuous run` 提供可崩溃恢复的持久化运行，后端可选本地 journal、SQLite 或外部 PostgreSQL。安装支持 curl 一键脚本、go install、源码构建与预编译包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 30+ 提供商接入，含 API key 与 OAuth 订阅登录及令牌自动刷新
- 单一静态二进制，三种运行模式（TUI/print/json）
- 持久化、崩溃可恢复的 continuous 运行，审批/预算/任务状态被保存
- 扩展通过子进程 + JSON-RPC 以任意语言编写，离线文档嵌入二进制

## 适用场景

- 在终端里通过 TUI 运行编码 agent 处理本地项目
- 接入 Anthropic/OpenAI 等多家模型服务做编码辅助
- 通过 Telegram bot 远程驱动编码任务
- 需要崩溃可恢复的长时 agent 运行（continuous 模式）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Yet another coding agent harness, lightweight and written (vibe-slopped) in go.
> L16: - built-in providers for Anthropic, OpenAI/Codex/Responses, Kimi, DeepSeek, Google Gemini/Vertex, GitHub Copilot, B
> L25: - durable, crash-recoverable runs in a persistent local store via `zot continuous run`, or hosted for multiple clie

## 星数曲线

```mermaid
xychart-beta
    title "patriceckhart/zot 星数(近 14 点)"
    x-axis ["2026-10-26", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-16", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-28"]
    y-axis "stars" 349 --> 374
    line [351, 353, 354, 353, 354, 351, 362, 367, 368, 370, 371, 372, 371, 371]
```

2026-10-26 351 → 2026-11-28 371（+20）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ceb2d044a5b9` · [字段定义](../../DATASET.md)*
