# shinerio/SkillFlow

⭐ 24 · Go · MIT · 推送 2026-08-31 · [GitHub](https://github.com/shinerio/SkillFlow) · 个人维护 · 中文 README

**跨平台桌面应用：统一管理并同步技能、提示词与记忆到多个 AI agent**

面向使用多种 AI coding agent 的开发者的桌面应用：本地维护技能库、提示词库与记忆库三类资产，通过内置适配器（Claude Code、OpenCode、Codex、Gemini CLI、OpenClaw）及自定义 agent 将选定的技能与记忆同步到各环境，支持合并/接管两种记忆同步模式。另提供 Git 仓库来源跟踪与技能更新检查、对象存储或 Git 云备份，以及双语 UI、托盘常驻等桌面功能。macOS 与 Windows 提供安装包下载，技能以含 skill.md 的目录为标准格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 技能/提示词/记忆三类资产的本地库管理与跨 agent 同步
- 内置 Claude Code、Codex、Gemini CLI 等 5 种适配器并支持自定义 agent
- 主记忆加模块化记忆，支持合并或接管两种同步模式
- 同步安全数据可备份到对象存储或 Git

## 适用场景

- 在多个 AI coding 工具间复用同一套技能和记忆配置
- 把散落的提示词沉淀为带版本管理的可复用资产
- 跟踪 GitHub 上的技能仓库并选择性导入推送

## 场景标签

`提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: SkillFlow is a cross-platform desktop app for managing reusable skills, prompts, and memories across agent environme
> L40: |**Cross-agent Sync**|Push skills and automatically sync memories across built-in and custom agents.|
> L54: - **Claude Code**

## 星数曲线

```mermaid
xychart-beta
    title "shinerio/SkillFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2fd0cb699466` · [字段定义](../../DATASET.md)*
