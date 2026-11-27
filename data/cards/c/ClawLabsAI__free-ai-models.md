# ClawLabsAI/free-ai-models

⭐ 294 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/ClawLabsAI/free-ai-models) · [官网](https://www.zerolimitai.com/developers?utm_source=github&utm_medium=repo_about) · 组织维护

**免费 LLM API 每日更新清单：按质量排名并标注数据政策**

每日更新的免费 AI 模型（免费 LLM API）聚合清单：用可读可重跑的评分脚本（scoring/score.js）结合基准指数与 LM Arena 评分对免费聊天模型排名，每行标注服务方是否可能用提示词训练及保留时长，并以 data/models.json 每日重新生成、按天保存快照。另附各免费端点的 base_url、限额与限制对照表。模型 id 为 OpenRouter id，可在支持该 id 的工具中直接使用。无 key 即可读取数据，仅采集公开官方 API。

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

- 以开源评分脚本每日对免费模型排名，输入来源可重算
- 标注每个免费端点的数据使用政策（是否训练/保留时长）
- data/models.json 每日重生成并保留历史快照
- 提供 OpenRouter/Groq/Google AI Studio 等端点限额与限制表

## 适用场景

- 找当前可用的免费 LLM API 并比较质量
- 发送敏感数据前查看服务方是否会用提示词训练
- 程序化读取 JSON 数据做模型选型或路由

## 场景标签

`精选清单` · 领域:学习与行业

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6bff8fbc2dc6` · [字段定义](../../DATASET.md)*
