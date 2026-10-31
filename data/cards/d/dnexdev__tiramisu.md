# dnexdev/tiramisu

⭐ 21 · C++ · MIT · 推送 2026-09-17 · [GitHub](https://github.com/dnexdev/tiramisu) · [官网](https://tiramisu.dnex.dev/) · 个人维护

**C++20 从零实现的类 PyTorch 机器学习框架**

以 C++20 从零构建的机器学习框架，通过 pybind11 暴露 PyTorch 风格的 Python API：包含反向模式自动微分（每个算子带梯度检查）、支持零拷贝视图与 NumPy 互操作的 strided 张量引擎、手写 AVX2 SIMD 矩阵乘法、完整 transformer 栈（多头注意力/LayerNorm/GELU/GPT）与 Adam 等优化器。可选 CUDA 后端，支持序列化检查点。面向深度学习学习与实验，提供 pip 轮子（Linux/macOS/Windows），其他平台需 CMake + C++20 编译器从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向模式自动微分，每个算子带梯度检查
- 手写 AVX2 SIMD matmul，x86 上约 8 倍于朴素实现
- 完整 transformer 栈：多头注意力、LayerNorm、GELU、GPT
- 可选 CUDA 后端（--device cuda）

## 适用场景

- 学习自动微分与深度学习框架的底层实现
- 在 Python 中以 PyTorch 风格 API 训练 MLP 与字符级 GPT
- C++ 环境下做张量计算与模型训练实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: A from-scratch ML framework in **C++20** with a PyTorch-like Python API.
> L7: - **Automatic differentiation** -- reverse-mode autograd with gradient checking on every op
> L10: - **Full transformer stack** -- multi-head attention, LayerNorm, GELU, GPT

## 星数曲线

```mermaid
xychart-beta
    title "dnexdev/tiramisu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f61a42a0cd95` · [字段定义](../../DATASET.md)*
