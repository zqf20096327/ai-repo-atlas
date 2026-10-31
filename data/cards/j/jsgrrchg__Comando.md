# jsgrrchg/Comando

⭐ 14 · TypeScript · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/jsgrrchg/Comando) · 个人维护

**本地优先的多面板 AI agent 编码工作区（桌面应用）**

面向开发者的桌面工作区：将代码编辑、AI agent 会话、终端、Git 与审查视图放在同一多面板界面，项目以标签页组织，可并行运行 Codex、Claude、Grok、Kilo、OpenCode 等 agent 会话。提供 agent 改动的独立审查层（保留或拒绝文件与 hunk，独立于 Git 流程）、Monaco 编辑器（Vim 模式、Git gutters）、GitHub issue/PR/Actions 集成。首次运行需构建 Rust 原生后端，状态为实验性 pre-1.0，明确不含语言服务器、调试与扩展市场。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 并行运行 Codex/Claude/Grok/Kilo/OpenCode 会话，支持流式活动、权限确认与排队提示
- agent 改动的独立审查层，可按文件与 hunk 保留或拒绝
- Monaco 编辑器、原生终端、Git 分支/worktree 管理与 GitHub 集成一体化
- 本地优先，agent 历史与配置保存在本地

## 适用场景

- 在同一工作区内并行驱动多个 AI agent 做探索、实现与审查
- 在独立于 Git 的审查层中逐 hunk 审核 AI 生成的改动
- 将 GitHub issue/PR 附加到 prompt 中驱动 agent 工作

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L16: Comando is a desktop workspace for developers who want to work with multiple AI agents without turning their editor
> L20: - **Work with the agent you prefer.** Run Codex, Claude, Grok, Kilo, or OpenCode sessions with streaming activity, 

## 星数曲线

```mermaid
xychart-beta
    title "jsgrrchg/Comando 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `811e50e0f2dd` · [字段定义](../../DATASET.md)*
