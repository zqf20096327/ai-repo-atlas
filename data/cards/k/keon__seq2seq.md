# keon/seq2seq

⭐ 706 · Python · MIT · 推送 2026-05-18 · [GitHub](https://github.com/keon/seq2seq) · 个人维护

**给学习研究者的 PyTorch 最小注意力 Seq2Seq 机器翻译实现**

以 PyTorch 实现的带注意力机制的编码器-解码器神经机器翻译模型：编码器为双向 GRU，解码器为 GRU 加注意力（对齐机制按 Bahdanau 论文）。训练数据为 Multi30k 德译英，经 HuggingFace datasets 加载、spaCy 分词。设计目标是最小可读代码、模块化结构与 GPU 批处理，设备自动检测 CUDA→MPS→CPU。适用于其他研究项目复用或作为教学参考实现，需 Python 3.9+ 与 PyTorch >= 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编码器双向 GRU + 解码器 GRU 注意力结构
- 支持批处理与 GPU（CUDA/MPS/CPU 自动检测）
- 模块化结构便于在其他项目中复用
- README 提供 CPU 冒烟测试的损失曲线与困惑度数据

## 适用场景

- 学习注意力 Seq2Seq 的最小可读实现
- 作为模板在自己项目中复用编码器-解码器结构
- 在 Multi30k 德英数据集上复现训练流程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: Minimal Seq2Seq model with attention for neural machine translation in PyTorch.
> L14: * Encoder: Bidirectional GRU
> L15: * Decoder: GRU with Attention Mechanism

## 星数曲线

```mermaid
xychart-beta
    title "keon/seq2seq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 705 --> 707
    line [706, 706]
```

2026-10-18 706 → 2026-10-27 706（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b88911e81bcd` · [字段定义](../../DATASET.md)*
