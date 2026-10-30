# Przemyslaw11/BeyondBackpropagation

⭐ 16 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Przemyslaw11/BeyondBackpropagation) · [官网](https://arxiv.org/abs/2511.01061) · 组织维护

**无反向传播深度学习算法的硬件实测基准研究代码**

PPAM 2026 论文的配套代码库，实现并对比 Forward-Forward、Cascaded Forward、Mono-Forward 三种免反向传播算法与调优后的 BP 基线：在 MNIST、Fashion-MNIST、CIFAR-10/100 上近千次运行，通过 NVML 以 5Hz 采集功耗、利用率与显存，测量能耗、时间、内存与 CO₂e。提供 YAML 配置、消融阶梯分析脚本与复现流程。能耗测量依赖 NVIDIA GPU 与 NVML；macOS 仅支持功能运行不记录能耗。面向科研复现者，Python 3.10 + PyTorch 2.4 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 FF/CaFo/MF 三种免反向传播算法及 BP 基线
- NVML 5Hz 硬件级能耗/功耗/显存测量（19,944 条测量记录）
- 预注册的消融阶梯分析（BP→BP-DS→MF-Joint→MF）
- 提供 BP/MF 匹配数据通过数协议的对比实验

## 适用场景

- 复现论文中的免反向传播算法能耗基准实验
- 在自己的 GPU 环境下训练并测量 Mono-Forward 模型
- 研究梯度分离等结构因素对精度与能耗的影响

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4:  Forward-Forward, Cascaded Forward and Mono-Forward measured on an NVIDIA A100
> L34: hardware: across almost 1000 runs on MNIST, Fashion-MNIST, CIFAR-10 and CIFAR-100, every run is
> L35: instrumented through NVML at 5 Hz for power, utilisation, clock and memory, and each algorithm is

## 星数曲线

```mermaid
xychart-beta
    title "Przemyslaw11/BeyondBackpropagation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b7bae5bde12f` · [字段定义](../../DATASET.md)*
