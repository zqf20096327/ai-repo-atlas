# google-deepmind/transformer_grammars

⭐ 142 · Python · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/google-deepmind/transformer_grammars) · 组织维护

**DeepMind 的 Transformer Grammars 研究代码：语法结构归纳偏置的语言模型**

TACL 2022 论文 Transformer Grammars 的官方实现，基于 JAX。模型将句子/文档表示为线性化树的动作序列，注意力掩码由结构本身决定，使成分表示递归组合。README 覆盖安装（含 C++ 扩展构建）、树结构数据准备、SentencePiece 或词表两种分词路径、训练、打分与采样脚本；示例数据来自狄更斯小说并用 spaCy/Benepar 解析。测试环境为 NVIDIA V100 + CUDA 11.3 + Python 3.7。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 注意力掩码由句法结构决定，成分表示递归组合
- 提供数据准备、训练、打分、采样全流程脚本
- 需构建 C++ 扩展计算注意力掩码/相对位置/记忆更新
- 支持 SentencePiece 与词表两种分词路径

## 适用场景

- 复现论文中的 TG 模型训练与评估实验
- 研究句法归纳偏置对语言建模的影响
- 基于 TG checkpoint 对树结构语料打分或采样

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Transformer Grammars are Transformer-like models of the joint structure and
> L8: recursively. The approach is fully described in our paper Transformer Grammars:
> L217: python train.py --config config.py

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/transformer_grammars 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 141 --> 143
    line [142, 142]
```

2026-10-18 142 → 2026-10-24 142（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5c4272674851` · [字段定义](../../DATASET.md)*
