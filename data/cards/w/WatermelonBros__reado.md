# WatermelonBros/reado

⭐ 30 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/WatermelonBros/reado) · [官网](https://reado.watermelon-studio.it) · 组织维护

**面向读代码与评审的 IDE：人标注行级评论，AI agent 执行修复**

基于 Tauri/React/TypeScript/Rust 构建的跨平台（macOS/Linux/Windows）读码与评审工具。核心理念是'倒置代码评审'：用户作为评审者阅读代码、在具体行上留下锚定评论（可标记为 task 或 note），再通过内置终端启动 Claude Code、Codex、Copilot 等 agent，经 reado CLI 与 MCP server 读取任务并修复代码，过程实时反映在界面中。评论以 Markdown 存于 .reado/ 目录，代码变动后自动重锚定；另含阅读进度追踪、项目 tour、知识库、可被 agent 驱动的内置浏览器与手机配对功能。MIT 许可，本地优先。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 行级锚定评论持久化为 .reado/ 下的 Markdown，代码移动后自动重锚定
- reado CLI 与 MCP server 构成 agent 稳定契约（task list/done/fail、reado://tasks 等资源）
- agent 在应用内终端工作，读码与修复过程实时可见
- 阅读进度追踪、项目 tour（tour.json）、docs/specs 知识库与可被 agent 驱动的内置浏览器

## 适用场景

- 审阅 AI agent 生成的大量代码并逐行下达修复任务
- 在专注阅读的界面里做分支/PR 评审并保留评论记录
- 让 Claude Code/Codex 等 agent 按我批准的清单自动修复问题

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L31: leave comments anchored to the exact lines that matter; your agent (Claude Code,
> L35: > **Inverted code review:** you are the reviewer, the AI is the committer.

## 星数曲线

```mermaid
xychart-beta
    title "WatermelonBros/reado 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3a75e720da18` · [字段定义](../../DATASET.md)*
