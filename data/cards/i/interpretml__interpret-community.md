# interpretml/interpret-community

⭐ 444 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/interpretml/interpret-community) · [官网](https://interpret-community.readthedocs.io/en/latest/index.html) · 组织维护

**扩展 Interpret 的表格数据模型可解释性 SDK**

由 Microsoft 维护的实验性仓库，在 Interpret 基础上扩展可解释性技术与工具函数：提供 SHAP（Kernel/GPU/Tree/Deep/Linear）、Mimic 全局代理、PFI、LIME 及自动选型的 TabularExplainer，统一 API 计算全局与局部解释。支持符合 Scikit predict/predict_proba 约定的模型与管道，兼容 PyTorch、TensorFlow、Keras 训练的模型；可将特征工程管道反转为原始特征视角的解释。可视化依赖 raiwidgets 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 种解释器：SHAP 系列、Mimic、PFI、LIME，统一 API
- TabularExplainer 按模型类型自动选择 SHAP 解释器
- 支持 numpy/pandas/scipy 格式与 Scikit 约定模型管道，含 PyTorch/TensorFlow/Keras
- GPU SHAP Kernel Explainer 基于 cuML 加速

## 适用场景

- 解释表格数据上训练的黑箱模型的全局与局部行为
- 用全局代理模型逼近并解释任意黑箱模型
- 在 Jupyter 中通过 ExplanationDashboard 探索模型表现与特征重要性

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: Interpret-Community is an experimental repository extending Interpret, with additional interpretability techniques a
> L15: Interpret-Community extends the Interpret repository and incorporates further community developed and experimental 
> L46: The explanation functions accept both models and pipelines as input as long as the model or pipeline implements a `

## 星数曲线

```mermaid
xychart-beta
    title "interpretml/interpret-community 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 443 --> 445
    line [444, 444]
```

2026-10-29 444 → 2026-10-30 444（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f678c250afd4` · [字段定义](../../DATASET.md)*
