# TsLu1s/atlantic

⭐ 34 · Python · MIT · 推送 2026-02-02 · [GitHub](https://github.com/TsLu1s/atlantic) · 个人维护

**监督学习表格数据的自动预处理框架**

面向表格数据的 Python 预处理库：基于输入列特征自动执行编码（label/one-hot/逆频率）、缩放（Standard/MinMax/Robust）、缺失值填补（简单/KNN/迭代）与特征选择（VIF 去多重共线、H2O AutoML 重要性筛选），并以树模型集成评估优化流程。提供一体化 Atlantic 管道（含 fast/balanced/thorough 等预设）与 AtlanticBuilder 流式接口做细粒度控制。基于 H2O.ai、Scikit-learn、XGBoost、Optuna、Pandas 构建，经 PyPI 以 pip install atlantic 安装。

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

- fit_processing 一体化自动预处理管道，支持 fast/balanced/thorough 优化级别
- AtlanticBuilder 流式接口提供编码/缩放/填补/特征选择细粒度控制
- H2O AutoML 特征选择与 VIF 多重共线过滤
- 三种自动编码器、缩放器与填补器组件可单独使用

## 适用场景

- 表格数据建模前省去手工特征工程与清洗
- 自动筛选低重要性与多重共线特征
- 处理含大量缺失值的预测建模数据集

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: The `Atlantic` project constitutes a comprehensive and objective approach to simplify and automate data processing 
> L18: * Automated treatment of tabular data associated with predictive analysis: It implements a global and carefully val

## 星数曲线

```mermaid
xychart-beta
    title "TsLu1s/atlantic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `084583301281` · [字段定义](../../DATASET.md)*
