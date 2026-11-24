# Kxvinnnn/tang-nano-lif-verilog

⭐ 4 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Kxvinnnn/tang-nano-lif-verilog) · 个人维护

**在 Tang Nano 9K FPGA 上实现神经形态 LIF 神经元的 Verilog RTL 工程**

以 Verilog RTL 在 Sipeed Tang Nano 9K FPGA（Gowin GW1NR-9C）上综合实现的脉冲神经网络 Leaky Integrate-and-Fire 处理核：用符号 16 位定点饱和运算离散化膜电位微分方程，通过 BSRAM 存储突触权重，消除 DSP 块，并经 UART 以 115200 bps 输出 9 字节遥测包。面向同行评审者、科研导师与硬件工程师，配套技术论文、报告、数据手册、答辩与演示文档。包含将加州房价回归模型经 Rate Coding 映射到硬件的推理基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 符号 16 位定点 Forward Euler 积分，零 DSP 块实现泄漏项（右移 4 位）
- BSRAM 存储突触权重矩阵，UART 50 Hz 输出 9 字节状态遥测包
- 房价回归模型经 Rate Coding 映射至硬件（R²=0.9922）
- 配套五卷技术文档：论文、报告、数据手册、答辩与演示脚本

## 适用场景

- 在低成本 FPGA 上运行事件驱动的 SNN 神经元推理
- 通过 Rate Coding 将量化回归权重映射到硬件进行预测
- 神经形态计算的教学演示与硬件验证
- 同行评审与答辩场景的硅级审计与遥测对照

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: A gate-level hardware implementation of an event-driven **Spiking Neural Network (SNN)** Leaky Integrate-and-Fire (
> L82: To demonstrate practical Machine Learning inference on neuromorphic silicon, a classic **Housing Price Regression**
> L85: **Figure 3:** End-to-end Machine Learning to FPGA silicon pipeline. **(Panel 1)** Classical floating-point regressi


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `654b98c79a6f` · [字段定义](../../DATASET.md)*
