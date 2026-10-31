# Wehuman01/aweshelf

⭐ 14 · Python · MPL-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/Wehuman01/aweshelf) · 个人维护 · 中文 README

**给 AI 编程 agent 会话做书签分类与恢复的 CLI 工具**

面向 Claude Code 与 Codex 会话的命令行书签管理器：将当前会话保存为书签（标题/分类/profile），支持列表、搜索、按存储 profile 恢复会话；书签仅存 session_id 引用，不复制会话内容，恢复依赖原会话文件仍在磁盘上。提供交互式 TUI 浏览界面（内联编辑、过滤、快捷键）与 VS Code/Cursor 侧边栏扩展；配套 aweswitch 实现多 profile 切换与启动时自动书签。可通过 AI agent 经 SKILL.md 操作，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话书签的创建、分类、搜索与按 profile 恢复
- 交互式 TUI：内联编辑、过滤、快捷键操作
- 配套 aweswitch 实现启动时自动书签与多 profile 恢复
- 提供 SKILL.md 供 AI agent 直接调用，支持 47+ 编程 agent 的 aweskill 安装

## 适用场景

- 我把常用的 AI 编程会话做成书签，之后快速恢复
- 按项目和分类整理 Claude Code / Codex 会话
- 配合 aweswitch 在不同 API profile 间切换并保持会话配置

## 场景标签

 · 领域:开发者工具/AI agent 会话管理

## 证据(README 行号)

> L3:  Bookmark, categorize, and restore AI coding sessions with aweswitch profiles.
> L4:  A lightweight CLI-first tool for Claude Code and Codex session management.

## 星数曲线

```mermaid
xychart-beta
    title "Wehuman01/aweshelf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `95106d214023` · [字段定义](../../DATASET.md)*
