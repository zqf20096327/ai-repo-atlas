# mlwithme/BertWithPretrained

⭐ 602 · Python · 推送 2026-09-08 · [GitHub](https://github.com/mlwithme/BertWithPretrained) · 个人维护 · 中文 README

**BERT 模型及其下游任务的 PyTorch 教学式实现与原理解析**

基于 PyTorch 从零实现 BERT 模型及七类下游任务：中文单句分类（头条 15 类）、MNLI 句对推理、SWAG 多选、SQuAD 问答、NSP/MLM 预训练与中文命名实体识别，并附带各任务原理讲解。仓库内置 bert_base_chinese 与 bert_base_uncased_english 预训练配置及对应数据集目录，使用时下载数据与预训练模型放入相应目录后，进入 Tasks 目录运行各任务脚本即可训练与推理。环境要求 Python 3.6、torch 1.5.0、torchtext 0.6.0 等，属于学习用途的完整实现工程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现 BERT 基础模型（Embedding/Self-Attention/NSP/MLM）
- 覆盖 7 类下游任务：分类、MNLI、SWAG、SQuAD、NER、预训练
- 内置中英文预训练模型配置与各任务数据集目录
- README 附各任务运行命令与训练/推理日志示例（如 SQuAD F1 88.3）

## 适用场景

- 跟随讲解学习 BERT 原理与 Transformer 实现细节
- 在中文分类、NER、SQuAD 问答等任务上训练微调 BERT
- 基于 NSP/MLM 在 WikiText 或宋词语料上从头预训练中文模型

## 场景标签

`教程课程` `微调` · 领域:学习与行业

## 证据(README 行号)

> L5: This project is an implementation of the BERT model and its related downstream tasks based on the PyTorch framework.
> L9: Before learning to use this project, you need to know the relevant principles of Transformer by these three examples

## 星数曲线

```mermaid
xychart-beta
    title "mlwithme/BertWithPretrained 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 601 --> 603
    line [602, 602]
```

2026-10-18 602 → 2026-10-30 602（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `088940883cab` · [字段定义](../../DATASET.md)*
