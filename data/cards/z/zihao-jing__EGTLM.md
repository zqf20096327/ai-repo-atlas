# zihao-jing/EGTLM

⭐ 21 · Python · Apache-2.0 · 推送 2026-05-14 · [GitHub](https://github.com/zihao-jing/EGTLM) · 组织维护 · 中文 README

**同时做文本生成与文本嵌入的模型训练评测代码**

EGTLM 模型的训练与评测代码，由 SenseTime 于 2024 年构建。模型通过两阶段训练（无监督预训练+有监督指令微调）和混合损失函数（生成损失+嵌入损失加权组合），同时支持文本生成与文本嵌入任务，并设计了基于该模型的 RAG 知识系统方案。在 MTEB 中文榜单得分 68、位列前十。以 Python 代码库形式提供，依赖 accelerate、transformers、datasets、wandb、mteb。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合损失函数统一训练生成与嵌入两类任务
- 两阶段训练：无监督预训练+有监督指令微调
- MTEB 中文评测 68 分（前十）
- 附带基于 EGTLM 的 RAG 知识系统方案

## 适用场景

- 复现或训练同时具备生成与嵌入能力的模型
- 在 MTEB 上评测中文文本嵌入效果
- 为 RAG 系统提供嵌入模型

## 场景标签

 · 领域:NLP/文本嵌入与大语言模型

## 证据(README 行号)

> L7: Embedding Generative Tuning Language Model (EGTLM), leveraging the robust semantic processing capabilities of large 
> L37: By using this mixed-task training approach, the model is capable of both text generation and embedding tasks effect

## 星数曲线

```mermaid
xychart-beta
    title "zihao-jing/EGTLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dc76855b26ed` · [字段定义](../../DATASET.md)*
