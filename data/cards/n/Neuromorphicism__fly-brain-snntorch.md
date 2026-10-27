# Neuromorphicism/fly-brain-snntorch

⭐ 31 · Python · MIT · 推送 2026-09-20 · [GitHub](https://github.com/Neuromorphicism/fly-brain-snntorch) · 个人维护

**果蝇大脑连接组的稀疏 snnTorch 脉冲神经网络仿真实现**

将 Brian2 实现的果蝇（Drosophila）大脑计算模型移植到 snnTorch 框架，采用稀疏张量（COO/CSR）运行包含约 12.7 万神经元的脉冲神经网络仿真。提供味觉、嗅觉、视觉、听觉 4 种感官实验，通过修改 fly_brain.py 中的变量切换刺激神经元，运行后生成结果图表。支持 Linux/Windows/macOS，CPU 即可运行（无需 CUDA/MPS，可选开启）。README 给出与 Brian2 的耗时对比及 snnTorch 神经元缺少相对不应期的限制说明。供计算神经科学与神经形态计算方向的研究者使用。

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

- 果蝇大脑连接组的 snnTorch 移植，支持稀疏（COO/CSR）与稠密两种模式
- 味觉/嗅觉/视觉/听觉 4 种感官实验，通过变量切换刺激神经元
- CPU 即可运行，CUDA/MPS 为可选项
- 运行输出约 12.7 万神经元的尖峰栅格图与实验图表

## 适用场景

- 仿真果蝇大脑连接组并复现感官刺激实验
- 在 snnTorch/PyTorch 生态中研究稀疏脉冲神经网络的仿真速度
- 比较不同平台（CPU/CUDA）与框架下的大规模 SNN 仿真表现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Port of Brian2 implementation of fruit fly brain to snnTorch with new sensory experiments
> L57: python3 fly_brain.py

## 星数曲线

```mermaid
xychart-beta
    title "Neuromorphicism/fly-brain-snntorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `aa8f392154c3` · [字段定义](../../DATASET.md)*
