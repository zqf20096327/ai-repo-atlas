# vcaesar/codg

⭐ 42 · Go · 推送 2026-10-27 · [GitHub](https://github.com/vcaesar/codg) · [官网](https://atomai.cc) · 个人维护 · 中文 README

**终端 AI 编码/工作 Agent 运行时（CLI/TUI/Web/桌面）**

用 Go 编写的 AI agent harness 系统，提供 CLI、TUI、Web UI（端口 4096）与 Wails 桌面端四种使用形态：在项目目录运行 codg 后通过 "/xxx" 命令或点击操作管理会话、查看 diff、切换权限模式（auto/ask）。支持多模型接入：100+ API 与 Pro 提供商、OpenAI/Claude 兼容自定义接口、llama.cpp 本地模型、Ollama/OpenRouter 等，并有 Agent 团队、Skills、MCP、插件市场（兼容 Claude Code/Codex 插件）、语音输入（whisper.cpp/funasr/qwen3-asr）与 Telegram 等消息渠道。通过 codg.toml 配置提供商、Agent、MCP、权限等。面向在终端中使用 AI agent 完成编码与自动化任务的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- CLI/TUI/Web UI/桌面四种运行形态，任意终端与操作系统支持
- 100+ 模型提供商接入，含 OpenAI/Claude 兼容自定义 API 与本地模型
- Agent 团队、Skills、MCP、插件市场与 Claude Code/Codex 插件兼容
- 上下文压缩与缓存以降低 token 消耗（README 称节省 70%-90%+）
- 本地语音引擎（whisper.cpp/funasr/qwen3-asr）通过 "/run install" 安装

## 适用场景

- 在终端里用多 agent 完成编码、调试与自动化任务
- 接入自选模型提供商或本地模型做代码助手
- 通过 Web UI 或 Telegram 渠道远程操作 agent

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: The next easy code and work AI agents harness system, auto and asynchronous, concurrency and high performance, Effic
> L52: - Auto and asynchronous, concurrency and high performance agents system, low memory and cpu, lessest tokens use (sa
> L53: - Multi models providers (100+ API and Pro providers, Custom URL API) and local models via by openai-compat or clau

## 星数曲线

```mermaid
xychart-beta
    title "vcaesar/codg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a1b225c3acc4` · [字段定义](../../DATASET.md)*
