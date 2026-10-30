# talos-hq/clud

⭐ 16 · Rust · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/talos-hq/clud) · [官网](https://talos-hq.github.io/clud/) · 组织维护

**在 Claude Code 终端内运行 Codex/DeepSeek 的 CLI 代理运行器**

Rust 编写的命令行工具，把 Codex、DeepSeek、Kimi、OpenRouter 等后端接入 Claude Code 终端运行：`--codex`/`--deepseek` 等切换后端，`clud do` 可从 GitHub issue 一路生成合并 PR，`clud grind` 批量处理 issue 列表。支持启动本地 Anthropic 兼容 API 网关、stdio MCP 服务器供 Hermes Agent 发现、PTY 图形头与守护进程会话。安装通过 install 脚本或 uv/pipx/pip 完成，依赖 uv 与 PATH 上的 Claude Code 可执行文件。限制：仅支持 Codex 后端配 Claude harness（反向拒绝），部分功能标注实验性（如 ChatGPT 订阅登录）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 在 Claude Code harness 内运行 Codex、DeepSeek、Kimi、OpenRouter 后端
- `clud do` 从单个 issue 到合并 PR 的端到端流程，`clud grind` 批量处理 issue 列表
- 本地 Anthropic Messages 兼容 API 网关（`clud serve`）与 stdio MCP 服务器
- PTY/Sixel 图形头、守护进程后台会话与 resume 会话管理

## 适用场景

- 在 Claude Code 终端里直接用 Codex 或 DeepSeek 模型干活
- 让 agent 自动解决 GitHub issue 并产出合并 PR
- 把本地 agent 会话以 Anthropic 兼容 API 暴露给其他客户端

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A luxury agentic experience with Claude, Codex and DeepSeek, by running them all on Claude Code.**
> L170: `clud serve --claude` or `clud serve --codex` exposes a local
> L171: Anthropic-compatible API for other clients.

## 星数曲线

```mermaid
xychart-beta
    title "talos-hq/clud 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-26 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `def0337a99c3` · [字段定义](../../DATASET.md)*
