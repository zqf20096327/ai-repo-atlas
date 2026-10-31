# fourdollars/rune

⭐ 15 · Rust · MIT · 推送 2026-10-30 · [GitHub](https://github.com/fourdollars/rune) · [官网](https://fourdollars.github.io/rune/) · 个人维护

**Rust 单二进制 AI agent：CLI 助手、Concourse CI 资源与 Markdown 交换中心**

用 Rust 编写的单一二进制程序，以三种模式运行：交互式 CLI AI 助手、Concourse CI 资源类型（check/in/out）、以及名为 Rune Notes 的 Markdown 数据交换中心（Web UI + MCP 端点 + REST API）。工具执行经过最多 5 层隔离（cgroups v2、网络命名空间/net-guard、Seccomp、Landlock、域名白名单），命令策略分 allowlist/confirm/unrestricted 三档。支持 GitHub Copilot、OpenRouter、Gemini、OpenAI 兼容与 Ollama 等提供方，内置 9 个工具、MCP 客户端/服务器、流式输出、并行工具调用，并可编译内嵌 Vim/Neovim 插件。限制：零信任沙箱为 best-effort，依赖运行环境可用性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一二进制三模式：CLI 助手 / Concourse CI 资源 / Rune Notes 服务
- 工具执行经 5 层隔离（cgroups/网络/seccomp/Landlock/域名白名单）
- 内置 MCP 客户端与 HTTP MCP 服务器端点
- 内嵌零依赖 Vim/Neovim 插件（FIM 补全与 :RuneAsk 等命令）

## 适用场景

- 在终端用自然语言驱动沙箱化的 AI 助手执行任务
- 在 Concourse CI 流水线中以资源类型调用 AI agent
- 以 Markdown 文件为唯一事实源，连接外部 agent 与浏览器扩展做笔记同步

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L3: A high-performance, zero-trust AI agent built in Rust. Single binary, triple mode: interactive CLI assistant, Concou
> L13: - **Tool Calling** — 9 built-in tools (5 standard sandboxed tools + 4 serve-mode notes tools): `read_file`, `write_
> L14: - **Rune Notes (Data Exchange Hub)** — AI-native Markdown hub served from the same single binary. Exposes Web UI, M

## 星数曲线

```mermaid
xychart-beta
    title "fourdollars/rune 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6015433efeb5` · [字段定义](../../DATASET.md)*
