# crossoverJie/SkillDeck

⭐ 652 · Swift · MIT · 推送 2026-11-14 · [GitHub](https://github.com/crossoverJie/SkillDeck) · [官网](http://crossoverjie.top/SkillDeck/) · 个人维护 · 中文 README

**macOS 桌面 GUI：统一管理多个 AI 编码 Agent 的技能**

面向 macOS 的原生 SwiftUI 应用，集中管理分布在多个 AI 编码 Agent（Claude Code、Codex、Gemini CLI、Cursor 等 15 个）技能目录中的 skills。核心机制：以文件系统为数据库（SKILL.md 目录），通过 symlink 与 lock file 管理技能在各 Agent 间的安装分配；提供 skills.sh 与 ClawHub 注册表浏览、调用次数统计、SKILL.md 编辑器、一键更新检查，并内置 skilldeck 技能支持自然语言管理。要求 macOS 14+，提供通用二进制、Homebrew 与源码构建三种安装方式，界面支持英文与简体中文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨 15 个 AI 编码 Agent 的技能统一管理与 Agent 分配（symlink）
- skills.sh 排行榜与 ClawHub 目录浏览，支持搜索/排序/过滤
- 按技能跟踪 Codex、Claude Code、Copilot CLI 中的调用次数
- 内置 skilldeck 技能，可在任意 Agent 中用自然语言管理技能

## 适用场景

- 我同时用多个 AI 编码 Agent，想在一处管理所有技能
- 清理不再使用的技能，按调用统计排序
- 从 GitHub 或本地文件夹导入技能并分配给指定 Agent
- 用可视化编辑器修改 SKILL.md 并实时预览

## 场景标签

 · 领域:开发者工具/AI Agent 生态管理

## 证据(README 行号)

> L5:  The desktop GUI for managing AI code agent skills on macOS.
> L24: - **Multi-Agent Support** — Claude Code, Codex, Copilot CLI, OpenCode, Pi, Cursor, Kiro, CodeBuddy, Trae, Qoder, QC
> L101: MVVM with `@Observable` (macOS 14+). The filesystem is the database — skills are directories containing `SKILL.md`

## 星数曲线

```mermaid
xychart-beta
    title "crossoverJie/SkillDeck 星数(近 18 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-24"]
    y-axis "stars" 577 --> 658
    line [583, 584, 586, 587, 589, 590, 591, 592, 587, 592, 621, 638, 640, 642, 643, 651, 652, 652]
```

2026-10-22 583 → 2026-11-24 652（+69）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `db42463f5606` · [字段定义](../../DATASET.md)*
