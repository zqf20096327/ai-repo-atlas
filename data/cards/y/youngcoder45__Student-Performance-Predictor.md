# youngcoder45/Student-Performance-Predictor

⭐ 15 · Python · MIT · 推送 2026-06-25 · [GitHub](https://github.com/youngcoder45/Student-Performance-Predictor) · 个人维护

**用机器学习预测学生期末成绩与及格结果的端到端项目**

基于 scikit-learn 的端到端机器学习项目，解决两个任务：回归预测学生期末分数、分类预测及格与否。数据来自 UCI 学生成绩数据集（不可下载时生成确定性合成数据离线训练），流程覆盖数据清洗、特征工程（学习效率、风险指数等）、多模型对比、RandomizedSearchCV 调参、joblib 模型持久化，并通过 Streamlit 网页应用交付预测（分数、及格概率、置信度、特征贡献图）。定位为作品集项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 回归与分类双任务：多算法对比后选定 Random Forest 与 Gradient Boosting
- UCI 数据集集成与确定性离线合成数据回退
- 特征工程含学习效率、作业完成率、风险指数等指标
- Streamlit 应用输出预测分数、及格概率与特征贡献图

## 适用场景

- 输入学生信息预测期末成绩与及格概率
- 复现完整的 ML 工作流作为学习或作品集参考
- 离线环境下训练与演示学生成绩预测

## 场景标签

 · 领域:教育/机器学习

## 证据(README 行号)

> L14: - Regression: predict a student's final exam score from academic, behavioral, and demographic inputs.
> L15: - Classification: predict whether the student is likely to pass or fail.
> L107: 11. Serve predictions through Streamlit.

## 星数曲线

```mermaid
xychart-beta
    title "youngcoder45/Student-Performance-Predictor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `60cc91a3b2ff` · [字段定义](../../DATASET.md)*
