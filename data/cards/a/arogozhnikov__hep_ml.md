# arogozhnikov/hep_ml

⭐ 199 · Jupyter Notebook · NOASSERTION · 推送 2026-08-23 · [GitHub](https://github.com/arogozhnikov/hep_ml) · [官网](https://arogozhnikov.github.io/hep_ml/) · 个人维护

**面向高能物理的机器学习 Python 库：均匀分类器与多维重加权**

面向高能物理研究场景的 Python 机器学习库，提供与质量等变量低相关的均匀分类器（uBoost、UGradientBoosting 及 FlatnessLoss 等损失函数）、均匀性度量、多维分布重加权（GBReweighter）、sPlot 与加速推理的 Bonsai BDT。估计器与 scikit-learn 兼容，支持 Python 3.9-3.13 与 Linux/macOS/Windows，通过 pip 安装；运行示例可能需要额外安装 ROOT 和 uproot。采用 Apache 2.0 许可。

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

- 均匀分类器 uBoost / UGradientBoosting（含 FlatnessLoss）
- 多维分布重加权 GBReweighter 与 sPlot 实现
- 估计器与 scikit-learn 兼容
- Bonsai BDT 用于快速分类推理

## 适用场景

- 粒子物理分析中训练与质量变量低相关的分类器
- 对仿真样本做多维分布重加权以匹配真实数据
- 构建推理速度更快的 BDT 模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **hep_ml** provides specific machine learning tools for purposes of high energy physics.
> L18: * uniform classifiers - the classifiers with low correlation of predictions and mass (or some other variable, or ev

## 星数曲线

```mermaid
xychart-beta
    title "arogozhnikov/hep_ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 198 --> 200
    line [199, 199]
```

2026-10-18 199 → 2026-10-28 199（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e4889e1ee1d9` · [字段定义](../../DATASET.md)*
