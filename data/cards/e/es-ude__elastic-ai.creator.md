# es-ude/elastic-ai.creator

⭐ 26 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/es-ude/elastic-ai.creator) · [官网](https://es-ude.github.io/elastic-ai.creator/) · 组织维护

**面向 FPGA 的神经网络设计训练与 VHDL 生成库**

University of Duisburg-Essen 智能嵌入式系统实验室开发的 Python 库，属于 ElasticAI 生态：提供 elasticai.creator.nn 包中的量化层（linear、LSTM、hard sigmoid 等）用于设计与训练神经网络，将模型转换为中间表示再翻译为 VHDL，配合第三方工具（如 Xilinx Vivado）编译到 FPGA，并可生成 Elastic Node V5 骨架用于 C stub 接口。当前仅支持 torch.nn.Sequential 可表示的顺序模型，部分模块处于开发或弃用讨论状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供定点量化层（linear、带批归一化 linear、LSTM）与激活函数
- 模型翻译为 VHDL，配合第三方工具（如 Xilinx Vivado）编译到 FPGA
- 可生成 Elastic Node V5 骨架以 C stub 与 FPGA 上的模型交互
- 模块化架构支持添加自定义 VHDL 组件

## 适用场景

- 为 FPGA 设计并训练定点量化的神经网络
- 将 PyTorch 顺序模型转换为 VHDL 部署到 FPGA
- 在自研 VHDL 组件基础上扩展硬件生成能力

## 场景标签

 · 领域:嵌入式系统/硬件AI

## 证据(README 行号)

> L3: Design, train and compile neural networks optimized specifically for FPGAs.
> L5: * design and train it using the layers provided in the `elasticai.creator.nn` package.
> L6: * translate the model to a target representation, e.g. VHDL
> L11: The project is part of the ElasticAI ecosystem developed by the Intelligent Embedded Systems Lab of the University 

## 星数曲线

```mermaid
xychart-beta
    title "es-ude/elastic-ai.creator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2275920edc3d` · [字段定义](../../DATASET.md)*
