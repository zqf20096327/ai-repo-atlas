# kraiskil/onnx2c

⭐ 422 · C · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/kraiskil/onnx2c) · 个人维护

**面向微控制器的 ONNX 转 C 编译器：把神经网络编译成单个 C 文件**

onnx2c 读取 ONNX 模型文件，生成可嵌入项目的 C 代码，目标场景是微控制器上的 TinyML 推理。生成的代码不依赖 stdio、无动态内存分配、编译期分配缓冲区、除标准 C 数学库外无库依赖，输出为单个 C 文件。目前 166 个 ONNX 算子中 91 个至少部分实现，不支持加速器和训练反向传播。通过 git clone 加 CMake 从源码构建，需系统安装 ProtocolBuffers；支持 float16/bfloat16 映射为 _Float16/__bf16，并提供张量 union 化、去 Cast 节点、AVR 常量放入指令存储等优化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX 模型编译为单个自包含 C 文件，仅依赖标准 C 数学库
- 无动态内存分配、无 stdio 依赖，适配微控制器资源限制
- 支持 float16/bfloat16（映射 _Float16/__bf16）与 AVR 常量优化
- 包含在 MCU 开发板上初步运行 .onnx 的辅助脚本

## 适用场景

- 把已训练的神经网络（PyTorch/TensorFlow 导出的 ONNX）部署到 MCU 项目
- 设计网络阶段验证模型是否适配目标硬件
- 嵌入式产品中做本地推理而不引入推理框架运行时

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Onnx2c is a ONNX to C compiler. It will read an ONNX file,
> L6: Onnx2c's target is "Tiny ML", meaning running the inference on microcontrollers. To make this
> L16: neural network to an ONNX file (e.g. PyTorch and Tensorflow both can) and you have a working microcontroller

## 星数曲线

```mermaid
xychart-beta
    title "kraiskil/onnx2c 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 420 --> 423
    line [421, 422, 422]
```

2026-10-18 421 → 2026-10-27 422（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `564a07298c32` · [字段定义](../../DATASET.md)*
