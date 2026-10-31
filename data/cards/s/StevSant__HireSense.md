# StevSant/HireSense

⭐ 14 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/StevSant/HireSense) · [官网](https://hiresense-demo.vercel.app) · 个人维护

**自托管求职全流程平台：聚合招聘信息并用 LLM 排序匹配**

面向求职者的自托管 Web 应用（FastAPI + Angular 22 + PostgreSQL/pgvector）。从多个招聘网站与公司 ATS 门户抓取职位，按稳定身份去重后，用 pgvector 全库语义预排序、技能重叠与分层 LLM 评分（便宜模型过滤、强模型排序）生成匹配榜单；并覆盖投递跟踪（Saved→Offer）、按职位定制 CV 与求职信生成、面试准备、外联、市场分析与自动巡航。无 LLM key 时可回退到纯启发式匹配；Postgres 为必需依赖，无 SQLite 回退。通过 Docker Compose 部署，含 Grafana 可观测性栈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector 全库 ANN 预排序 + 技能重叠 + 分层 LLM 评分的匹配管线
- 多来源职位抓取并按稳定身份去重，含变更与关闭检测
- 投递管道跟踪、模板化 CV/求职信生成、市场分析、Autopilot 定时任务
- APP_MODE=local 无 LLM key 也可运行（纯启发式匹配）

## 适用场景

- 把多平台招聘信息聚合成按匹配度排序的短名单
- 跟踪每个职位从收藏到 Offer 的投递进度与产物
- 为每个职位生成定制的 CV 与求职信

## 场景标签

`语义搜索` `网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L5: HireSense pulls postings from job boards and company ATS portals, ranks them against your
> L6: profile with **pgvector semantic search + tiered LLM scoring**, and runs the whole pipeline
> L74:  with skill overlap and **tiered LLM scoring** (cheap models filter, strong models rank).

## 星数曲线

```mermaid
xychart-beta
    title "StevSant/HireSense 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `27172028fe2e` · [字段定义](../../DATASET.md)*
