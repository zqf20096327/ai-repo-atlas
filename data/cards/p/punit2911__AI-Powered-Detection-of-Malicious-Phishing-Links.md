# punit2911/AI-Powered-Detection-of-Malicious-Phishing-Links

⭐ 49 · Jupyter Notebook · MIT · 推送 2026-11-17 · [GitHub](https://github.com/punit2911/AI-Powered-Detection-of-Malicious-Phishing-Links) · [官网](https://phishprobeai.streamlit.app/) · 个人维护

**面向安全研究者的钓鱼 URL 机器学习检测原型与演示**

由一组 Jupyter notebook 与 Streamlit 应用组成的钓鱼 URL 检测项目：从标注数据中按每类 5,000 条抽样，提取 15 个 URL 结构特征，经三种特征选择流程生成数据集，并对比 10 种分类器；最终以 MinMax 缩放 + Random Forest 的 scikit-learn pipeline 形式提供 model.pkl，供 Streamlit 应用做实时推理并展示分数仪表与特征重要性。README 明确其为研究原型，结果仅反映项目内数据集评估，仅用于研究教育用途。

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

- 15 个 URL 派生特征的提取 pipeline，特征顺序与模型严格对齐
- 10 种分类器在同一数据集上的对比评估（含 stacking/XGBoost/SVM 等）
- 内嵌 model.pkl 可直接推理，train_model.py 可复现训练
- Streamlit 仪表盘提供扫描、分数仪表、特征重要性与会话统计

## 适用场景

- 学习钓鱼 URL 特征工程与分类器对比的完整流程
- 本地运行仪表盘对输入 URL 生成钓鱼评分作为参考
- 基于 dataset_2.csv 复现固定划分下的训练实验

## 场景标签

`网络安全` `模型评测` `教程课程` · 领域:评测与运维

## 证据(README 行号)

> L7: A Streamlit application and a set of Jupyter notebooks for extracting URL
> L18: recreates the selected Random Forest model as a pipeline with MinMax scaling.
> L20: checked-in `model.pkl` for inference.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `e0373b77705c` · [字段定义](../../DATASET.md)*
