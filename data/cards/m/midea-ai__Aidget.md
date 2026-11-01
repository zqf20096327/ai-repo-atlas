# midea-ai/Aidget

⭐ 186 · Python · Apache-2.0 · 推送 2026-10-31 · [GitHub](https://github.com/midea-ai/Aidget) · 组织维护 · 中文 README

**面向边端 MCU/RTOS 的推理引擎与模型转换工具链**

美的集团开发的边缘推理引擎，将固定形状 TFLite 模型转换为模型专属 C 程序，运行于 CPU 与 MCU。模型准备在主机端完成，设备端以直接 C 调用执行，内存由应用控制；支持 FP32、INT8 及混合算子数值路径，可选 Arm NEON、CMSIS-NN、ESP-NN 加速。已在美的空调、冰箱、扫地机器人等智能家电量产中使用。本仓库以源码形式提供推理运行时与模型转换工具链，运行时为 C，Python 3.10+ 用于转换流程，许可证 Apache-2.0。

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

- TFLite 固定形状模型转换为模型专属 C 程序
- 支持 FP32/INT8/混合算子与 Arm NEON、CMSIS-NN、ESP-NN 加速
- 应用控制内存的静态执行与内存规划
- 提供 ESP32-S3 与 Raspberry Pi Zero W 上的延迟/内存/代码体积基准数据

## 适用场景

- 在 MCU/RTOS 等资源受限设备上部署 TFLite 模型
- 对比 TFLM、TVM、ncnn 等方案在 ESP32 上的推理性能
- 将推理代码以源码或静态/共享库形式嵌入家电等嵌入式产品

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L15: Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute a
> L19: The engine converts fixed-shape TFLite models into model-specific C programs for CPUs and MCUs. Model preparation r


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `068d42bc40b1` · [字段定义](../../DATASET.md)*
