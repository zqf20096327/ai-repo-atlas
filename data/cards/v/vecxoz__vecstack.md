# vecxoz/vecstack

⭐ 697 · Python · NOASSERTION · 推送 2025-11-01 · [GitHub](https://github.com/vecxoz/vecstack) · 个人维护

**Python 堆叠（stacking）集成工具库：自动化 OOF 特征生成**

vecstack 是实现 stacking（stacked generalization）集成技术的 Python 包，提供轻量函数式 API（stacking 函数，一行生成 stacked 特征）与完全兼容 scikit-learn 的 StackingTransformer 转换器 API，可放入 Pipeline 与 FeatureUnion 实现多层堆叠。支持任意 sklearn 风格估计器、分类与回归、类标签或概率预测、自定义度量与目标变换。仅支持 CV 式 stacking（非 blending holdout 式）。依赖 numpy、scipy、scikit-learn>=1.6.0，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 函数式 API 一行生成 stacked 特征，内存占用低
- StackingTransformer 兼容 sklearn Pipeline/FeatureUnion，支持多层堆叠
- 支持任意 sklearn 风格估计器、分类/回归、自定义度量
- 可自动保存每次运行的 stacked 特征与超参数（Kaggle 场景）

## 适用场景

- Kaggle 等竞赛中构建多层 stacking 集成模型
- 在 sklearn Pipeline 中嵌入 stacking 以便部署与调参
- 学习 stacking/OOF 概念并从零实现（含教程与 FAQ）

## 场景标签

 · 领域:机器学习/表格数据建模

## 证据(README 行号)

> L8: Python package for stacking (stacked generalization) featuring lightweight ***functional API*** and fully compatible
> L140: Stacking (stacked generalization) is a machine learning ensembling technique.

## 星数曲线

```mermaid
xychart-beta
    title "vecxoz/vecstack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 696 --> 698
    line [697, 697]
```

2026-10-18 697 → 2026-10-28 697（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9cdf194595a2` · [字段定义](../../DATASET.md)*
