# oolong-tea-2026/arena-ai-leaderboards

⭐ 39 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/oolong-tea-2026/arena-ai-leaderboards) · [官网](https://arena.ai/leaderboard) · 个人维护

**Arena AI 各榜单的每日快照数据仓库，结构化 JSON 并带历史追踪**

Arena AI（原 LMSYS Chatbot Arena）不提供公开 API，本仓库通过 GitHub Actions 每日自动抓取其全部榜单（LLM、视觉、代码、视频、图像等），以统一 JSON Schema 存储每日快照，latest.json 指向最新快照，支持历史追踪。提供免认证 REST API（api.wulong.dev）、Raw GitHub JSON 与 Python 示例三种访问方式。数据含排名、模型、厂商、许可类别、ELO 分、置信区间与投票数。面向需要机器可读榜单数据的开发者与研究者。

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

- GitHub Actions 每日自动更新全部 Arena AI 榜单快照
- 统一 JSON Schema，含 rank/model/vendor/license/score/ci/votes 字段
- 免认证 REST API 与 Raw GitHub JSON 两种访问方式
- latest.json 指针加日期目录实现历史追踪

## 适用场景

- 获取机器可读的模型榜单数据做分析或可视化
- 追踪模型 ELO 分数随时间的变化
- 在应用中嵌入每日更新的榜单数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: **Auto-updated daily snapshots of every Arena AI (formerly LMSYS Chatbot Arena) leaderboard in structured JSON.**
> L11: Arena AI doesn't provide a public API. This repo gives you **stable, machine-readable data with historical tracking

## 星数曲线

```mermaid
xychart-beta
    title "oolong-tea-2026/arena-ai-leaderboards 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `07b0af2e5d87` · [字段定义](../../DATASET.md)*
