# aurelio-amerio/GenSBI

⭐ 20 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/aurelio-amerio/GenSBI) · [官网](https://gensbi.com) · 个人维护

**JAX 的仿真推断生成式方法库：流匹配/扩散/归一化流做后验推断**

基于 JAX 和 Flax NNX 的仿真推断（SBI）库，面向似然函数不可解析场景下需要后验推断的研究者与从业者。实现最优传输条件流匹配、扩散模型与归一化流三类生成方法，提供 Recipes 高层 API 用少量代码完成训练与推断，包含 Flux1、Flux1Join、Simformer 等 Transformer 模型实现，并支持通过 mesh 进行 GPU/TPU 多设备并行训练与采样（FSDP 与张量并行规则标注为实验性）。配有配套综述论文与示例 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 OT 条件流匹配、扩散模型、归一化流三类 SBI 方法
- Recipes 高层 API：少量代码完成训练与推断
- Flux1 / Flux1Join / Simformer 等 Transformer 模型实现
- mesh 多设备 GPU/TPU 数据并行训练与采样

## 适用场景

- 似然不可解析的科研推断问题中做后验分布估计
- 在 two-moons 等基准上比较流匹配与扩散方法
- 高维复杂仿真数据上训练生成式推断模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: **GenSBI** is a JAX-based library for Simulation-Based Inference (SBI) using state-of-the-art generative methods, c
> L21: - **Modern SBI Algorithms**: Implements cutting-edge techniques like **Optimal Transport Conditional Flow Matching*

## 星数曲线

```mermaid
xychart-beta
    title "aurelio-amerio/GenSBI 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-26 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b12cc914d0c0` · [字段定义](../../DATASET.md)*
