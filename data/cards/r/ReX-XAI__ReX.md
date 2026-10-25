# ReX-XAI/ReX

⭐ 48 · Jupyter Notebook · MIT · 推送 2026-10-20 · [GitHub](https://github.com/ReX-XAI/ReX) · [官网](https://rex-xai.readthedocs.io/) · 组织维护

**图像/表格分类器的因果责任解释工具，黑盒可解释性**

面向图像分类器（也支持表格与 3D 数据）的因果可解释性工具：给定输入与分类器，计算数据上的因果责任图（responsibility map），并识别最小、充分的解释；可找出单一解释、非连续解释、多个独立解释与对比解释。黑盒设计，不依赖分类器内部结构。通过 pip 安装 rex_xai，默认依赖 onnxruntime，GPU 需换装 onnxruntime-gpu，3D 数据需额外安装可选依赖。要求 Python >= 3.10。

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

- 计算因果责任图并识别最小、充分的解释
- 黑盒方法，对分类器内部结构不可知
- 支持图像、表格与 3D 数据
- 支持非连续解释、多独立解释与对比解释

## 适用场景

- 解释图像分类器的预测依据
- 为部分遮挡图像找出非连续的解释区域
- 对表格或 3D 数据的模型输出做因果归因

## 场景标签

 · 领域:机器学习可解释性

## 证据(README 行号)

> L9: ReX is a causal explainability tool for image classifiers. It also works on tabular and 3D data.
> L15: ReX is black-box, that is, agnostic to the internal structure of the classifier.

## 星数曲线

```mermaid
xychart-beta
    title "ReX-XAI/ReX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `015de97378af` · [字段定义](../../DATASET.md)*
