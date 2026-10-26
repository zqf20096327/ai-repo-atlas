# dcramer/dex

⭐ 386 · TypeScript · MIT · 推送 2026-03-02 · [GitHub](https://github.com/dcramer/dex) · [官网](https://dex.rip) · 个人维护

**给 AI agent 的结构化任务追踪工具，提供跨会话持久记忆**

面向 AI agent（Claude Code、OpenCode、Codex、Cursor 等）的任务追踪工具：任务以结构化形式记录描述、上下文与结果，支持 agent 拆解工作、追踪进度并在多会话间保留记录。存储采用 JSONL 格式（每行一个任务），便于协作、版本管理与合并。可通过 npm 全局安装，或用 npx skills add 为各 agent 安装技能；使用自然语言或斜杠命令操作。开发采用 pnpm 构建，支持作为 Claude 插件本地加载测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结构化任务记录：描述/上下文/结果三段式
- JSONL 存储（每行一任务），Git 友好、可版本化
- 跨会话持久记忆，支持 agent 拆解与追踪工作
- 为 Claude Code、OpenCode、Codex、Cursor 提供技能安装器

## 适用场景

- 让 AI agent 在多会话的长任务中保留进度与决策记录
- 以类 issue 的结构组织 agent 的工作项
- 将任务记录纳入 Git 版本管理便于协作

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Task tracking for AI agents. Persistent memory for complex, multi-session work.
> L13: **Built for agent coordination.** Agents break down work, track progress, and record results that persist across se
> L25: Or use the skills installer for your AI agent (Claude Code, OpenCode, Codex, Cursor):

## 星数曲线

```mermaid
xychart-beta
    title "dcramer/dex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 385 --> 387
    line [386, 386]
```

2026-10-18 386 → 2026-10-26 386（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4f278d64de9f` · [字段定义](../../DATASET.md)*
