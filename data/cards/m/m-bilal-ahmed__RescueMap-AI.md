# m-bilal-ahmed/RescueMap-AI

⭐ 17 · TypeScript · 推送 2026-04-01 · [GitHub](https://github.com/m-bilal-ahmed/RescueMap-AI) · [官网](https://rescuemap-ai.org/) · 个人维护

**灾害应急响应平台：验证与聚类地理位置报告并实时可视化**

面向应急救援人员与地方团队的开源地理空间平台：从官方源（FEMA/USGS）、注册伙伴和公众提交等多渠道接收位置报告，用逻辑回归与随机森林分类器按来源可信度、地理聚类、文本相似度和时效性进行可靠性评分，DBSCAN 思路的聚类合并近似重复报告，结果以 Leaflet 实时地图按验证状态分色展示，并提供 Verified Rate KPI。离线优先架构，可在单台笔记本或树莓派上运行，无需云服务；有同行评审论文支撑（DOI: 10.55041/ISJEM.04944）。技术栈为 Flask + Next.js + Scikit-learn/NLTK + SQLite/PostgreSQL，需从源码分别启动前后端。

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

- 逻辑回归/随机森林验证层，可在低配硬件离线运行
- 按 severity × confidence × recency 透明可审计地排序报告
- DBSCAN 聚类合并近似重复报告，来源可信度加权
- 离线优先：单机或树莓板可运行，恢复连接后同步数据

## 适用场景

- 灾害期间对多渠道涌入门的位置报告做去重与可信度排序
- 在断网或云服务不可用的现场环境下维持态势图
- 查看实时地图与验证率 KPI 以确定优先处置区域

## 场景标签

 · 领域:灾害应急/地理空间

## 证据(README 行号)

> L19: RescueMap-AI ingests location-based reports from multiple sources, validates them using lightweight machine learnin
> L70: **Abstract:** A lightweight pipeline employing logistic regression and random forest classifiers, integrated with r

## 星数曲线

```mermaid
xychart-beta
    title "m-bilal-ahmed/RescueMap-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bff60042424f` · [字段定义](../../DATASET.md)*
