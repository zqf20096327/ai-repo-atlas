# matteocarnelos/microflow-rs

⭐ 195 · Rust · Apache-2.0 · 推送 2026-05-26 · [GitHub](https://github.com/matteocarnelos/microflow-rs) · 个人维护

**面向 MCU 的 Rust TinyML 推理引擎，运行 TFLite 模型**

由 Matteo Carnelos 在帕多瓦大学与 Grepit AB 合作开发的 TinyML 推理引擎，含两部分：编译器（microflow-macros crate）在 Rust 编译前解析并预处理 TensorFlow Lite 模型、生成源码；运行时（microflow crate）为 no_std 组件，运行在目标 MCU 上，实现算子、激活函数与量化。用户通过 Rust 过程宏将模型附到 struct 上，编译器生成 predict() 方法供调用推理。当前支持 FullyConnected、Conv2D 等算子与 ReLU/Softmax 等激活函数，已在 ESP32、Cortex-M 系列、ATmega328 等 5 种 MCU 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编译期解析 .tflite 模型并生成 predict() 方法的 Rust 过程宏接口
- no_std 运行时可部署于 8/32 位 MCU（含 ATmega328、ESP32）
- 支持量化的 Conv2D/FullyConnected 等算子与 ReLU/Softmax 激活函数
- 随附正弦预测、语音命令识别、人体检测三个测试模型

## 适用场景

- 在资源受限的嵌入式设备上运行量化神经网络推理
- 用 Rust 过程宏把 TFLite 模型编译进固件
- 在多种主流 MCU 上部署 TinyML 应用

## 场景标签

 · 领域:嵌入式机器学习/物联网

## 证据(README 行号)

> L4: MicroFlow is a robust and efficient TinyML inference engine designed for deploying machine learning models on embedd
> L19: On the other hand, the runtime is a `[no_std]` component designed to run on the target MCU.
> L25: By applying the `model` macro to a `struct` and providing the model's path, the MicroFlow compiler generates a `pre

## 星数曲线

```mermaid
xychart-beta
    title "matteocarnelos/microflow-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 194 --> 196
    line [195, 195]
```

2026-10-18 195 → 2026-10-22 195（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1ca3617d2c9d` · [字段定义](../../DATASET.md)*
