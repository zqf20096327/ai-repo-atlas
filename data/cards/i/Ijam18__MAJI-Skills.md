# Ijam18/MAJI-Skills

⭐ 19 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/Ijam18/MAJI-Skills) · 个人维护

**面向编码 agent 的 SKILL.md 技能集：纪律与日常工作流**

一组以纯 SKILL.md 文件形式组织的 agent 技能，覆盖工作纪律（maji-mode/maji-jimat）、初始化配置（maji-setup）、提交/调试/评审/测试等代码工作流。兼容 Claude Code、Cursor、Antigravity、Codex 与 Gemini CLI，各工具通过 AGENTS.md 或链接目录自动发现技能。个人上下文存于 me/ 文件夹且被 gitignore，更新不冲突。基于 29,582 条 Claude Code 消息测量 token 影响（均值 −18.2%）。仓库内容全部免费，另有独立收费的 MAJI Skills Pro。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SKILL.md 纯文件技能，兼容 Claude Code/Cursor/Antigravity/Codex/Gemini CLI
- 个人配置存于 me/ 目录并 gitignore，git pull 更新不冲突
- 基于 29,582 条消息的实测 token 影响（均值 −18.2%，P90 −28.3%）
- 技能分稳定层与实验层（experimental），迁移规则见 docs/TIERS.md

## 适用场景

- 给编码 agent 装一套提交、评审、调试、测试的固定工作流
- 通过 maji-setup 让 agent 记住我的技术栈、语言风格与工具偏好
- 在多个 agent 工具间共享同一套技能和个人配置

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A working discipline and everyday code skills, distilled from real, repeated work. Every skill is a plain `SKILL.md`
> L19: 1. Open `my-agent` in your agent (Claude Code, Cursor, Antigravity, Codex or Gemini CLI). It reads `AGENTS.md` and 
> L62: |Agent|Reads the hub|Finds skills in|

## 星数曲线

```mermaid
xychart-beta
    title "Ijam18/MAJI-Skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `db0c963f1618` · [字段定义](../../DATASET.md)*
