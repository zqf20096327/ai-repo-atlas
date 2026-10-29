# shiloz-stack/VeloSpec

⭐ 17 · Python · MIT · 推送 2026-08-07 · [GitHub](https://github.com/shiloz-stack/VeloSpec) · 个人维护

**语法感知的自适应投机解码库，加速 LLM 结构化输出**

面向 LLM 推理加速的 Python 库（pip 安装），将语法位掩码同时作用于草稿模型、并按位掩码密度（popcount）动态调整投机预算 K，从而加速 JSON/工具调用等结构化生成；无需训练。包含 4 个自研 GPU kernel（3 CUDA + 1 Triton），在 A100-SXM4 上以 Qwen3.5-4B/0.8B 做端到端基准：enum 密集 schema 下吞吐 2.73×，平均 1.35×；自由文本场景吞吐略低于固定 K。需要 Python 3.10+、CUDA 与 Triton。

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

- 语法位掩码同时约束草稿模型，保持高接受率
- 按位掩码密度动态设定投机预算 K（确定性信号，无需训练）
- 4 个自研 GPU kernel（3 CUDA + 1 Triton），Triton 融合 logit 处理替代 xgrammar mask + argmax + CPU popcount
- A100 端到端基准：纯 enum schema 吞吐 2.73×，平均 1.35×

## 适用场景

- 加速 JSON / 工具调用等结构化输出的推理吞吐
- 在受限语法场景下保持投机解码的接受率
- 研究自适应投机预算策略在结构化生成中的作用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: **VeloSpec** speeds up structured LLM output (JSON, tool calls) by combining
> L9: grammar-aware speculative decoding with an adaptive speculation budget —
> L10: 4 custom GPU kernels (3 CUDA + 1 Triton), benchmarked end-to-end on A100.

## 星数曲线

```mermaid
xychart-beta
    title "shiloz-stack/VeloSpec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1992b158b6fd` · [字段定义](../../DATASET.md)*
