# Batev/XAI-Analytics

⭐ 12 · HTML · BSD-3-Clause · 推送 2026-10-31 · [GitHub](https://github.com/Batev/XAI-Analytics) · 组织维护

**面向用户的机器学习可解释性分析 Jupyter 工具**

以交互式 Jupyter Notebook 形式提供的机器学习解释（XAI）工具：覆盖数据可视化、数据预处理、表格分类模型训练（逻辑回归、决策树、随机森林、SVC、XGBoost）以及全局与局部模型解释（SHAP、ELI5、LIME、优化 LIME 的 CSI/VSI、RBO）。支持 Python 3.12，通过 uv 或 pip+requirements.txt 安装，macOS 需另行安装 libomp。回归解释、无监督与强化学习为声明的非目标；Skater 与旧 PDPbox 适配在当前环境不可用。由维也纳工业大学成员创建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 表格分类模型训练（逻辑回归/决策树/随机森林/SVC/XGBoost）
- 多种解释技术：SHAP、ELI5、LIME、优化 LIME（CSI/VSI）、RBO
- 交互式 Jupyter Notebook 界面，支持本地数据与 CSV
- 跨平台 CI（Windows/Linux/macOS）离线测试套件

## 适用场景

- 训练表格分类模型并查看其全局与局部解释
- 在 Jupyter 中对数据集做可视化与预处理后建模
- 比较不同解释技术对同一模型实例的说明

## 场景标签

 · 领域:机器学习可解释性

## 证据(README 行号)

> L3: XAI-Analytics is a tool that opens the black-box of machine learning. It makes model interpretability easy.
> L4: **XAI-Analytics** offers a wide range of features such as data visualization, data preprocessing, ML-model training 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 mid · 依据 README sha `2406863c0e17` · [字段定义](../../DATASET.md)*
