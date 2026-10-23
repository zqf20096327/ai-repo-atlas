# madebyaris/native-cli-ai

⭐ 199 · Rust · 推送 2026-07-12 · [GitHub](https://github.com/madebyaris/native-cli-ai) · [官网](https://nca-cli.com) · 个人维护

**Rust 单二进制终端编码 agent：会话、子 agent 与编排一体**

Rust 编写的终端编码 agent，以单二进制分发，产品形态是 CLI/TUI（无桌面壳）。提供全屏 TUI、行式 REPL、一次性 run、detached 后台会话与 attach/status/logs，输出 JSON/NDJSON 并支持 Unix-socket IPC 供编排器驱动。支持派生子 agent（父子血缘、可选 git worktree 隔离）、MCP 工具加载、技能发现、会话持久化与长对话自动摘要。默认使用 MiniMax，可选 OpenAI、Anthropic、OpenRouter 与自定义端点，支持多模态图文输入。安装途径为一键脚本、GitHub Releases 预编译二进制或 cargo 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制 CLI，全屏 TUI / 行 REPL / 一次性 run / 后台 detached 会话
- 子 agent 派生：父子血缘与可选 git worktree 隔离
- JSON/NDJSON 输出与 Unix-socket IPC，可作被编排的 worker 进程
- 默认 MiniMax，支持 OpenAI/Anthropic/OpenRouter/自定义端点与 MCP 工具

## 适用场景

- 在终端里跑编码 agent，管理可恢复的会话与事件日志
- 派生隔离的子 agent 做多分支探索或后台分析
- 通过 JSON/NDJSON 与 IPC 把 agent 嵌入自动化编排流水线

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: `nca` is a Rust-native coding CLI that ships as a single binary. It is built for local-first, terminal-first workfl
> L39: - Uses MiniMax by default, with OpenAI, Anthropic, OpenRouter, and custom endpoint support.

## 星数曲线

```mermaid
xychart-beta
    title "madebyaris/native-cli-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 197 --> 200
    line [198, 199, 199]
```

2026-10-18 198 → 2026-10-23 199（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b16bd9edd777` · [字段定义](../../DATASET.md)*
