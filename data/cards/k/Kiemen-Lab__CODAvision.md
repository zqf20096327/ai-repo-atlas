# Kiemen-Lab/CODAvision

⭐ 21 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/Kiemen-Lab/CODAvision) · [官网](https://www.nature.com/articles/s41596-026-01404-3) · 组织维护

**面向生物医学图像的语义分割标注与训练工具**

开源 Python 包，提供 GUI 引导的语义分割工作流：读取 CT、MRI、组织学等生物医学图像，结合外部标注工具（Aperio ImageScope 或 QuPath，后者需将 GeoJSON 注释转换为 XML）生成标注数据集，训练并运行分割模型。基于 TensorFlow/Keras 与 PyTorch（DeepLabV3+、UNet），支持插件式添加自定义模型架构并自动接入 GUI 与训练管线。安装走 conda 环境 + pip，Windows/Linux 需 CUDA 与 NVIDIA GPU（≥8 GB VRAM），Apple Silicon 支持 Metal 加速。附 Nature Protocols 协议与示例数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GUI 引导的生物医学图像语义分割工作流（训练+处理）
- 插件式模型架构，支持 TensorFlow/Keras 与 PyTorch 多框架注册
- 兼容 Aperio ImageScope 与 QuPath 标注（提供 GeoJSON2XML 转换路径）
- 跨平台支持：Windows/Linux（CUDA）与 Apple Silicon（Metal）

## 适用场景

- 我对组织学/CT/MRI 图像做语义分割并训练自己的模型
- 我想在 GUI 里完成从标注数据准备到模型训练的全流程
- 我需要在 Mac（Apple Silicon）上跑生物医学图像分割

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: CODAvision is an open-source Python package designed for semantic segmentation of biomedical images through a user-f
> L150: - TensorFlow/Keras models (DeepLabV3+, UNet)

## 星数曲线

```mermaid
xychart-beta
    title "Kiemen-Lab/CODAvision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ffb927ca8c0b` · [字段定义](../../DATASET.md)*
