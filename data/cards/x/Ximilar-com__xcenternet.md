# Ximilar-com/xcenternet

⭐ 160 · Python · MIT · 推送 2025-12-04 · [GitHub](https://github.com/Ximilar-com/xcenternet) · 组织维护

**TensorFlow 2 实现的 CenterNet/TTFNet 无锚框目标检测库**

基于 tf.keras 的 CenterNet（Objects as Points）与 TTFNet 修改实现，用 tf.data.Dataset 训练，支持 EfficientNet/ResNet 骨干、多尺度训练、可变形卷积与自定义数据集微调（mscoco 格式）。提供在 Pascal VOC 与 MSCOCO 上训练的预训练模型下载与 TensorBoard 日志，含 train/eval/predict 脚本。安装需克隆仓库、装 TensorFlow 2.4+ 及 tf-image、tf-addons 等依赖，可变形卷积需从特定分支安装；含 Cython 代码需编译。仅做 2D 目标检测，不含姿态估计或 3D。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CenterNet/TTFNet 的 tf.keras 实现，支持 ResNet/EfficientNet 骨干
- 可变形卷积支持及对应预训练模型
- mscoco 格式自定义数据集训练/微调，多 GPU 训练
- 提供预训练模型下载与 TensorBoard 训练日志

## 适用场景

- 在自有数据集上训练/微调目标检测模型
- 使用预训练模型对单张图片做检测预测
- 复现论文在 Pascal VOC/MSCOCO 上的训练与评估

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: Modified **TensorFlow 2.4+** (or 2.2 if you use XCenterNet tagged as v1.0.0) tf.keras implementation of **CenterNet*
> L10: * Added *stronger* NMS for better results

## 星数曲线

```mermaid
xychart-beta
    title "Ximilar-com/xcenternet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 159 --> 161
    line [160, 160]
```

2026-10-18 160 → 2026-10-30 160（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `284e996ab4a2` · [字段定义](../../DATASET.md)*
