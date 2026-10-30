# jianqingzheng/res_aligner_net

⭐ 35 · Python · Apache-2.0 · 推送 2026-02-11 · [GitHub](https://github.com/jianqingzheng/res_aligner_net) · [官网](https://jianqingzheng.github.io/res_aligner_net/) · 组织维护

**医学图像不连续形变配准的深度学习训练与推理实现**

Medical Image Analysis 2024 论文 RAN（Residual Aligner-based Network）的官方代码，基于 TensorFlow/Keras 实现训练与推理流水线。针对多器官不连续形变对齐问题，提出量化指标 Motion Separability、运动可分离主干结构（优化的空洞卷积）与 Residual Aligner 模块（RAM），在公开腹部与肺部 CT 数据上执行由粗到细的无监督配准。安装方式为 git clone 源码并 pip 安装指定版本依赖（tensorflow 2.3.1 等），提供数据下载/预处理、训练（README 标注训练时长大于一周）与推理脚本，并附 Colab demo 与用户手册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提出量化指标 Motion Separability 度量器官不连续形变预测能力
- Motion-Separable 多尺度主干结构配合 Residual Aligner 模块（RAM）
- 在公开腹部与肺部 CT 数据上的无监督由粗到细配准流水线
- 提供 Colab demo、notebook 与用户手册

## 适用场景

- 复现论文中的腹部/肺部 CT 不连续形变配准实验
- 在自有医学影像数据上训练 RAN 模型进行形变配准
- 基于 Motion Separability 指标评估配准网络

## 场景标签

 · 领域:医学图像分析/图像配准

## 证据(README 行号)

> L15: > This repo provides an implementation of the training and inference pipeline of RAN based on TensorFlow and Keras.
> L25: To verify the validity of this quantitative metric as well as the accuracy and efficiency of our method, a series o

## 星数曲线

```mermaid
xychart-beta
    title "jianqingzheng/res_aligner_net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d61c99def851` · [字段定义](../../DATASET.md)*
