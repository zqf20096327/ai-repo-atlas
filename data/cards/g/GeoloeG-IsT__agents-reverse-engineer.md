# GeoloeG-IsT/agents-reverse-engineer

⭐ 22 · TypeScript · MIT · 推送 2026-09-12 · [GitHub](https://github.com/GeoloeG-IsT/agents-reverse-engineer) · 个人维护

**为 AI 编码助手生成代码库文档的工具（AGENTS.md/.sum）**

面向使用 AI 编码助手的开发者：通过 npx 交互式安装器向 Claude Code、Codex、OpenCode、Gemini CLI 注入 /are-* 命令，扫描代码库（遵循 .gitignore、后序遍历）生成每文件 .sum 摘要、每目录 AGENTS.md 及运行时指针文件（CLAUDE.md 等）。基于 Git 变更检测做增量更新，仅重生成改动文件。另含实验性功能：项目规格合成、带/不带文档的 A/B 计划与实现对比、成本与 token 遥测面板。要求 Node.js 18+ 与一个 AI 编码助手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 生成 .sum 文件、每目录 AGENTS.md 与运行时指针文件（CLAUDE.md/GEMINI.md 等）
- Git 感知的增量更新，仅重生成改动文件的文档
- 支持 Claude Code、Codex、OpenCode、Gemini CLI 四种运行时
- 实验性：计划/实现的 A/B 对比、规格合成与遥测面板（成本/token/追踪）

## 适用场景

- 让 Claude Code 等 AI 助手首次会话即了解大型项目的结构与模式
- 代码库演进过程中自动保持 AI 上下文文档同步
- 对比有/无项目文档时 AI 计划与实现质量的差异

## 场景标签

 · 领域:开发者工具/AI 辅助编程

## 证据(README 行号)

> L5: **Generate `.sum` files and `AGENTS.md` for Claude Code, OpenCode, and any AI assistant that supports `AGENTS.md`.**
> L37: **agents-reverse-engineer** fixes that. It generates rich, multi-level documentation that AI assistants actually re
> L48: Developers using AI coding assistants (Claude Code, Codex, OpenCode, Gemini CLI, or any tool supporting `AGENTS.md`

## 星数曲线

```mermaid
xychart-beta
    title "GeoloeG-IsT/agents-reverse-engineer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3d0bb4f7d5bd` · [字段定义](../../DATASET.md)*
