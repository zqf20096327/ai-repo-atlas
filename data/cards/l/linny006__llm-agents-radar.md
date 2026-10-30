# linny006/llm-agents-radar

⭐ 15 · Python · 推送 2026-10-29 · [GitHub](https://github.com/linny006/llm-agents-radar) · [官网](https://github.com/linny006?utm_source=github&utm_medium=about&utm_campaign=llm-agents-radar) · 个人维护 · 中文 README

**LLM agent 框架的自动更新索引，GitHub 每 15 分钟刷新**

一个由 GitHub Actions cron 驱动的自更新追踪器：每 15 分钟运行 tracker.py，通过 GitHub Search API 抓取 LLM agent 框架仓库，与 data/items.json 快照做 diff，重写 README 中的条目表格并提交变更（新增/过期移除）。面向需要发现 GitHub 上新出现 agent 框架的开发者，条目按活跃度信号排序，包含星数、语言、更新时间与描述。无外部服务、无付费 API，同一维护者还维护十余个同机制的 topic 追踪器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub Actions cron 每 15 分钟自动扫描并重写条目表格
- 以 GitHub Search API 为数据源，diff 快照后提交增删变更
- 条目含星数/语言/更新时间/描述，按活跃度信号排序
- 同一维护者提供 12 个相关 topic 的 live 追踪器

## 适用场景

- 发现 GitHub 上新发布的 LLM agent 框架
- 跟踪 agent 生态近期有哪些新项目上下架
- 按活跃度信号浏览当前 agent 框架列表

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: Live-updating index of LLM agent frameworks shipping on GitHub, refreshed every 15 minutes
> L16: A self-updating tracker that discovers and indexes new LLM agent frameworks as they appear on GitHub. Unlike static
> L18: This list is **auto-updated every 15 minutes** by a GitHub Actions cron.

## 星数曲线

```mermaid
xychart-beta
    title "linny006/llm-agents-radar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cfd32be13bcb` · [字段定义](../../DATASET.md)*
