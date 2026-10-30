# JingbiaoMei/work-canvas-skill

⭐ 20 · CSS · Apache-2.0 · 推送 2026-06-25 · [GitHub](https://github.com/JingbiaoMei/work-canvas-skill) · 个人维护 · 中文 README

**把 agent 工作成果渲染为单文件可审阅 HTML 的 Agent 技能**

面向编码 agent 的技能（SKILL.md 格式）：让 agent 将进度、调试、分析、对比与决策等工作过程渲染为一个自包含的离线 HTML 页面（work canvas）。提供三类产物骨架——进度/状态报告、评审/决策备忘、对比/排行榜，页面内联 CSS/JS 与媒体、无 CDN、双击离线打开，含浅色/深色双主题与来源页脚。以 work-canvas.skill 压缩包形式由 agent 自行安装到 Claude Code、Codex、Pi、OpenCode 等工具的技能目录。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类产物骨架：进度报告、评审/决策备忘、对比/排行榜
- 输出单文件自包含 HTML（内联 CSS/JS、无 CDN、离线打开）
- 页面含 agent+模型+日期的来源页脚与非破坏性输出原则
- 提供 work-canvas.skill 打包文件供 agent 自动安装到多种工具

## 适用场景

- 把长任务或基准测试的进度整理成一页可浏览的报告
- 生成可标注评论的 HTML 评审/决策文档用于团队对齐
- 构建带成本与延迟列的多方案对比页

## 场景标签

 · 领域:开发者工具/Agent 技能

## 证据(README 行号)

> L9: When a long or messy task is better *seen* than read line-by-line in a terminal, `work-canvas` has the agent render 
> L31: This skill is **agent-installable**. The repo ships a packaged **`work-canvas.skill`** — a zip of just the skill fo
> L59: SKILL.md                 router + workflow + conventions

## 星数曲线

```mermaid
xychart-beta
    title "JingbiaoMei/work-canvas-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b21e3fc5e719` · [字段定义](../../DATASET.md)*
