# Jim137/qkan

⭐ 32 · Python · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/Jim137/qkan) · [官网](https://qkan.jimq.cc) · 个人维护

**论文官方实现的量子启发 Kolmogorov-Arnold 网络库**

论文《Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks》的官方 PyTorch 实现，供科研与开发者构建和训练 QKAN 模型。核心机制是以量子变分激活函数（QVAF）替代 KAN 的样条激活，提供 exact/flash/cute/cutile/cutn 五种求解器，后四种为 GPU 优化（Triton、CuTe DSL、cuQuantum），支持 BF16/FP8 混合精度、QKAN 专用优化器、激活检查点、CUDA graph 加速。另含 PennyLane 版量子电路演示（未做性能优化）。经 pip 安装，含函数拟合、分类、生成建模示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 量子变分激活函数（QVAF）的 PyTorch 实现，官方论文代码
- 五种求解器，含 Triton/CuTe/cuQuantum GPU 优化版本
- BF16/FP8 混合精度与 QKAN 专用优化器（QKANAdamMini 等）
- CUDA graph 训练/推理加速与激活检查点

## 适用场景

- 复现论文中的 QKAN 实验与函数拟合/分类任务
- 将量子变分激活函数用于自定义 PyTorch 模型训练
- 研究混合精度与 GPU 求解器对 KAN 类网络的影响

## 场景标签

 · 领域:机器学习/量子启发算法

## 证据(README 行号)

> L18: This is the official repository for the paper:
> L23: We provide a PyTorch implementation of QKAN with:

## 星数曲线

```mermaid
xychart-beta
    title "Jim137/qkan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 33
    line [31, 32]
```

2026-10-18 31 → 2026-10-29 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2a3414c3074e` · [字段定义](../../DATASET.md)*
