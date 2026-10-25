# vinhowe/piston

⭐ 37 · Rust · MIT · 推送 2025-12-03 · [GitHub](https://github.com/vinhowe/piston) · [官网](https://sequence.toys) · 个人维护

**浏览器内训练序列模型：WebGPU 自动微分库与网页试验场**

包含两个相关项目：Piston 是概念验证的 WebGPU 自动微分库，从 Ratchet 分叉并加入反向传播；Sequence Toy 是基于 Piston 的网页试验场，支持在浏览器中训练 Transformer、LSTM、GRU 与 vanilla RNN 等序列模型。反向传播实现参考 Candle，惰性执行模型来自 LazyTensor，另含 Muon 优化器参考、简化版 BPE 分词器与基于 minGPT 的 GPT-2 实现。README 仅列出致谢与出处，未给出安装运行步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- WebGPU 自动微分库 Piston（Ratchet 分叉）
- 浏览器内训练 Transformer/LSTM/GRU/RNN 的网页试验场
- 含 Muon 优化器参考与 GPT-2 模型实现

## 适用场景

- 在浏览器中直接训练小型序列模型做实验
- 了解 WebGPU 上的自动微分与惰性执行实现

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: Train language models in your browser with WebGPU-powered autodiff.
> L9: Sequence Toy is a web playground for training sequence models (Transformers, LSTMs, GRUs, and vanilla RNNs) using Pi

## 星数曲线

```mermaid
xychart-beta
    title "vinhowe/piston 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `64eda5c0f83c` · [字段定义](../../DATASET.md)*
