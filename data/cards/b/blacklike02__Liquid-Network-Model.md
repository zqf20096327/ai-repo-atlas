# blacklike02/Liquid-Network-Model

⭐ 4 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/blacklike02/Liquid-Network-Model) · 个人维护 · 中文 README

**基于液体神经网络的 PyTorch 自回归语言模型训练与生成工具**

以 LTC（液体时间常数）与 CfC（闭式连续时间）单元替代 self-attention 的自回归语言模型实现，逐 token 循环更新隐状态，生成成本随序列长度线性增长。仓库提供语料加载清洗、BPE/字符分词器、训练（截断 BPTT、EMA、蒸馏、混合精度）、文本生成与交互式对话 REPL，统一由 liquid_text_model.py 入口启动。训练数据与检查点不随仓库提供，需自备语料（有意义生成需兆级文本），CPU 可运行但 GPU 执行需 CUDA 版 PyTorch。

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

- LTC/CfC 液体神经网络单元替代 self-attention，逐 token 循环处理
- 多时间常数库（fast/medium/slow）经 softmax 混合，支持共享权重循环深度
- 支持对话数据自动转换（OpenAI/ShareGPT/Alpaca 格式）与 loss 掩码训练
- 可选 Triton 融合内核与 CUDA Graphs 加速推理

## 适用场景

- 用自己的文本语料从零训练一个小型语言模型
- 训练对话语料后进行交互式聊天
- 研究液体神经网络在语言建模中的行为

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: An autoregressive language model implemented with **Liquid Neural
> L9: Networks** (Liquid Time-Constant and Closed-form Continuous-time) in PyTorch.
> L16: Instead of self-attention, the model processes text recurrently: each layer's
> L74: - Temperature, top-k, top-p, and repetition-penalty sampling.

## 星数曲线

```mermaid
xychart-beta
    title "blacklike02/Liquid-Network-Model 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-20 4 → 2026-11-22 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `2a6d5b589222` · [字段定义](../../DATASET.md)*
