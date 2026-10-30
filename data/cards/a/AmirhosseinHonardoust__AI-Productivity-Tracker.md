# AmirhosseinHonardoust/AI-Productivity-Tracker

⭐ 35 · Python · MIT · 推送 2026-09-09 · [GitHub](https://github.com/AmirhosseinHonardoust/AI-Productivity-Tracker) · 个人维护

**教育演示：用 SQL 特征工程与 ElasticNet 回归预测每日生产力分数**

基于 Python/scikit-learn 的回归流水线演示项目：将合成日常行为 CSV 载入 SQLite，经 queries.sql 派生心理学启发特征（昼夜节律对齐、Yerkes–Dodson 唤醒、深工作时长等），训练 ElasticNet 回归模型并对新日期输出连续生产力估计。含模型对比（ElasticNetCV/随机森林/GBDT）、SHA-256 校验的模型工件、合成数据生成器与命令行训练评分。README 明确声明这是教学演示而非经过验证的心理或职业健康工具，R²≈0.32 为披露上限，不用于监测真实人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SQL 视图派生心理学启发特征并做列/范围校验
- ElasticNet 与三种备选模型在同一切分上的文档化对比
- 模型工件 SHA-256 校验，unpickle 前验证完整性
- 合成数据生成器与跨 Python 3.10–3.12 的 CI（95% 覆盖率门禁）

## 适用场景

- 学习诚实评估的端到端回归工作流
- 参考 SQL 特征工程与训练/评分特征一致性实践
- 复现或调整合成行为数据上的模型对比实验

## 场景标签

 · 领域:机器学习/行为分析

## 证据(README 行号)

> L11: A responsible machine learning project that turns daily behavioral logs into a **productivity signal**, using **SQL
> L38: - Train an interpretable ElasticNet regression model
> L42: - Score new, unlabeled "candidate" days with the trained model

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/AI-Productivity-Tracker 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-30 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5a5d7b9dbfc0` · [字段定义](../../DATASET.md)*
