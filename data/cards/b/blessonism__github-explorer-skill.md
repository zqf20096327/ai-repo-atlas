# blessonism/github-explorer-skill

⭐ 79 · MIT · 推送 2026-10-22 · [GitHub](https://github.com/blessonism/github-explorer-skill) · 个人维护 · 中文 README

**OpenClaw 技能：对任意 GitHub 项目做多源深度分析并输出研判报告**

面向 OpenClaw Agent 框架的技能（Skill）：输入任意 GitHub 项目名或仓库链接，自动抓取 Issues、Commits、中文社区（知乎/V2EX/微信）、技术博客与 Twitter 讨论等多源信息，调用内置 web_search/web_fetch/browser 工具，结合可选的 search-layer 等搜索技能，按固定模板输出结构化研判报告（含项目阶段判断、精选 Issue、竞品对比、知识源收录情况）。缺少依赖技能时自动降级为仅用内置工具。通过 npx 或 git clone 安装到 ~/.openclaw/skills/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多源采集：README 之外的 Issues、Commits、中文社区、博客、Twitter 讨论
- 意图感知搜索与多查询并行采集，结果按权威性/新鲜度加权排序
- 固定模板结构化输出（定位/健康度/竞品对比/局限/判断等 14 个模块）
- 依赖技能缺失时自动降级为仅用内置工具

## 适用场景

- 选型前快速研判一个开源项目的阶段与活跃度
- 了解某项目在技术社区与中文社区的讨论声量
- 对比同赛道项目差异辅助技术选型

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: GitHub Explorer 是一个 OpenClaw Agent Skill，能够对任意 GitHub 项目进行**多源深度分析**，输出结构化的项目研判报告。
> L34: 本 Skill 会调用以下 OpenClaw 内置工具（无需额外安装）：`web_search`、`web_fetch`、`browser`

## 星数曲线

```mermaid
xychart-beta
    title "blessonism/github-explorer-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-30 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `565ad6f0135a` · [字段定义](../../DATASET.md)*
