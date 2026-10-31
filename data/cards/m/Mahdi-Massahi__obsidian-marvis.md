# Mahdi-Massahi/obsidian-marvis

⭐ 14 · TypeScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/Mahdi-Massahi/obsidian-marvis) · 个人维护

**Obsidian 多视图项目规划与习惯追踪插件，含 Gemini 语音助手**

面向 Obsidian 用户的项目规划与习惯追踪插件：项目、里程碑、任务、日志、事件均为带 frontmatter 的 markdown 笔记，其上提供 Kanban、Timeline（甘特图）、Calendar、Table 四种视图，支持拖拽、过滤、模糊搜索与 RRULE 循环任务。AI 部分为基于 Google Gemini Live 的语音/文本助手（需自带 API key，写库前有确认弹窗），并为外部编码 agent 提供 marvis-project 技能。macOS 支持 Apple 日历单向同步，移动端可用；开发者自述产品处于新发布阶段、存在粗糙边缘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四种视图渲染同一数据源（markdown 笔记）
- Gemini Live 语音/文本助手，感知当前项目与笔记，写库经确认弹窗
- 为 Claude Code/Cursor 等编码 agent 生成 marvis-project 技能文件
- macOS Apple 日历单向同步，移动端可用

## 适用场景

- 在 Obsidian 中用看板、甘特图、日历管理项目和任务
- 用语音或对话让 AI 助手添加任务、查询日程
- 让 Claude Code/Cursor 等编码 agent 直接读取和更新规划笔记

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L9: A multi-view project planner and habit tracker for Obsidian. Projects, milestones, tasks, logs, habits and events ar
> L19: Talk to your planner — voice or text — via **Google Gemini Live**. Knows your projects and the note you have open, 
> L24: ### 🦾 Coding agents as project managers

## 星数曲线

```mermaid
xychart-beta
    title "Mahdi-Massahi/obsidian-marvis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a8821445d6b3` · [字段定义](../../DATASET.md)*
