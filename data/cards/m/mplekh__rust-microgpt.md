# mplekh/rust-microgpt

⭐ 50 · Rust · 推送 2026-03-07 · [GitHub](https://github.com/mplekh/rust-microgpt) · 个人维护

**Karpathy microGPT 的 Rust 移植：字符级 GPT 训练与生成**

将 Andrej Karpathy 的 microgpt.py Python 实现翻译为纯 Rust 的字符级 GPT：包含自研基于 Tape 的反向模式自动微分引擎（预分配内存池、原始指针绕过边界检查）、复刻 Python random 的 MT19937 确定性随机数、Transformer 前向（WTE/WPE 嵌入、多头缩放点积注意力、ReLU MLP）与 Adam 优化器及线性学习率衰减。面向对底层实现感兴趣的开发者：下载文本数据集（names.txt 等）重命名为 input.txt，用 cargo run --release 训练并生成 20 个新字符串；面向短字符串生成（名字、歌词、代码片段），属学习/实验规模实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Tape 的反向模式自动微分引擎（预分配内存池 + 原始指针）
- 复刻 Python random 模块的 MT19937 确定性 RNG
- 完整 Transformer 训练循环：嵌入、多头注意力、MLP、Adam 与线性学习率衰减
- 训练后自动进入推理循环生成 20 个新字符串

## 适用场景

- 阅读/修改一个纯 Rust 的微型 GPT 实现来学习 Transformer 细节
- 用自己的文本（名字、歌词、代码片段）训练字符级生成模型
- 学习自动微分引擎与反向传播的底层实现

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: ### A high-performance, character-level GPT written in Pure Rust.
> L57: After training, the model enters an inference loop and generates 20 new "hallucinated" strings based on the pattern

## 星数曲线

```mermaid
xychart-beta
    title "mplekh/rust-microgpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-26 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7ff5d56321d8` · [字段定义](../../DATASET.md)*
