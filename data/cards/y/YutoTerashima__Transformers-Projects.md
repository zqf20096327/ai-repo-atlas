# YutoTerashima/Transformers-Projects

⭐ 16 · Jupyter Notebook · MIT · 推送 2026-05-02 · [GitHub](https://github.com/YutoTerashima/Transformers-Projects) · 个人维护 · 中文 README

**中文 NLP Transformer 项目集：9 类任务笔记与训练结果档案**

基于 Hugging Face Transformers 的中文 NLP 学习与研究项目合集，以 Jupyter 笔记本覆盖掩码/自回归语言建模、命名实体识别、机器阅读理解、多项选择、句对相似度、双编码器检索、检索式聊天与 T5/GLM 摘要共 9 条任务线。仓库不含大模型权重与原始数据集，改为提交原始笔记本、工具代码、任务注册表以及从本地 trainer_state.json 生成的指标报表，并附笔记本复杂度与任务覆盖度等二轮审查 CSV。通过 pip -e 安装并运行 pytest 与冒烟脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 条中文 NLP 任务线（MLM/NER/MRC/选择/相似度/检索/摘要等）
- 指标快照由本地 trainer_state.json 工件生成（如 NER F1 0.9529）
- 仓库不含 GB 级权重与缓存，提交笔记本+工具代码+任务注册表+报告
- 二轮审查输出复杂度/排行榜/覆盖度三份 CSV

## 适用场景

- 学习 Hugging Face Transformers 在中文 NLP 各任务上的完整训练流程
- 查阅 MacBERT/Mengzi-T5/GLM 在中文数据集上的实测指标
- 复用双编码器+FAISS+交叉编码器的检索式问答管线代码

## 场景标签

`教程课程` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A curated Chinese NLP lab built with Hugging Face Transformers. The notebooks cover language
> L8: This repository packages the original learning notebooks from the local `DL` workspace into a
> L44: The latest maturity iteration turns the notebook collection into an auditable NLP project archive.

## 星数曲线

```mermaid
xychart-beta
    title "YutoTerashima/Transformers-Projects 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `59e2a5155ecf` · [字段定义](../../DATASET.md)*
