# storagebits/ttlm

⭐ 3 · C · MIT · 推送 2026-11-22 · [GitHub](https://github.com/storagebits/ttlm) · [官网](https://storagebits.github.io/ttlm/) · 个人维护

**在无 CPU 的 Gigatron TTL 计算机上运行的 22k 三值权重微型语言模型**

TTLM 是一个 decoder-only transformer（2 层、宽 32、21,984 个三值参数），以纯整数运算（加法、移位、查表，无乘法）在 Gigatron TTL 8 位计算机上运行推理，模型压缩到 9 KB 权重加 2.5 KB KV cache，与屏幕画面共存于 32 KB RAM 中。模型在笔记本电脑上用 40,000 条模板生成的合成对话训练约五分钟；三种实现（PyTorch、Python 参考、Gigatron C/汇编）输出 bit-identical logits。可烧录到真实 Gigatron、在浏览器模拟器或任意模拟器中运行。

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

- 三值权重（BitNet b1.58 风格）使线性层无需乘法
- 纯整数推理：移位归一化、查表 softmax、quarter-squares 乘法
- PyTorch/Python/C 三实现 bit-identical，make test 自动校验
- 模型权重与 KV cache 直接以像素形式显示在屏幕上

## 适用场景

- 在真实 Gigatron TTL 硬件上与模型对话
- 在浏览器模拟器中直接体验极小语言模型推理
- 研究三值量化与整数推理在极端受限硬件上的实现

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L19: TTLM puts a language model on it. It's not a lookup table or a chatbot script: it's a
> L47: |Architecture|decoder-only transformer (GPT-style), causal self-attention|
> L100: 1. the PyTorch training model (`model/qmodel.py`),
> L151: You need a Gigatron with 32 KB and ROM v4 (`gigatron/ttlm.gt1`). For ROM v3,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `760ebbc1ae30` · [字段定义](../../DATASET.md)*
