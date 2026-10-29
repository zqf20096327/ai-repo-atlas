# vaelkeep/hermes-paper-agent

⭐ 70 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/vaelkeep/hermes-paper-agent) · [官网](https://vaelkeep.github.io/hermes-paper-agent/) · 个人维护

**自动生成个人夜间报纸的 agent：数据桌面写代码、模型写文章**

自托管的个人日报生成器：每天凌晨由 agent 调度运行多个"桌面"——数据桌面（步数、账本、天气、金融）用 Python 代码从 inbox 文件与免费 API 渲染表格和图表，模型不经手数字；散文桌面由 LLM 从已摘要的 feed、笔记、照片各写一篇报道；头版桌面最后汇总写读者次日日程。每个桌面走 write→check→fix 循环，检查未通过则不出版。排版由独立项目 Vael Paper 引擎完成，输出为 markdown 静态站点。示例基于 Hermes Agent，也可运行在 Claude Code、Codex、Cursor 等支持 AGENTS.md 的平台，或无 agent 仅 cron 跑数据桌面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据桌面用代码生成表格与图表，模型不产出数字
- 每桌面运行 write→check→fix 循环，检查未通过不出版
- 由 cron 调度夜间无人值守运行，早晨出刊
- 与 agent 框架解耦：AGENTS.md + SKILL.md + 任意调度器即可迁移

## 适用场景

- 每天早晨读到汇聚自己日历、账本、feed 与实时数据的个人报纸
- 自托管运行个性化每日简报，不依赖第三方推送
- 在任意支持 AGENTS.md 的 agent 平台上复用同一套写报流程

## 场景标签

`AI 写作` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L100: - **Prose desks** are the model (Hermes). They take a handful of
> L102: - **The lead desk** runs last, sees everything, and writes the front page: the
> L113: Every desk — and the edition as a whole — runs the same loop: **write** the

## 星数曲线

```mermaid
xychart-beta
    title "vaelkeep/hermes-paper-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-29"]
    y-axis "stars" 67 --> 71
    line [68, 69, 70, 70]
```

2026-10-18 68 → 2026-10-29 70（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4090c3cf4bb4` · [字段定义](../../DATASET.md)*
