# holistic-ai/holisticai

⭐ 114 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/holistic-ai/holisticai) · [官网](https://holisticai.readthedocs.io/en/latest/index.html) · 组织维护

**面向开发者的 AI 系统可信度评估与偏差缓解 Python 库**

开源 Python 库，围绕准确率之外的五个维度评估 AI 系统：偏差（65 个指标、28 个缓解器）、可解释性（LIME/SHAP 后端）、鲁棒性、安全/隐私与效能。指标为普通数组函数，兼容 fit/predict 接口的 scikit-learn 形态模型；提供带缓解器插槽的 Pipeline，缓解器可作用于前/中/后处理阶段。内置 18 个公平性相关数据集，首次使用时拉取并缓存。基础安装仅含 scikit-learn/pandas/numpy/pyarrow，重型依赖（JAX、SHAP 等）按 extra 可选安装；macOS 上部分缓解器的求解器需先装 C 工具链。需 Python 3.9+，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个维度：bias/explainability/robustness/security/efficacy，共 100+ 指标
- 28 个偏差缓解器，支持 pre/in/post-processing 三阶段，兼容 scikit-learn Pipeline
- 内置 18 个按受保护属性预切分的数据集加载器
- 指标为纯数组函数，批量报告返回 pandas DataFrame

## 适用场景

- 检测分类/回归模型是否对不同人群存在偏差
- 在现有 scikit-learn 训练流程中插入偏差缓解步骤
- 评估模型的隐私泄露与对抗鲁棒性

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L33: An open-source library for assessing and improving the safety aspects of AI
> L38: against a scikit-learn-shaped model — and for bias, a mitigator you can drop

## 星数曲线

```mermaid
xychart-beta
    title "holistic-ai/holisticai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-29 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ee1e56200982` · [字段定义](../../DATASET.md)*
