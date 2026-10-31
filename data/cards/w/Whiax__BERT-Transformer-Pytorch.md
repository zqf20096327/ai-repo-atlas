# Whiax/BERT-Transformer-Pytorch

⭐ 46 · Python · MIT · 推送 2026-06-27 · [GitHub](https://github.com/Whiax/BERT-Transformer-Pytorch) · 个人维护

**给 NLP 初学者的 BERT/Transformer PyTorch 教学实现**

单文件（train.py，约 300 行）的 BERT 与 Transformer PyTorch 实现，面向 NLP 初学者与想了解 Transformer 工作原理的人。采用简化的 BERT 训练方式，无需标签；Transformer 部分仅保留 encoder。模型可在 1 x RTX2070Super 上 30 分钟内完成训练。2023 年 8 月更新增加用于训练 GPT 的 'predict next word' 任务，代码在 main_predictnextword.py 中。附实现细节文章链接与词嵌入可视化。

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

- 单文件约 300 行实现 BERT 与 Transformer
- 简化训练，无需标签
- 额外提供 GPT 式 'predict next word' 任务实现
- 可在单张 RTX2070Super 上 30 分钟训练

## 适用场景

- 初学者阅读源码理解 Transformer 内部机制
- 跑通一个小型 BERT/GPT 训练实验
- 对照教程文章学习 PyTorch 实现

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: Basic implementation of BERT and Transformer in Pytorch in one python file of ~300 lines of code (train.py).
> L4: This project aims to provide an easy-to-run easy-to-understand code for NLP beginners and people who want to know ho

## 星数曲线

```mermaid
xychart-beta
    title "Whiax/BERT-Transformer-Pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e79da42a7f32` · [字段定义](../../DATASET.md)*
