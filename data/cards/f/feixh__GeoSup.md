# feixh/GeoSup

⭐ 30 · Python · 推送 2026-07-17 · [GitHub](https://github.com/feixh/GeoSup) · 组织维护

**ICRA 2019 论文官方代码：几何监督的单目深度预测**

UCLA Vision Lab 发布的 Geo-Supervised Visual Depth Prediction 研究代码，配套 VISMA2 数据集（单目视频 VGA@30Hz、惯性测量 400Hz、深度流）。代码基于 Yin 等人的 GeoNet 模型改造，仅保留深度预测部分，通过语义信息几何损失（SIGL）正则化训练，支持用实验室 VIO 系统估计的位姿替代位姿网络。README 覆盖数据解析（需 ROS）、PSPNet 分割掩码生成、训练与可视化对比流程，无打包发布。

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

- 基于 GeoNet 改造的单目深度预测训练代码，SIGL 损失可选启用
- 配套发布 VISMA2 数据集（视频+惯性+深度+VIO 轨迹）
- 支持以 VIO 位姿替代位姿网络训练
- 提供基线与本文方法的深度预测结果对比可视化脚本

## 适用场景

- 复现 ICRA 2019 论文的深度预测实验
- 在 VISMA2 数据集上训练视觉-惯性深度预测模型
- 研究几何监督信号（重力/位姿）对深度估计的作用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Geo-Supervised Visual Depth Prediction
> L58: - `use_sigl`: If set, impose the *semantically informed geometric loss (SIGL)* to the baseline model.
> L64: Note, the code is built on top of the GeoNet model of Yin *et al.* which jointly estimates depth and flow, but we o

## 星数曲线

```mermaid
xychart-beta
    title "feixh/GeoSup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `96424c86694a` · [字段定义](../../DATASET.md)*
