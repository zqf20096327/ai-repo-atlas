# npapatheodorou/personal-trainer-skill

⭐ 15 · 推送 2026-06-22 · [GitHub](https://github.com/npapatheodorou/personal-trainer-skill) · 个人维护

**把任意文件型 AI agent 变成健身教练兼营养师的技能包**

一套可移植的 AI 教练系统：以 SKILL.md 与 AGENTS.md 双入口打包同一知识库，将 Claude Code、Codex、Cursor、opencode、Gemini CLI 等具备文件读写能力的 agent 变成个人教练——编排 RPE 渐进超负荷训练、记录训练日志、按 Mifflin-St Jeor 计算热量与宏量营养素、生成餐食计划，并通过工作目录中 coach-data/ 文件夹在会话间持久化运动员档案与日志。内置证据库将每条指导规则映射到力量训练与营养学文献，要求标注证据置信度且不虚构引文。免责声明中明确不替代医生或注册营养师。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 与 AGENTS.md 双入口打包，兼容多种文件型 agent
- coach-data/ 文件持久化：档案、动作库、追加式训练日志、计划与营养目标
- 证据库将训练/营养规则映射到文献并要求标注置信度、拒绝伪科学
- 训练用 RPE 加载与渐进超负荷，营养按 Mifflin-St Jeor 计算热量与蛋白目标

## 适用场景

- 让 Claude Code 或 Codex 等编程 agent 充当我的长期健身教练
- 跨会话记录训练日志、追踪进展并处理平台期
- 计算减脂热量与宏量营养素并生成符合饮食限制的餐食计划

## 场景标签

 · 领域:健康与健身/AI agent 技能

## 证据(README 行号)

> L3: A single, portable **AI coaching system** that turns your agent into a complete,
> L12: - as a **Claude Code / claude.ai skill** (`personal-trainer/SKILL.md`), and

## 星数曲线

```mermaid
xychart-beta
    title "npapatheodorou/personal-trainer-skill 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28", "2026-10-30"]
    y-axis "stars" 11 --> 16
    line [12, 13, 15, 15]
```

2026-10-18 12 → 2026-10-30 15（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `772b7ccc268d` · [字段定义](../../DATASET.md)*
