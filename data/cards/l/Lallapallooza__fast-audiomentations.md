# Lallapallooza/fast-audiomentations

⭐ 38 · Python · MIT · 推送 2026-05-08 · [GitHub](https://github.com/Lallapallooza/fast-audiomentations) · 个人维护

**GPU/CUDA 上的 PyTorch 音频数据增强变换库，以 Triton 核实现**

面向 PyTorch 训练管线的音频增强库：提供 Clip、Gain、PolarityInversion、Reverse、四种 FIR 滤波与 AddBackgroundNoise 九种变换，均以手写 Triton 内核在 GPU 上执行，采用构造期预分配缓冲、热路径零分配的设计。仅支持 Linux x86_64 + CUDA，macOS/Windows/CPU-only/ROCm 明确排除在外；随机参数变换默认缓冲上限 129，无种子可复现机制。尚未发布 PyPI，通过 uv 以 git 依赖安装；与 audiomentations、torch-audiomentations 做数值验证与基准对比，但不做 API 兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种音频变换以手写 Triton 内核 GPU 执行
- 构造期预分配缓冲、热路径零分配设计
- 基准框架同时对比 audiomentations（CPU）与 torch-audiomentations（CUDA）并记录主机环境不变量
- AddBackgroundNoise 可选 NVIDIA DALI 数据加载器，否则回退 torch DataLoader

## 适用场景

- 为音频机器学习训练管线做 GPU 批量数据增强
- 在 CUDA 服务器上替代 CPU 音频增强以加速数据准备
- 验证/对比不同音频增强库的数值一致性与吞吐性能

## 场景标签

 · 领域:音频/机器学习数据工具

## 证据(README 行号)

> L3: > GPU-resident audio augmentations for PyTorch, dispatched as hand-written Triton kernels. Linux + CUDA only. MIT.
> L14: - **Linux x86_64 + CUDA only.** macOS / Windows / CPU-only / ROCm are out of scope. Every transform allocates its s

## 星数曲线

```mermaid
xychart-beta
    title "Lallapallooza/fast-audiomentations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `34199cf439e7` · [字段定义](../../DATASET.md)*
