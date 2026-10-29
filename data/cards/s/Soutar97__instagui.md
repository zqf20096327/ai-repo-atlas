# Soutar97/instagui

⭐ 108 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Soutar97/instagui) · 个人维护

**把任意 CLI 一条命令变成本地 Web 表单的 AI 工具**

面向不常驻终端的开发者/用户：运行 npx instagui <tool>，读取工具的 --help 文本，用 AI 引擎（Anthropic/OpenAI/Gemini/DeepSeek/Ollama 或 claude/codex/gemini CLI，自动检测）解析为 JSON Schema，渲染为本地 Web 表单；点 Run 后以参数数组方式本地执行并流式返回输出，且始终预览将执行的完整命令。ffmpeg/yt-dlp/pandoc 等 8 个工具内置 Schema，无需 API key；其他工具首次提取需可用引擎，之后缓存。仅绑定 127.0.0.1，单用户，不支持交互式 TUI 程序与子命令树。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 --help 并用 AI 提取为结构化 Schema，渲染成 Web 表单
- 8 个常用工具（ffmpeg/yt-dlp/pandoc 等）内置 Schema，无需 API key
- 多 AI 引擎自动检测：API key 优先于已登录 CLI（claude/codex/gemini），支持本地 Ollama
- 命令以参数数组 spawn 执行、仅绑定 127.0.0.1、CSRF 防护与同源校验

## 适用场景

- 不熟悉终端时通过表单使用 ffmpeg/pandoc 等命令行工具
- 忘记 flag 语法时借助表单与实时命令预览学习 CLI
- 通过 SSH 端口转发在远程服务器上以表单操作 CLI

## 场景标签

 · 领域:开发者工具/CLI 易用化

## 证据(README 行号)

> L24: parses the tool's own `--help` text with AI into a structured schema and renders that as a form.
> L122: 2. **Extract** — send the help text to the Claude API (`claude-haiku-4-5`) and get back a validated

## 星数曲线

```mermaid
xychart-beta
    title "Soutar97/instagui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 106 --> 109
    line [107, 108, 108]
```

2026-10-18 107 → 2026-10-29 108（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `12edfc0a34bf` · [字段定义](../../DATASET.md)*
