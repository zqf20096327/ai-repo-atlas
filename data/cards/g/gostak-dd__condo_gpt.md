# gostak-dd/condo_gpt

⭐ 67 · Python · 推送 2026-01-12 · [GitHub](https://github.com/gostak-dd/condo_gpt) · 个人维护

**用自然语言查询分析迈阿密公寓数据的 AI 助手**

面向非技术的房产经纪人与投资者的网页应用：用户以自然语言提问，系统借助 LangChain/LangGraph agent 与 OpenAI GPT 模型解读问题、动态生成 SQL 查询 PostgreSQL（Condo Cube 样例库，覆盖 South Beach/Miami Beach 等区域），并生成交互式地图、图表与 PDF 报告，集成 Google Maps API 做地理编码。需自备 OpenAI 与 Google Places API key，本地部署 Flask + PostgreSQL 运行。作者将项目定位为求职作品集，同时开放贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言提问并动态生成 SQL 查询 PostgreSQL 数据库
- 集成 Google Maps API 支持位置类查询与交互式地图
- 生成图表与 PDF 报告
- 基于 LangChain & LangGraph agent 架构

## 适用场景

- 房产经纪人和投资者用自然语言做公寓市场分析与对比
- 生成带地图和图表的分析报告辅助投资决策
- 作为 LangChain 项目练习的开源贡献入口

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: Condo GPT is an intelligent assistant for querying and analyzing condominium data in Miami. It uses natural language
> L13: The purpose is to allow real estate agents and investors who are not technical, to easily and quickly perform high-

## 星数曲线

```mermaid
xychart-beta
    title "gostak-dd/condo_gpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-24 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `eb73d4064a49` · [字段定义](../../DATASET.md)*
