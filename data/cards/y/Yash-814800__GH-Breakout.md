# Yash-814800/GH-Breakout

⭐ 5 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Yash-814800/GH-Breakout) · [官网](https://yash-814800.github.io/GH-Breakout/) · 个人维护

**每日公开的新 GitHub 仓库突破预测排行榜，带可验证记录**

一个数据工程与预测项目：每日从 GH Archive 事件数据中识别有增长动量的年轻仓库，用 LightGBM 模型输出未来 30 天爆发的概率，每条分数附一句解释（SHAP 句子），所有预测写入哈希链账本固化到 Hugging Face，使记录不可被悄悄修改。管线由 GitHub Actions 每日运行，dbt 分四层组织 52 个模型与 274 个测试，站点用 Astro 部署于 GitHub Pages，浏览器内可运行 DuckDB-WASM 查询 Parquet。全栈使用免费额度，声明成本为 $0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LightGBM 模型输出突破概率并附 SHAP 生成的解释句
- 每日预测写入哈希链账本，支持 breakout ops verify-ledger 校验
- 52 个 dbt 模型、274 个 dbt 测试与 390 个 Python 测试
- 点时特征、泄漏测试与带 30 天禁运期的滚动起点评估

## 适用场景

- 每天查看哪些年轻 GitHub 仓库被标记为可能的突破者
- 查看某仓库的历史预测记录并核验哈希链完整性
- 参考其 dbt 分层建模与数据质量测试的工程实践
- 在浏览器中用 SQL 直接查询其公开 Parquet 数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L24: Breakout Radar ranks today's candidates by that probability, explains each score in a sentence, and
> L25: records every prediction in a hash-chained ledger so the track record can be checked by anyone.
> L38: |**Model** (LightGBM, calibrated)|**0.108** [0.102, 0.114]|**0.241** [0.228, 0.255]|

## 星数曲线

```mermaid
xychart-beta
    title "Yash-814800/GH-Breakout 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-23 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ec0c2c283b93` · [字段定义](../../DATASET.md)*
