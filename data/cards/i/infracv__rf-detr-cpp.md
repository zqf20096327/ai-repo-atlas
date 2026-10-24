# infracv/rf-detr-cpp

⭐ 207 · C++ · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/infracv/rf-detr-cpp) · [官网](https://infracv.com) · 组织维护

**面向生产部署的 RF-DETR C++/TensorRT 推理引擎**

为 Roboflow 的 RF-DETR（DINOv2 backbone 的 DETR 式检测模型）提供纯 C++/TensorRT 推理引擎，覆盖目标检测（nano-large）与实例分割（seg-nano 至 seg-2xlarge），运行时零 Python 依赖。预处理用 GPU CUDA kernel，主机到设备传输为异步 pinned memory，推理调度用 CUDA Graph replay，支持 FP32/FP16/INT8 三种精度，面向 NVIDIA GPU（CC≥8.0）与 Jetson（Orin/Thor/GH200）优化。模型转换需一次性 Python 步骤；另提供 C ABI 供 Python/Rust/Go FFI 调用。限制：仅支持 NVIDIA 硬件，FP16 存在 attention 数值溢出产生 NaN 的已知风险，需回退 FP32。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测与实例分割的 C++17/TensorRT 实现，运行时零 Python 依赖
- FP32/FP16/INT8 三种精度，INT8 经 QDQ ONNX 校准
- GPU CUDA 预处理 kernel、异步 pinned memory 传输、CUDA Graph replay
- C ABI（librfdetr_c.so）支持 Python/Rust/Go FFI 调用

## 适用场景

- 在 NVIDIA GPU/Jetson 上以低延迟部署 RF-DETR 检测或分割
- 去掉推理时的 Python/PyTorch 依赖做生产环境部署
- 在 C++/Rust/Go 项目中通过 C ABI 集成检测能力

## 场景标签

`目标检测` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L18: **RF-DETR C++** is a production-grade TensorRT inference engine for RF-DETR, Roboflow's transformer-based real-time
> L24: rfdetr::Detections dets = detector.detect(cv::imread("image.jpg"), 0.5f);

## 星数曲线

```mermaid
xychart-beta
    title "infracv/rf-detr-cpp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 205 --> 208
    line [206, 207, 207]
```

2026-10-18 206 → 2026-10-24 207（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e70acbdea60c` · [字段定义](../../DATASET.md)*
