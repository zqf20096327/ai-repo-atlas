# FunnySaltyFish/Better-Ruozhiba

⭐ 265 · Apache-2.0 · 推送 2026-02-21 · [GitHub](https://github.com/FunnySaltyFish/Better-Ruozhiba) · 个人维护 · 中文 README

**人工审核修订的中文弱智吧问答数据集**

基于原 Hugging Face 数据集 LooksJuicy/ruozhiba 的中文问答语料：原部分答案由 GPT-4 生成，贡献者逐条人工审阅原文与回复，剔除格式错误并修改或重写部分答案，供大语言模型中文语料训练使用。任务类别标注为 text-generation，语言为中文，采用 Apache-2.0 许可。以数据集形式托管于 Hugging Face，并提供 BibTeX 引用格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐条人工审阅原文与回复，剔除格式错误
- 修改或重写了原 GPT-4 生成的部分答案
- 面向大语言模型的中文 text-generation 语料

## 适用场景

- 为大语言模型的中文预训练或微调提供问答语料
- 获取经人工清洗的弱智吧风格问答数据

## 场景标签

 · 领域:NLP/训练数据集

## 证据(README 行号)

> L8: 原项目为 https://huggingface.co/datasets/LooksJuicy/ruozhiba，原部分答案为 GPT-4 生成。贡献者们**人为审阅了每一条的原文和回复**，剔除了一些原文中的格式错误，修改或重写了
> L3: - text-generation

## 星数曲线

```mermaid
xychart-beta
    title "FunnySaltyFish/Better-Ruozhiba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 264 --> 266
    line [265, 265]
```

2026-10-18 265 → 2026-10-27 265（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0084c8d022d2` · [字段定义](../../DATASET.md)*
