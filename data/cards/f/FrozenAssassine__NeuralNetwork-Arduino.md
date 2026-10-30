# FrozenAssassine/NeuralNetwork-Arduino

⭐ 15 · C++ · 推送 2026-01-05 · [GitHub](https://github.com/FrozenAssassine/NeuralNetwork-Arduino) · [官网](https://medium.com/@FrozenAssassine/neural-network-from-scratch-on-esp32-2a53a7b65f9f) · 个人维护

**在 ESP32/Arduino 上运行神经网络的轻量 C++ 库**

面向微控制器的轻量神经网络库：提供设备端训练与仅推理两种模式。推理模式通过 Python 脚本将已有 PyTorch 模型转换为头文件加载到 ESP32 或 Arduino；也可直接在芯片上训练（暂不支持权重保存），但较大模型会受内存限制。支持 Softmax/Sigmoid/Relu/TanH/LeakyRelu 激活函数与 Xavier 初始化，OOP 结构（BaseLayer 继承）便于扩展层类型。通过 PlatformIO 克隆项目并上传代码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 模型经 Python 脚本转换为头文件供 ESP32/Arduino 推理
- 支持设备端训练（暂无权重保存功能）
- 提供 Softmax/Sigmoid/Relu/TanH/LeakyRelu 激活函数与 Xavier 初始化
- 基于 BaseLayer 继承的 OOP 层结构，便于新增层类型

## 适用场景

- 在 ESP32/Arduino 上部署 PyTorch 训练好的模型做推理
- 资源受限设备上直接训练简单网络（如 XOR）
- 简单机器人或传感器项目中的轻量预测任务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: This project is a lightweight neural network implementation designed to run on microcontrollers like the **ESP32** a
> L7: The project has two supported modes, inference and training mode. Inference mode uses an existing torch model and co

## 星数曲线

```mermaid
xychart-beta
    title "FrozenAssassine/NeuralNetwork-Arduino 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `badd658899de` · [字段定义](../../DATASET.md)*
