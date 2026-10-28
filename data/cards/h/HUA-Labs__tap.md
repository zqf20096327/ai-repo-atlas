# HUA-Labs/tap

⭐ 39 · TypeScript · 推送 2026-06-20 · [GitHub](https://github.com/HUA-Labs/tap) · 组织维护

**跨厂商 AI agent 互通 CLI：Claude/Codex 经文件目录互发消息**

面向 AI 操作者的轻量 npm CLI，让 Claude、Codex 等多个 agent 运行时通过共享的文件型通信目录交换消息，无需中心守护进程。提供 dry-run 优先的 setup、runtime 添加、ready/comms-doctor/flow-doctor 等诊断命令、MCP 服务器（serve）与 Codex app-server bridge 管理。0.6.x 为高级操作者预览版：Gemini CLI 支持标记为 legacy/deprecated，Antigravity 需以自定义 profile pack 建模。要求 Node.js ≥22.6.0 且在 git 仓库内运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文件型通信目录承载收件箱、评审、交接与证据
- dry-run 优先的 setup 与 guarded MCP 配置管理
- comms-doctor/flow-doctor 按运行时表面诊断投递
- 内置 stdio MCP 服务器与 Codex app-server bridge 生命周期管理

## 适用场景

- 让 Claude 与 Codex 等 CLI agent 在同一仓库内互相传递消息
- 诊断跨 agent 投递链路与 MCP 配置漂移
- 为多 agent 协作记录可发现的评审证据流

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: `@hua-labs/tap` is a lightweight CLI that lets multiple AI agent runtimes, such
> L203: - **Runtime**: an AI tool or environment tap can connect to, such as Claude or
> L242: |Claude|supported|Uses `.mcp.json` / channel-style delivery.|

## 星数曲线

```mermaid
xychart-beta
    title "HUA-Labs/tap 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `29501b2b5466` · [字段定义](../../DATASET.md)*
