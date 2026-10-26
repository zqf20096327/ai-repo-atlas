# IRCVLab/Depth-Anything-for-Jetson-Orin

⭐ 72 · Python · 推送 2025-11-10 · [GitHub](https://github.com/IRCVLab/Depth-Anything-for-Jetson-Orin) · 组织维护

**面向 Jetson Orin 的实时单目深度估计方案**

将 Depth-Anything-Small 模型部署到 NVIDIA Jetson Orin(8GB) 上，通过 TensorRT 引擎加速，处理 CSI 摄像头实时画面输出深度图。流程为：从 HuggingFace 拉取权重导出 ONNX 与 TensorRT 引擎（需联网），之后离线运行摄像头流与深度估计。限制：当前仅支持 CSI 相机（改代码可支持 USB 相机）；Base/Large 模型因内存不足不支持；输入尺寸须能被 14 整除。附有各输入尺寸的推理耗时与内存占用实测数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorRT 引擎加速的实时深度估计（518x518 输入 98ms，308x308 输入 23.5ms）
- 导出权重后无需网络即可离线推理
- 提供 Camera 流式封装与 DepthEngine 少量代码即用的接口
- 附 Jetson Orin(8GB) 上的推理时间与显存占用实测表

## 适用场景

- 在 Jetson Orin 上跑实时单目深度估计
- 为机器人/自动驾驶/AR 原型提供深度感知输入
- 在边缘设备上验证 Depth-Anything-Small 的性能指标

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project aims to provide a real-time depth estimation optimized for NVIDIA Jetson Orin devices. Utilizing the po
> L16: - NVIDIA Jetson Orin Developer Kit(8GB)

## 星数曲线

```mermaid
xychart-beta
    title "IRCVLab/Depth-Anything-for-Jetson-Orin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-26 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e11a0b82bcba` · [字段定义](../../DATASET.md)*
