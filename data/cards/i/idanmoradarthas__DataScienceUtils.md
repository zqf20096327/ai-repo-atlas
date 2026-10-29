# idanmoradarthas/DataScienceUtils

⭐ 37 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/idanmoradarthas/DataScienceUtils) · [官网](https://datascienceutils.readthedocs.io/en/latest/) · 个人维护

**扩展 Scikit-Learn/Matplotlib API 的数据科学常用方法库**

Python 工具包 ds_utils，扩展 Scikit-Learn 与 Matplotlib API，提供数据科学项目常用的指标计算与可视化方法。metrics 模块含混淆矩阵绘制、ROC/PR 曲线阈值标注（plotly 后端）、REC 回归曲线、时间序列方向性指标、按概率分组的精度分析及按特征分组的误差报告；preprocess 模块提供特征可视化（按类型自动选择小提琴图/热力图/计数图）、相关性提取与热力图/树状图、特征交互图、PCA 解释方差图等。面向使用 sklearn 生态的数据科学开发者，以 PyPI 包与文档站点形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混淆矩阵、ROC/PR 曲线阈值标注、REC 回归曲线等指标可视化
- 时间序列方向性指标（directional accuracy/bias）
- 按特征值分组输出误差分析报告（DataFrame 表格）
- 特征可视化按数据类型（float/datetime/categorical）自动选择图表，含缺失值处理

## 适用场景

- 分类模型评估时一键绘制混淆矩阵与 ROC/PR 曲线并标注阈值
- 检查模型在哪些特征取值区间上误差偏高
- 探索性数据分析中快速可视化特征分布、相关性与交互关系

## 场景标签

 · 领域:数据科学/机器学习工具

## 证据(README 行号)

> L15: Data Science Utils extends the Scikit-Learn API and Matplotlib API to provide simple methods that simplify tasks an
> L23: The API of the package is built to work with the Scikit-Learn API and Matplotlib API.

## 星数曲线

```mermaid
xychart-beta
    title "idanmoradarthas/DataScienceUtils 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `124def5d086c` · [字段定义](../../DATASET.md)*
