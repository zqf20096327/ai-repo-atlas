# kmheckel/spyx

⭐ 139 · Jupyter Notebook · MIT · 推送 2026-07-07 · [GitHub](https://github.com/kmheckel/spyx) · [官网](https://spyx.readthedocs.io/en/latest/) · 个人维护

**基于 JAX 的脉冲神经网络（SNN）构建与训练库**

构建于 JAX 与 Flax NNX 之上的 SNN 库，整个网络（含时间动力学）经 XLA JIT 编译以提升吞吐。提供两种训练方式：代理梯度下降（BPTT）与免梯度神经进化（evosax）；内置 LIF/ALIF/CuBaLIF 等神经元模块、状态空间层、复相网络、int8/int4/BitNet 量化与基准测试工具，并支持 NIR 导入导出和 ONNX 导出。默认 CPU 安装即可跑教程，较大模型依赖 GPU/TPU。面向 SNN 研究与实验人群，配套论文与硕士论文实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XLA JIT 编译整个网络（含时间动态）
- 代理梯度 BPTT 与神经进化（evosax）两种训练路径
- LIF/ALIF/CuBaLIF 等神经元与 LRU/S5Diag/Mamba 等状态空间层
- int8/int4/BitNet 量化、NIR 互操作与 ONNX 导出

## 适用场景

- 在 JAX 生态中搭建并训练脉冲神经网络
- 用代理梯度或神经进化方法做 SNN 实验
- 量化模型并测量延迟/吞吐/脉冲率等指标
- 通过 NIR 将模型迁移到神经形态硬件

## 场景标签

`模型训练` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L8: Spyx (pronounced "spikes") is a compact spiking neural network library built on JAX and Flax NNX. It offers the flex
> L12: - **Two ways to train** — surrogate-gradient descent (backprop through time) and gradient-free neuroevolution (`spy

## 星数曲线

```mermaid
xychart-beta
    title "kmheckel/spyx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-29 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f4e18e376f3d` · [字段定义](../../DATASET.md)*
