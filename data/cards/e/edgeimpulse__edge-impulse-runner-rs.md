# edgeimpulse/edge-impulse-runner-rs

⭐ 15 · Rust · BSD-3-Clause-Clear · 推送 2026-09-08 · [GitHub](https://github.com/edgeimpulse/edge-impulse-runner-rs) · [官网](https://edgeimpulse.com) · 组织维护

**Rust 库：在 Linux/macOS 上运行 Edge Impulse 模型**

提供 FFI 与 EIM 两种模式的 Rust 推理库：FFI 模式（默认）通过 C++ SDK 直接调用运行分类、目标检测与视觉异常检测模型，支持摄像头/麦克风/加速度计等多种传感器输入与连续分类；EIM 模式仅作向后兼容。模型可通过 EI_MODEL 本地路径或 Edge Impulse Studio 凭据下载获取，支持 aarch64 交叉编译（Docker）、多平台目标及 TVM/ONNX/QNN 等加速后端构建标志。同时提供向 Edge Impulse 项目上传训练/测试数据的接口。面向在嵌入式与边缘设备上集成 Edge Impulse 模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | BSD-3-Clause-Clear |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FFI 默认模式直接调用 Edge Impulse C++ SDK 推理
- 支持分类/目标检测/视觉异常检测与多类传感器输入
- Docker 辅助 aarch64 交叉编译，覆盖树莓派/Jetson 等 ARM64 设备
- TVM/ONNX Runtime/QNN/Ethos-U/Akida 等后端构建标志

## 适用场景

- 在 Linux/macOS 或 ARM 边缘设备上嵌入 Edge Impulse 模型推理
- 从摄像头、麦克风或传感器流做连续分类
- 将训练/测试/异常数据上传到 Edge Impulse 项目
- 针对 Jetson、Qualcomm 等硬件选择加速后端构建

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: This Rust library provides two modes for running Edge Impulse models:
> L16: - Run Edge Impulse models on Linux and MacOS
> L275: - **Default (TensorFlow Lite Micro):**

## 星数曲线

```mermaid
xychart-beta
    title "edgeimpulse/edge-impulse-runner-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `7ea37b1b58cf` · [字段定义](../../DATASET.md)*
