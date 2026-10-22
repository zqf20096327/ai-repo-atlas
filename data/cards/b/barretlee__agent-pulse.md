# barretlee/agent-pulse

⭐ 240 · TypeScript · MIT · 推送 2026-08-28 · [GitHub](https://github.com/barretlee/agent-pulse) · [官网](https://barretlee.github.io/agent-pulse/) · 个人维护 · 中文 README

**面向决策者的 AI 行业情报系统：信号→证据→判断→下一步信号**

将官方发布、论文、资本与政策变化、传播信号加工为可溯源的事件（Event），维护六个战略视图、证据时间线、414 个来源的目录与健康度审计。仓库包含采集器、证据模型、质量门、静态渲染与 GitHub Pages 交付路径，GitHub Actions 每日刷新数据、每周生成决策简报。事件分为事实/证据/背景/影响/判断/下一步信号六层，发布需过确定性门控；DeepSeek 的 AI 增强为本地实验性可选功能。本地运行需 Node.js 22+，SQLite 为零配置默认存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 414 个来源目录与健康/降级/失败审计（266/27/70/51）
- 事件六层结构：事实→证据→背景→影响→判断→下一步信号
- GitHub Actions 每日数据刷新 + 每周门控式决策简报
- catalogued/observed/active/published 四态分离的证据管线

## 适用场景

- 投资与企业管理者跟踪 AI 行业的实质变化而非新闻
- 研究者查看有原始出处的行业事件时间线
- 评估来源覆盖强弱与活跃度的公开情报基础设施

## 场景标签

 · 领域:AI 行业情报/数据基础设施

## 证据(README 行号)

> L7: > **Evidence-backed AI industry intelligence for people who need to decide, not just keep up.** Agent Pulse turns of
> L38: |**Evidence timeline**|What happened first, what changed later, and which primary sources support it?|Every publish
> L131: AI-assisted Event convergence and weekly-brief drafting remain **experimental and opt-in for local runs**. Put `DE

## 星数曲线

```mermaid
xychart-beta
    title "barretlee/agent-pulse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 239 --> 241
    line [240, 240]
```

2026-10-18 240 → 2026-10-22 240（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fd8d6e61a813` · [字段定义](../../DATASET.md)*
