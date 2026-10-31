# SkuldNorniern/cetana

⭐ 15 · Rust · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/SkuldNorniern/cetana) · 个人维护

**Rust 机器学习库：类型安全张量运算与神经网络构建**

用 Rust 编写的机器学习库，面向在应用中集成机器学习功能的开发者。提供类型安全张量运算、自动微分与反向传播、线性/卷积/池化层、激活函数、优化器与损失函数（MSE/交叉熵）以及模型序列化保存加载。当前仅 CPU 后端可用，CUDA、MPS、Vulkan 后端列为规划项，分布式训练、混合精度、量化与模型库等属于 Roadmap 未完成阶段。以 crates.io 包形式经 Cargo.toml 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类型安全张量运算与自动微分/反向传播
- 神经网络层组件（Linear/卷积/池化）与损失函数、优化器
- 模型序列化（保存/加载训练模型）
- CPU 后端当前可用，CUDA/MPS/Vulkan 列为规划

## 适用场景

- 在 Rust 项目中构建和训练神经网络
- 需要内存安全的张量运算与自动微分
- 保存和加载训练好的模型用于推理

## 场景标签

 · 领域:机器学习/开发库

## 证据(README 行号)

> L20: Cetana is a Rust-based machine learning library designed to provide efficient and flexible machine learning operati
> L33: - **Type-safe Tensor Operations** - Memory-safe tensor operations with compile-time guarantees

## 星数曲线

```mermaid
xychart-beta
    title "SkuldNorniern/cetana 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0d2e238c3379` · [字段定义](../../DATASET.md)*
