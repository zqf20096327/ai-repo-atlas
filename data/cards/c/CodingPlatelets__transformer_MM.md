# CodingPlatelets/transformer_MM

⭐ 15 · Scala · LGPL-3.0 · 推送 2026-07-16 · [GitHub](https://github.com/CodingPlatelets/transformer_MM) · 组织维护 · 中文 README

**用 Chisel3 编写的 Transformer LLM 硬件加速器设计**

以 Chisel HDL 实现的面向大语言模型推理的硬件加速器 RTL 设计：包含定点/浮点（IEEE-754）处理单元、脉动阵列 GEMM/GEMV、基于 I-BERT 算法的定点 Softmax、注意力机制组件（Q/K 生成、Scores×Value 计算）、自定义 SRAM 与 HBM/DRAM/AXI 存储接口，顶层 VitisRTLKernel 用于 Xilinx FPGA 平台集成，并含 LLaMA 3 架构的注意力层与矩阵控制器实现。部分稀疏矩阵组件已标记废弃但保留兼容。通过 sbt + ChiselTest 运行验证，面向硬件开发与科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 脉动阵列 GEMM：n×n 矩阵乘固定 3n 周期完成
- 浮点单元采用 fudian.FCMA 模块，符合 IEEE-754，支持 FMA 流水
- 定点 Softmax 基于 I-BERT 算法（二次逼近指数，3 周期）
- 含 LLaMA 3 架构注意力层实现与 AXI/HBM 存储接口

## 适用场景

- 在 FPGA 上构建 LLM 推理加速硬件
- 复用定点/浮点运算单元与脉动阵列做神经网络硬件设计
- 研究 Transformer 算子的 RTL 实现与延迟特性

## 场景标签

`科研工具` `推理引擎` · 领域:学习与行业

## 证据(README 行号)

> L10: This is a comprehensive transformer-based large language model (LLM) accelerator developed using Chisel HDL. It imp
> L183: - **LLaMA 3 Support**: Includes attention layer and matrix controller implementations for LLaMA 3 architecture

## 星数曲线

```mermaid
xychart-beta
    title "CodingPlatelets/transformer_MM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `937ac12b72c9` · [字段定义](../../DATASET.md)*
