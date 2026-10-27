# yxtay/char-rnn-text-generation

⭐ 63 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/yxtay/char-rnn-text-generation) · 个人维护

**多框架复刻 char-RNN 字符级文本生成模型**

复刻 Andrej Karpathy 字符级 RNN 文本生成模型的代码库：以 Embedding + 2 层 LSTM + Dense 为默认结构（词表 98、LSTM 输出 128），在 Keras、TensorFlow、PyTorch 等不同深度学习框架中实现训练与生成脚本，主题标签还列出 Chainer 与 MXNet。提供 CLI 训练（指定 checkpoint 与文本路径）与生成（指定 seed、长度、top-n）两种用法，通过 git clone 与 uv sync 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 char-RNN 模型在 Keras/TensorFlow/PyTorch 多框架下实现
- 训练与生成均提供命令行接口（checkpoint、seed、top-n 等参数）
- 默认模型结构与训练超参数（batch 64、序列长 64、32 epochs）在 README 中完整给出

## 适用场景

- 学习 char-RNN 字符级文本生成的实现细节
- 对比不同深度学习框架下同一模型的写法
- 用自己的语料训练并生成字符级文本

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L6: This repository attempts to replicate the models, with slight modifications, in different python deep learning frame
> L63: ### Text Generation

## 星数曲线

```mermaid
xychart-beta
    title "yxtay/char-rnn-text-generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-27 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b840b61f4023` · [字段定义](../../DATASET.md)*
