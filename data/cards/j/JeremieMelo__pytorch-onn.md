# JeremieMelo/pytorch-onn

⭐ 331 · Python · MIT · 推送 2026-01-13 · [GitHub](https://github.com/JeremieMelo/pytorch-onn) · 个人维护

**光子神经网络仿真与协同设计的 PyTorch 库，面向光子 AI 研究者**

基于 PyTorch 的集成神经形态光子学仿真框架，支持相干与非相干光学神经网络（ONN）在 GPU 上的训练与推理，可扩展至百万参数级 ONN。提供 MZI、FFT-ONN、多操作数微环（SqueezeLight）、PCM 光内存计算等多种架构，支持相位量化与非理想性注入、CUDA 加速的批量 MZI 阵列分解，以及标准 PyTorch 模型向光学模拟版本的转换。面向神经形态光子学、光 AI 系统设计与光子集成电路优化方向的研究者。依赖 Python、PyTorch、TensorFlow-gpu、CUDA 与 NVIDIA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MZI/FFT/微环/PCM 多种 ONN 架构的训练与推理
- 相位量化与非理想性注入（gamma 误差、相位波动、串扰）
- CUDA 加速批量 MZI 阵列分解，宣称较 CPU 实现 10-50 倍加速
- 标准 PyTorch Conv2d/Linear 模型可初始化/转换为光学模拟版本

## 适用场景

- 在 GPU 上仿真和训练光学神经网络模型
- 做光子集成电路与算法的跨层协同设计实验
- 研究 ONN 器件非理想性与量化对模型的影响

## 场景标签

 · 领域:光子计算/神经形态硬件

## 证据(README 行号)

> L23: Integrated neuromorphic photonics simulation framework based on PyTorch. It supports coherent and incoherent optica
> L25: Researchers on neuromorphic photonics, optical AI system design, photonic integrated circuit optimization, ONN trai

## 星数曲线

```mermaid
xychart-beta
    title "JeremieMelo/pytorch-onn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 329 --> 332
    line [330, 331, 331]
```

2026-10-18 330 → 2026-10-29 331（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `961737345190` · [字段定义](../../DATASET.md)*
