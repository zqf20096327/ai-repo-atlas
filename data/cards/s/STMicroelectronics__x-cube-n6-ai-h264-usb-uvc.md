# STMicroelectronics/x-cube-n6-ai-h264-usb-uvc

⭐ 15 · C · NOASSERTION · 推送 2026-09-09 · [GitHub](https://github.com/STMicroelectronics/x-cube-n6-ai-h264-usb-uvc) · 组织维护

**STM32N6 上的人体检测演示固件：NPU 推理 + H264 UVC 推流**

意法半导体官方发布的 STM32Cube 扩展应用包，在 STM32N6570-DK 开发板上演示完整视觉流水线：摄像头采集、在 NPU 上运行量化目标检测模型（人体检测，输出带置信度的矩形框）、H264 编码后经 USB UVC 推流到主机摄像头应用。支持 4 种摄像头模块与 720p/480p@30fps，FreeRTOS 多线程，需用 STM32CubeIDE/IAR/Makefile 交叉编译并烧录到外部 Flash，或直接使用预编译 hex。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NPU 加速的量化目标检测模型推理（人体检测）
- DCMIPP 双管道、裁剪/抽取/缩放与 ISP 处理
- H264 编码 + USB UVC（Azure RTOS USBX）推流到主机
- 提供预编译二进制与 STM32CubeIDE/IAR/Makefile 三种构建方式

## 适用场景

- 在 STM32N6570-DK 上学习端侧 AI 推理与 NPU 部署
- 参考摄像头采集→检测→编码→USB 推流的嵌入式流水线实现
- 评估 STM32N6 平台的边缘视觉应用能力

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Computer Vision application demonstrating the deployment of object detection models on the STM32N6570-DK board and s
> L22: - NPU accelerated quantized AI model inference
> L89: 7. Detected people are surrounded by a rectangle with the associated confidence level.

## 星数曲线

```mermaid
xychart-beta
    title "STMicroelectronics/x-cube-n6-ai-h264-usb-uvc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a65ed1438e9b` · [字段定义](../../DATASET.md)*
