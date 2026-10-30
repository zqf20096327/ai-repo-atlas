# brightwave-inc/tidebreak

⭐ 32 · Rust · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/brightwave-inc/tidebreak) · [官网](https://www.tidebreak.io) · 组织维护

**本地优先桌面应用：在隔离 Git worktree 中运行 AI 编码代理**

Apache-2.0 的本地优先桌面工作台，以 Rust 编写，分 Code mode 与 Work mode：前者在独立 Git worktree 中运行 Claude Code、Codex CLI、opencode、Grok CLI，管理会话、diff、终端、浏览器测试、审查、PR 与 CI 修复；后者把文档转化为版本化的表格、演示、报告与应用。用户自带模型订阅或 API key（含 Ollama 本地端点），凭据存于系统凭证库，数据留在本地。当前为 pre-1.0，Windows/Linux 构建已暂停，部分能力仅限 macOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Code mode 在隔离 Git worktree 中运行 Claude Code / Codex CLI / opencode / Grok CLI
- Work mode 生成版本化交付物（表格、演示、报告、应用）并支持版本回溯与导出
- 支持本地 Ollama / OpenAI 兼容端点，可在对话中切换模型
- 提供桌面应用、headless 服务器、CLI、本地 HTTP/WebSocket API 与 MCP 服务面

## 适用场景

- 并行运行多个 AI 编码代理且不干扰我的工作副本
- 把代理产出走完审查、CI 修复到 PR 合并的完整流程
- 让代理基于我的文档生成交付物并保留版本历史

## 场景标签

`编码 Agent` `AI 写作` · 领域:编码与开发

## 证据(README 行号)

> L33: Tidebreak does not replace the coding agents or models you already use. It runs
> L34: Claude Code, Codex CLI, opencode, and Grok CLI inside durable workspaces, then
> L35: adds worktree isolation, agent control, diffs, terminals, browser testing,

## 星数曲线

```mermaid
xychart-beta
    title "brightwave-inc/tidebreak 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9363dc14916d` · [字段定义](../../DATASET.md)*
