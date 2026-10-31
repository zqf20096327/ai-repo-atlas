# AmirhosseinHonardoust/Shap-Mini

⭐ 20 · Python · MIT · 推送 2025-11-09 · [GitHub](https://github.com/AmirhosseinHonardoust/Shap-Mini) · 个人维护

**用 SHAP 解释表格分类模型的最小可复现示例项目**

以 SHAP 框架演示模型可解释性的轻量教学项目：训练 RandomForest 或 LogisticRegression 二分类模型（无数据时自动生成 12 特征合成数据集），计算全局与局部特征重要性，输出重要性条形图与依赖散点图，结果以 JSON/PNG 保存。固定随机种子（42）保证可复现，支持 CPU-only 环境运行，代码量少于 100 行。面向想学习 SHAP 用法与模型审计的开发者和学习者，可替换自有 CSV 数据集扩展使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 RandomForest 与 LogisticRegression 两种基线模型
- 全局重要性图与任意特征依赖图
- 无数据时自动生成合成二分类数据集
- 固定随机种子确保结果可复现

## 适用场景

- 学习 SHAP 值的原理与可视化方法
- 审计小型表格模型的特征贡献
- 用自己的 CSV 数据做特征重要性分析

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **SHAP Mini** is a lightweight and reproducible project that demonstrates **model explainability** using the **SHAP 
> L6: The project is intentionally minimal, using only **RandomForest** and **LogisticRegression**, so users can easily in
> L23: - **SHAP visualization suite:**

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Shap-Mini 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `269fa169e1c2` · [字段定义](../../DATASET.md)*
