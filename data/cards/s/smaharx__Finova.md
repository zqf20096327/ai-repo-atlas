# smaharx/Finova

⭐ 21 · Python · NOASSERTION · 推送 2026-09-14 · [GitHub](https://github.com/smaharx/Finova) · 个人维护

**个人财务追踪应用：NLP 分类、异常检测与支出预测**

基于 Streamlit 与 SQLite 的本地个人财务追踪应用：用户录入的交易通过 NLP 自动分类，Isolation Forest 标记异常消费，Prophet 生成 30 天支出预测，并提供纠正 AI 分类结果的人工界面。分层架构为 Streamlit UI、Pandas/Scikit-learn/Prophet 处理层与本地 SQLite 数据层。安装方式为 git clone 源码加 pip 依赖，附带注入 2 万条合成交易的种子脚本用于模型测试；README 列出微服务化与 PostgreSQL 迁移等未来计划但当前为单体本地应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NLP 自动交易分类，支持人工纠正（Human-in-the-loop）
- Isolation Forest 无监督异常消费检测
- Prophet 30 天支出预测
- 合成数据种子脚本注入 20,000 条交易用于模型测试

## 适用场景

- 本地记录并自动分类日常支出
- 发现异常消费并获得支出预测
- 需要数据留在本地 SQLite 的个人财务分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: Finova is a personal finance tracker that helps you manage spending, correct AI predictions, detect anomalies, and 
> L16: The system allows users to input transactions which are automatically categorized via NLP. It then processes histor
> L22: - Unsupervised anomaly detection (Isolation Forest) for unusual spending

## 星数曲线

```mermaid
xychart-beta
    title "smaharx/Finova 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6df85e6a7c55` · [字段定义](../../DATASET.md)*
