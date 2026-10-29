# AspadaX/tiny-llm

⭐ 43 · Rust · MIT · 推送 2026-08-14 · [GitHub](https://github.com/AspadaX/tiny-llm) · 个人维护

**Rust 手写 MiniCPM5-1B 极简推理引擎，附 TUI 可视化**

纯 Rust 编写的极简大模型推理引擎，专用于 MiniCPM5-1B。手写张量运算与 RMSNorm、RoPE、GQA 注意力、SwiGLU 等 Transformer 组件，实现简单 KV cache 并提供 SIMD 优化，CPU-only 运行无需 GPU。带 TUI 实时展示注意力热图、候选 logits 与延迟/吞吐统计。模型文件需自行从 HuggingFace 下载，通过 cargo 构建运行。作者以学习 LLM 原理为目的编写，另含基于 candle 的分支版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手写张量运算与 RMSNorm/RoPE/GQA/SwiGLU 等算法组件
- CPU-only 推理，无需 GPU
- TUI 实时可视化注意力热图与候选 logits
- KV cache 实现与 SIMD 优化，附基准统计

## 适用场景

- 阅读源码学习 LLM 推理各组件的实现原理
- 在无 GPU 环境本地运行 MiniCPM5-1B 生成文本
- 观察注意力热图与推理过程做教学演示

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A minimal LLM inference engine for MiniCPM5-1B, built purely in Rust.
> L13: - **CPU-only inference** — no GPU required

## 星数曲线

```mermaid
xychart-beta
    title "AspadaX/tiny-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-29 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6ecdc6988bdf` · [字段定义](../../DATASET.md)*
