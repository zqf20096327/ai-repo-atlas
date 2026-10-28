# SamirAbouHaidar/HARP-NeXt

⭐ 23 · Python · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/SamirAbouHaidar/HARP-NeXt) · 组织维护

**面向机器人与嵌入式系统的 3D LiDAR 语义分割网络（IROS 2025）**

HARP-NeXt 是一个用于 3D LiDAR 点云语义分割的深度学习网络，IROS 2025 论文的官方实现。提出降低计算开销的预处理方法、Conv-SE-NeXt 特征提取块与多尺度 range-point 融合骨干网络；在 nuScenes 与 SemanticKITTI 基准上提供预训练权重（Hugging Face 可下载），RTX 4090 上达 100 FPS，Jetson AGX Orin 上接近实时。面向机器人/自动驾驶研究者的 Python 实现，提供训练与评测命令及 conda/venv 安装流程，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多尺度 range-point 融合骨干与 Conv-SE-NeXt 特征提取块
- nuScenes / SemanticKITTI 预训练权重可下载评测
- 提供桌面（conda + CUDA 11.8）与 Jetson（JetPack 6.0）两条安装路径
- RTX 4090 上 100 FPS，Jetson AGX Orin 嵌入式平台可近实时运行

## 适用场景

- 在 nuScenes 或 SemanticKITTI 上评测/复现 3D 语义分割结果
- 在 Jetson 嵌入式平台上部署实时 LiDAR 分割
- 基于官方权重对自己的 LiDAR 点云数据做微调训练

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L27: This is the official repo of **HARP-NeXt**, a High-Speed and Accurate Range-Point Fusion Network for 3D LiDAR Seman
> L40: HARP-NeXt achieves high accuracy in real-time on the RTX 4090 GPU at 100 FPS, while delivering near real-time perfo

## 星数曲线

```mermaid
xychart-beta
    title "SamirAbouHaidar/HARP-NeXt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `898cc4f919a6` · [字段定义](../../DATASET.md)*
