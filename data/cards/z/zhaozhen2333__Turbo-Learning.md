# zhaozhen2333/Turbo-Learning

⭐ 30 · Python · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/zhaozhen2333/Turbo-Learning) · [官网](https://arxiv.org/abs/2606.12371) · 组织维护 · 中文 README

**无需训练的检测-分割迭代精化推理策略（CVIU 2026 官方实现）**

论文“A Turbo-Inference Strategy for Object Detection and Instance Segmentation”(CVIU 2026) 的官方实现：在推理阶段闭合检测与实例分割的单向流水线，将粗糙实例掩码的前景信息回传以精化边界框与分数，再复用预训练掩码头预测更精细的掩码。无需重训权重，以 MaskBoxRefiner 模块插入 MMDetection 3.3.0 的 RoI 头，覆盖 Mask R-CNN、Cascade/HTC、QueryInst/Sparse R-CNN、RTMDet-Ins 四类模型，并提供 18 个预训练权重链接。代价是以推理速度换精度（FPS 下降）。面向计算机视觉研究者与 MMDetection 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练无关：全部精化在推理阶段完成，可复用现有预训练权重
- MaskBoxRefiner 即插即用模块，从 RoI 头配置启用
- 覆盖 Mask R-CNN/Cascade/HTC/QueryInst/Sparse R-CNN/RTMDet-Ins 四类模型族
- 在 COCO 2017 全部 5,000 张验证图上复现结果，附 Checkpoint SHA-256

## 适用场景

- 在已有 MMDetection 实例分割模型上免费提升 bbox AP 与 mask AP
- 复现论文在 COCO 上的评测结果
- 与研究型训练无关方法（如 Soft-NMS）叠加组合后处理

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L19: > **Official implementation** of “A Turbo-Inference Strategy for Object Detection and Instance Segmentation,” publi
> L27: The method is **training-free**, reuses the pretrained mask head, and can be attached to existing top-down instance
> L121: This repository is built on MMDetection 3.3.0. A typical installation is:

## 星数曲线

```mermaid
xychart-beta
    title "zhaozhen2333/Turbo-Learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a1dc9235870f` · [字段定义](../../DATASET.md)*
