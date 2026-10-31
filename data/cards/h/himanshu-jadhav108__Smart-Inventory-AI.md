# himanshu-jadhav108/Smart-Inventory-AI

⭐ 15 · Python · 推送 2026-07-16 · [GitHub](https://github.com/himanshu-jadhav108/Smart-Inventory-AI) · [官网](https://smart-inventory-ai.streamlit.app/) · 组织维护

**面向零售商的 AI 需求预测与库存优化应用**

基于 Streamlit 的零售库存预测与优化平台：上传销售 CSV（date, product_id, units_sold）后，系统用 EWMA、线性回归、季节分解的集成方法生成需求预测，结合统计与 IQR 方法做异常检测并给出严重度评分，按需求波动动态计算安全库存与再订货点，并输出面向业务的解释性建议。面向中小零售商设计，可本地或云端运行，附 Kaggle 测试数据集与在线 Demo。模型预测精度以 MAE/MAPE 和 walk-forward 测试衡量。

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

- 集成预测（EWMA/线性回归/季节分解）生成需求预测
- 统计+IQR 异常检测并附严重度评分
- 动态安全库存与再订货点计算（考虑提前期与需求波动）
- CSV 即传即用，内置 Kaggle 测试数据集与应用内样本数据

## 适用场景

- 上传销售数据获得补货量与补货时点建议
- 发现销量异常波动并评估严重度
- 为小店或多店连锁计算安全库存，减少积压与缺货

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L64: - **Ensemble Forecasting**: EWMA, Linear Regression, Seasonal Decomposition
> L65: - **Anomaly Detection**: Statistical + IQR-based methods with severity scoring
> L66: - **Safety Stock Optimization**: Dynamic calculations based on demand volatility

## 星数曲线

```mermaid
xychart-beta
    title "himanshu-jadhav108/Smart-Inventory-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `89668c14b369` · [字段定义](../../DATASET.md)*
