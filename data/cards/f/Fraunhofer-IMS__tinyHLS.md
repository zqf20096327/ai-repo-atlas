# Fraunhofer-IMS/tinyHLS

⭐ 15 · Python · NOASSERTION · 推送 2026-07-20 · [GitHub](https://github.com/Fraunhofer-IMS/tinyHLS) · [官网](https://fraunhofer-ims.github.io/tinyHLS/) · 组织维护

**将 Keras 神经网络编译为可综合 Verilog 协处理器的 HLS 工具**

Fraunhofer IMS 开发的紧凑型硬件编译器：读取 tensorflow.keras 神经网络，翻译为平台无关的专用协处理器，输出完全可综合的 Verilog HDL 代码，并以 AHB-lite 接口封装便于集成到自定义处理器系统（如 RISC-V）。当前支持 conv1D、maxpool1D、globalaveragepool1D、dense 层及 linear/ReLU 激活，conv1D 可选资源优化或性能优化版本。工具处于活跃开发中，功能将持续扩展。以 conda 环境安装 Python 包方式使用，另提供 PPG/ECG 生物信号示例与 PyTorch 配合的变通方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- tensorflow.keras 模型到可综合 Verilog HDL 的自动翻译
- 协处理器带 AHB-lite 接口，可集成到自定义处理器系统
- 支持 conv1D/maxpool1D/globalaveragepool1D/dense 层与 linear/ReLU 激活
- conv1D 层提供资源高效与性能优化两种配置

## 适用场景

- 将 1D CNN 模型部署为嵌入式/边缘硬件加速器
- 为自定义处理器系统生成神经网络协处理器 IP
- 在 PPG/ECG 生物信号数据集上演示模型到 HDL 的流程

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: **tinyHLS** is a compact hardware compiler developed by Fraunhofer IMS. It processes tensorflow.keras
> L10: neural networks and translates them into a dedicated co-processor unit. The generated outputs are platform
> L11: independent and consist entirely of synthesizable Verilog HDL code. The co-processor is wrapped with a

## 星数曲线

```mermaid
xychart-beta
    title "Fraunhofer-IMS/tinyHLS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c7f80602f5b5` · [字段定义](../../DATASET.md)*
