# tscircuit/contribution-tracker

⭐ 25 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/tscircuit/contribution-tracker) · [官网](https://contributions.tscircuit.com) · 组织维护

**用 LLM 扫描 PR 生成周度贡献概览与月度变更日志的网站**

面向 tscircuit 组织的贡献追踪系统：扫描组织内所有 PR，用 LLM 对每个 Diff/PR 做摘要并按属性分类评分，将结果整理为贡献者概览、按仓库/贡献者划分的 PR 表、评分与赞助明细等图表表格，发布到 contributions.tscircuit.com 网站；AI 生成的月度变更日志存放在 changelogs 目录。评分机制中 1-3 星由 AI 自动评定，4-5 星需人工审核。README 提供本地运行的 Development 章节入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描 tscircuit 组织全部 PR 并用 LLM 摘要分类
- AI 自动评定 1-3 星，4-5 星需人工审核
- 按仓库/贡献者组织 PR 与评分表格，含 Staff Pass Ratio 统计
- 生成 AI 月度变更日志

## 适用场景

- 查看开源组织每周贡献概览与评分
- 追踪贡献者的 PR 合并与评审数据
- 查阅 AI 生成的月度项目变更日志

## 场景标签

`AI 写作` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: - All PRs in the tscircuit org are scanned/summarized via an LLM
> L10: - The LLM classifies each Diff/PR as into a set of attributes for scoring
> L5: Generates weekly contribution overviews for tscircuit contributors. Check out all

## 星数曲线

```mermaid
xychart-beta
    title "tscircuit/contribution-tracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f41cc5af22d1` · [字段定义](../../DATASET.md)*
