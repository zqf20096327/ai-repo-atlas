# edwardyehuang/iSeg

⭐ 18 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/edwardyehuang/iSeg) · 个人维护

**Keras 3 语义分割库：多种 backbone 与预训练权重开箱可用**

基于 Keras 3 的语义分割库（当前仅支持 TensorFlow 后端，PyTorch/JAX 后端待发布），提供现代 ResNet、ConvNeXt、Swin Transformer、InternImage、EVA02、MOAT 等十余种 backbone，backbone 均不依赖固定输入尺寸，并提供可下载的预训练权重。支持混合精度训练与推理、确定性结果、最多 8 GPU 训练与推理、TPU/TPU Pod 训练、Windows 10/11 与 WSL2、Apple M1 macOS。要求 TensorFlow >= 2.10，通过 Conda 环境安装。

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

- 十余种 backbone（ResNet/ConvNeXt/Swin/InternImage/EVA02 等），输入尺寸无关
- 混合精度训练与推理（Volta 及之后 GPU 架构）
- 支持最多 8 GPU 及 TPU/TPU Pod 训练
- 预训练 backbone 权重可下载

## 适用场景

- 用现成 backbone 搭建并训练语义分割模型
- 加载预训练权重做图像分割推理
- 在 TPU/GPU 集群上训练分割任务

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: ## iSeg : A Keras 3 ~~TensorFlow 2~~ Library for Semantic Segmentation
> L40: - [x] Modern ResNet

## 星数曲线

```mermaid
xychart-beta
    title "edwardyehuang/iSeg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `63a8eae91dd1` · [字段定义](../../DATASET.md)*
