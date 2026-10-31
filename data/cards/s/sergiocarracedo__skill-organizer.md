# sergiocarracedo/skill-organizer

⭐ 15 · Go · 推送 2026-06-15 · [GitHub](https://github.com/sergiocarracedo/skill-organizer) · [官网](https://skill-organizer.sergiocarracedo.es/) · 个人维护

**CLI 工具：把嵌套组织的 agent 技能目录同步为扁平符号链接**

面向使用 SKILL.md 技能的 agent 工具（Claude Code、Codex、Antigravity 等）的命令行工具：以嵌套的 skills-organized 源目录为唯一编辑入口，生成 agent 工具所需的扁平一级技能目录（符号链接，路径 / 替换为 --）。提供 sync/status 同步与漂移检测、经 skills.sh 导入第三方技能并跟踪上游更新、技能启用/禁用、基于外部 agent CLI 的技能重叠分析、后台 watch 服务与 shell 补全。通过 npm、homebrew 或 GitHub Releases 二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 嵌套源树生成扁平符号链接目标目录（如 .claude/skills/）
- 经 skills.sh 导入技能并跟踪上游更新，备份保留 10 天
- 调用已安装 agent CLI 分析技能重叠/重复（0-100 重叠分）
- onboard 交互式初始化，支持 Claude Code、Codex、Antigravity 等

## 适用场景

- 按来源或主题分组管理大量 agent 技能而不手动复制目录
- 从 GitHub 仓库导入技能并检查上游更新
- 找出技能集中重复或部分重叠的技能

## 场景标签

 · 领域:开发工具/agent 基础设施

## 证据(README 行号)

> L5: `skill-organizer` lets you keep `SKILL.md` directories organized in nested folders while exposing the flat first-lev
> L7: It uses an organized source tree such as `skills-organized/` as the source of truth and generates a flat target fold
> L90: - Any directory containing `SKILL.md` is treated as a skill.

## 星数曲线

```mermaid
xychart-beta
    title "sergiocarracedo/skill-organizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `99c5dd727499` · [字段定义](../../DATASET.md)*
