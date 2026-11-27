# ClawLabsAI/free-ai-models

⭐ 294 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/ClawLabsAI/free-ai-models) · [官网](https://www.zerolimitai.com/developers?utm_source=github&utm_medium=repo_about) · 组织维护

**每日更新的免费 LLM API 排名清单及评分方法**

一份每日自动更新的免费 AI 模型（免费 LLM API）清单：按可复现的开源评分文件（基准测试 55/45 混合 LM Arena 评分）对 12 个免费聊天模型排名，逐行标注托管方是否会用提示词训练及保留时长，并记录实时可用状态。数据以 `data/models.json` 每日重新生成并保留每日快照，可用 curl/jq/Python/JavaScript 直接读取。id 采用 OpenRouter 格式，可直接用于 OpenAI SDK、LiteLLM、Cline 等工具。另列出各免费 provider 的 base URL 与限额表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每日自动重建排名，快照存于 data/history/
- 标注每个免费端点的数据训练政策与保留时长
- 评分方法为可读取、可重跑的 scoring/score.js
- 提供稳定 JSON URL 供程序直接消费

## 适用场景

- 选免费模型前查它是否拿我的提示词训练
- 为应用自动挑选今日最好的免费模型
- 对比各免费 provider 的限额与数据政策

## 场景标签

`精选清单` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: **A daily-updated list of every free AI model (free LLM API) available right now,
> L26: - **It is data, not just a page.** `data/models.json` is
> L38: |#|Model|Score|Measured by|Trains on your prompts?|Context|Max output|Tools|Input|Today|Source|

## 星数曲线

```mermaid
xychart-beta
    title "ClawLabsAI/free-ai-models 星数(近 24 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 230 --> 299
    line [235, 238, 243, 245, 246, 249, 251, 235, 260, 262, 263, 264, 266, 267, 269, 272, 275, 278, 280, 281, 285, 288, 290, 294]
```

2026-10-25 235 → 2026-11-27 294（+59）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `879315e0bca1` · [字段定义](../../DATASET.md)*
