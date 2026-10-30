# MelbourneDeveloper/dart_llm

⭐ 19 · Dart · 推送 2026-03-26 · [GitHub](https://github.com/MelbourneDeveloper/dart_llm) · 个人维护

**纯 Dart 实现的极小 GPT 语言模型：内置训练与文本生成**

用纯 Dart 编写的教学型极小语言模型：自实现 Tensor 与自动求导引擎，构建小型 GPT 网络（多头自注意力、MLP、LayerNorm），使用 ByteTokenizer 字节级分词（词表 256），在内置短文本上以 next-token 预测与交叉熵训练（默认 300 轮，AdamW 优化），随后打印采样生成的文本续写。超参数（块大小、层数、轮数等）需在 main() 中编辑源码调整。README 明示小数据少轮数下输出质量差属预期现象。

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

- 纯 Dart 自实现 Tensor/autograd 引擎，无深度学习框架依赖
- 小型 GPT 架构：多头自注意力 + MLP + LayerNorm
- 字节级分词（词表 256）与 AdamW 优化器
- 提供 dart test 测试入口

## 适用场景

- 学习 GPT 与反向传播的实现细节
- 在 Dart 环境中实验小型语言模型的训练与采样
- 替换内置语料验证超参数对生成质量的影响

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A tiny language model (LLM) written in pure Dart. It implements a minimal GPT-style network with a custom Tensor/aut
> L30: * Model: small GPT with multi‑head self‑attention, MLP, layer norm.

## 星数曲线

```mermaid
xychart-beta
    title "MelbourneDeveloper/dart_llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e02b99807825` · [字段定义](../../DATASET.md)*
