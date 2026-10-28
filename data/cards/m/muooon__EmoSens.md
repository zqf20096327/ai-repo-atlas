# muooon/EmoSens

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/muooon/EmoSens) · 个人维护 · 中文 README

**情感驱动的 PyTorch 系优化器系列（emoPulse 自动学习率）**

名为 emo-series 的神经网络优化器集合（EmoSens/EmoTion/EmoAiry/EmoCats/EmoVoid 等），采用自称的 Resonant Contraction 方法，包含 emoPulse 自动学习率调度、无矩（Moment-Free）变体、早停信号与分布式学习支持，面向 Transformer/DiT 模型的 LoRA 与全量微调给出学习率建议。README 含大量理论性声明，且作者已公告 v3.8 之前版本的实验结果与理论主张经其后续验证很可能不成立（含未应用 closure 的实现问题），相关内容标注为未验证草稿。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- emoPulse 自动学习率控制，已单独封装为 Scheduler 类型
- 多个变体覆盖精度/显存权衡（Adam 型、Adafactor 型、Lion 型、Original 型）
- v3.8 之前版本的理论与实验声明被作者公告为很可能不成立
- 对 Transformer/DiT 模型给出 LoRA 与全量微调的学习率起点建议

## 适用场景

- 在 LoRA/全量微调中替换现有优化器进行尝试
- 希望省去学习率调参的自动调度场景
- 分布式学习中采用免同步的优化器方案

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L89: - ###### This is a new generation of optimizers that use the Resonant Contraction Method (Resonant Projection Field
> L108: - Fully Automatic Value Learning Rate: Achieves both acceleration and refinement while eliminating the need to wor

## 星数曲线

```mermaid
xychart-beta
    title "muooon/EmoSens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8702e338689c` · [字段定义](../../DATASET.md)*
