# rblalock/omakaseagent

⭐ 20 · JavaScript · NOASSERTION · 推送 2026-08-26 · [GitHub](https://github.com/rblalock/omakaseagent) · [官网](https://omakaseagent.com) · 个人维护

**给 AI 编程 agent 的工作质量标准：十二条规则+评审门+项目记忆**

面向 Claude Code、Cursor、Codex、Grok 等编程 agent 的可移植质量标准包：通过 npx 命令安装十二条不可协商规则（OMAKASE-RULES.md）、重大产出评审量表（OMAKASE-CRITIQUE.md）与项目记忆（.omakaseagent/taste.md、decisions.md）。提供 engineer/critic/archivist 三个 lead agent 与 router 技能，agent 产出重大工作前先过评审门。以 npm 包分发，init 可重复运行且不覆盖既有记忆文件。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十二条规则 + 评审量表 + 项目记忆（taste.md/decisions.md）构成的质量标准
- 三个 lead agent（engineer/critic/archivist）与 router 技能
- 一条 npx 命令自动检测并安装到多种 agent 框架（cursor/claude/agents/grok/codex）
- init 可重复刷新，不覆盖已存在的项目记忆文件

## 适用场景

- 为我的 Claude Code/Cursor 项目统一 agent 编码质量标准
- 在重大改动合入前对 agent 产出执行评审门检查
- 跨项目沉淀技术偏好与决策记忆供 agent 沿用

## 场景标签

`Agent 记忆` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: Omakase is a **portable quality standard** for agent work: twelve rules, a critique rubric, and project memory (`.o
> L21: Paste this into your agent (Claude Code, Cursor, wherever it lives) — the setup is agentic, not a script:
> L67: npx omakaseagent init

## 星数曲线

```mermaid
xychart-beta
    title "rblalock/omakaseagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dd073e76d38a` · [字段定义](../../DATASET.md)*
