# SyntaxSpirits/rust-lstm

⭐ 24 · Rust · MIT · 推送 2026-10-12 · [GitHub](https://github.com/SyntaxSpirits/rust-lstm) · [官网](https://syntaxspirits.dev/rust-lstm) · 个人维护

**Rust 实现的 LSTM/BiLSTM/GRU 神经网络库，含训练与梯度验证**

用 Rust 编写的循环神经网络库，提供 LSTM、双向 BiLSTM、GRU 与线性层，多层堆叠；训练系统支持完整 BPTT、SGD/Adam/RMSprop 优化器、12 种学习率调度器、多种 dropout 与 zoneout 正则化、早停、批处理与 JSON/二进制模型持久化。梯度经有限差分校验，输出与梯度同 PyTorch 对比达 float64 舍入级别（CI 运行）。以 crates.io 包形式分发，面向 Rust 开发者与科研复现场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LSTM/BiLSTM/GRU 多层网络与完整 BPTT 训练系统
- SGD/Adam/RMSprop 与 12 种学习率调度器
- 多种 dropout、zoneout 正则化与早停
- 梯度经有限差分校验，与 PyTorch 对比在 CI 中验证

## 适用场景

- 在 Rust 项目中构建和训练序列模型
- 需要可复现训练（seed 固定权重与 mask）的研究实验
- 用 BiLSTM/GRU 做分类或序列建模任务

## 场景标签

 · 领域:机器学习/科学计算

## 证据(README 行号)

> L9: A comprehensive LSTM (Long Short-Term Memory) neural network library implemented in Rust with complete training capa
> L24: - **Complete Training System** with full backpropagation through time (BPTT)

## 星数曲线

```mermaid
xychart-beta
    title "SyntaxSpirits/rust-lstm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `87a0c7fc1cea` · [字段定义](../../DATASET.md)*
