# djene-mengistu/UAPS

⭐ 14 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/djene-mengistu/UAPS) · 个人维护

**半监督缺陷分割研究代码：不确定性引导伪标签训练**

论文《Uncertainty-aware and dynamically-mixed pseudo-labels for semi-supervised defect segmentation》(Computers in Industry) 的官方实现。方法：基于共享编码器与多解码器，对编码器输出施加扰动生成多路预测，随机权重动态混合生成伪标签，以解码器预测与平均预测的 KL 距离作为不确定性，引导伪标签监督与一致性正则。支持 NEU-Seg、DAGM、MTiles、KolektorSDD2 四个数据集，提供各对比网络的训练与测试脚本，基线架构为 U-Net 加扰动模块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多解码器动态混合预测生成伪标签
- KL 距离不确定性估计引导训练与正则
- 覆盖 4 个公开缺陷分割数据集与多个对比方法实现
- 基线为 U-Net 加扰动模块

## 适用场景

- 复现论文的半监督缺陷分割实验
- 在钢材/磁瓦等工业缺陷数据上训练分割模型
- 作为伪标签不确定性估计方法的参考实现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Uncertainty-aware and Dynamically-mixed Pseudo-labels for Semi-supervised Defect Segmentation (UAPS)
> L3: In this study, we propose a novel uncertainty-aware pseudo labels, which are generated from dynamically mixed predic
> L26: **Fig. 2:** Illustration of the overall framework of the UAPS using the unlabeled samples. We apply various perturb

## 星数曲线

```mermaid
xychart-beta
    title "djene-mengistu/UAPS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3f90a5df4621` · [字段定义](../../DATASET.md)*
