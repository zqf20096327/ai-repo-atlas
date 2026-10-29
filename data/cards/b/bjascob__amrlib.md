# bjascob/amrlib

⭐ 267 · Python · MIT · 推送 2026-03-10 · [GitHub](https://github.com/bjascob/amrlib) · 个人维护

**AMR 解析与生成的 Python 库：句子↔抽象意义表示图互转**

amrlib 提供 Abstract Meaning Representation（AMR）处理的 Python 模块：句子到图（StoG）解析、图到句子（GtoS）生成、QT 图形界面查看与绘图、SpaCy 扩展将 Docs/Spans 转 AMR 图、两种对齐算法（FAA/RBW），以及 Smatch/BLEU 对齐评测指标 API。内置神经网络模型（BART 解析、T5 生成）须单独下载安装。附模型训练与测试代码；在 Python 3 下构建测试，支持 Linux/Windows/Mac。库本身不含 AMR 共指消解，指向相关项目 amr_coref。

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

- StoG 解析模型在 LDC2020T02 上报告 83.7 SMATCH
- GtoS 生成模型 generate_t5wtense 报告 54 BLEU（带时态标签）
- SpaCy 扩展将 Docs/Spans 直接转 AMR 图
- Smatch/BLEU/对齐评测指标 API 与模型训练测试代码

## 适用场景

- 把英文句子解析为 AMR 图做语义表示
- 将 AMR 图生成回英文句子（如改写应用）
- 在 spaCy 流水线中接入 AMR 转换

## 场景标签

 · 领域:自然语言处理/语义表示

## 证据(README 行号)

> L12: * Sentence to Graph (StoG) parsing to create AMR graphs from English sentences.
> L30: The system includes different neural-network models for parsing and for generation. **!! Note:** Models must be dow

## 星数曲线

```mermaid
xychart-beta
    title "bjascob/amrlib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 266 --> 268
    line [267, 267]
```

2026-10-18 267 → 2026-10-29 267（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d5479c71d03c` · [字段定义](../../DATASET.md)*
