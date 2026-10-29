# Qengineering/RPi-Bullseye-DNN-image

⭐ 30 · BSD-3-Clause · 推送 2026-07-23 · [GitHub](https://github.com/Qengineering/RPi-Bullseye-DNN-image) · [官网](https://qengineering.eu/deep-learning-examples-on-raspberry-32-64-os.html) · 个人维护

**预装深度学习框架与示例的树莓派 4 Bullseye 64 位 SD 镜像**

面向 Raspberry Pi 4 的 Bullseye 64 位操作系统 SD 卡镜像（约 4GB，需 32GB 卡），预装 OpenCV 4.7.0、TensorFlow/Lite 2.10.0、PyTorch 1.13.0、ncnn、MNN、Paddle/Paddle-Lite 等 10 个深度学习框架，并内置分类、SSD、分割、姿态估计、人脸检测识别、YoloV5/YoloX、PaddleOCR 等 C++ 示例。默认超频至 1850 MHz，未启用 WiFi（默认密码 3.14）。镜像可通过 Imager 或 balenaEtcher 烧录安装。另附 TensorFlow-Lite 单包打包、摄像头接入（Gstreamer/LVVC）与 OpenCV+TensorFlow 导入冲突的说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预装 OpenCV/TensorFlow/PyTorch/ncnn/MNN/Paddle 等 10 个框架
- 内置分类、检测、分割、姿态、人脸识别、OCR 等 C++ 示例
- 默认超频 1850 MHz，含 Gstreamer/LVVC 摄像头接入示例
- 将 TensorFlow-Lite 分散库打包为单一 C++ 库包

## 适用场景

- 树莓派上快速获得可运行的深度学习开发环境，免去逐个编译框架
- 在 Pi 4 上运行目标检测、人脸识别、姿态估计等 C++ 示例
- 学习嵌入式设备上多框架部署与摄像头流接入

## 场景标签

`目标检测` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L44: ## Pre-installed frameworks.
> L46: Clicking on the links below will direct you to our installation guide.

## 星数曲线

```mermaid
xychart-beta
    title "Qengineering/RPi-Bullseye-DNN-image 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `02de5326a917` · [字段定义](../../DATASET.md)*
