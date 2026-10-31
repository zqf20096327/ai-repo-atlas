# ahmed-ramsey-shahin/deep-learning-accelerator

⭐ 16 · SystemVerilog · 推送 2025-12-10 · [GitHub](https://github.com/ahmed-ramsey-shahin/deep-learning-accelerator) · 个人维护

**SystemVerilog 神经网络推理加速器：脉动阵列矩阵乘单元**

以 SystemVerilog/Verilog 实现的深度学习硬件加速器 RTL 设计，面向神经网络推理。核心为脉动阵列矩阵乘单元，配套处理元件（PE）、Carry Save 与 Wallace Tree 乘法器、统一缓冲、权重 FIFO、脉动数据排布模块，以及 ReLU/Sigmoid/Softmax/Tanh 激活函数模块。PE 默认 8 位数据宽度与 32 位累加器宽度。README 给出各模块的参数、输入输出与功能说明及项目结构，未提供安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 脉动阵列矩阵乘单元与配套 PE 数据流设计
- Carry Save 与 8x8 Wallace Tree 两种乘法器实现
- 统一缓冲、权重 FIFO 与脉动数据排布模块
- ReLU/Sigmoid/Softmax/Tanh 四种激活函数硬件模块

## 适用场景

- 学习 TPU 式脉动阵列加速器的 RTL 设计
- 作为数字 IC 设计课程或研究的教学参考实现
- 在 FPGA/ASIC 流程中复用矩阵乘与乘法器组件

## 场景标签

 · 领域:硬件/芯片设计

## 证据(README 行号)

> L1: # Deep Learning Hardware Accelerator
> L3: A hardware implementation of a deep learning accelerator using SystemVerilog/Verilog, designed for efficient neural 

## 星数曲线

```mermaid
xychart-beta
    title "ahmed-ramsey-shahin/deep-learning-accelerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fd2bec8b863d` · [字段定义](../../DATASET.md)*
