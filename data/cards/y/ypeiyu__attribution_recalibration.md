# ypeiyu/attribution_recalibration

⭐ 34 · Python · 推送 2026-01-21 · [GitHub](https://github.com/ypeiyu/attribution_recalibration) · [官网](https://openreview.net/forum?id=WUWJIV2Yxtp) · 个人维护

**面向模型解释的特征归因重校准算法实现（ICLR 2023 Spotlight）**

论文 Re-calibrating Feature Attributions for Model Interpretation 的官方代码实现：针对路径积分类归因方法依赖取绝对值导致与理论前提矛盾的问题，通过计算合适的参考点进行重校准，可嵌入现有基于积分的归因方法。实现收录 InputGrad、GradCAM、SmoothGrad、IG、EG、AGI 等 13 种归因方法，通过 python main.py 对 ImageNet 等数据集与预训练模型运行可视化与定量评估。依赖 Python 3.9 与 PyTorch 1.12，需自行准备数据集与模型后从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 ICLR 2023 spotlight 论文的归因重校准算法
- 收录 13 种梯度/积分类特征归因方法
- 支持可视化与 DiffID 等定量评估指标

## 适用场景

- 研究人员复现论文中的归因重校准实验
- 对比多种积分类归因方法在 ImageNet 上的表现
- 将重校准方案嵌入自有积分归因流程

## 场景标签

 · 领域:机器学习可解释性

## 证据(README 行号)

> L4: This code implements attribution re-calibration algorithm from the following paper:
> L11: Due to its desirable theoretical properties, path integration is a widely used scheme for feature attribution to in

## 星数曲线

```mermaid
xychart-beta
    title "ypeiyu/attribution_recalibration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eb7e156521d4` · [字段定义](../../DATASET.md)*
