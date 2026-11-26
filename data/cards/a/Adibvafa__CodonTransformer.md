# Adibvafa/CodonTransformer

⭐ 230 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/Adibvafa/CodonTransformer) · [官网](https://adibvafa.github.io/CodonTransformer) · 个人维护

**多物种密码子优化深度学习模型：为蛋白表达生成宿主特异性 DNA 序列**

基于 Transformer（BigBird 架构）的密码子优化工具，训练数据来自 164 个物种、逾 100 万条 DNA-蛋白质对，输入蛋白序列后生成具有自然类似密码子分布的宿主特异性 DNA 序列。支持确定性解码与基于 temperature/top_p 的采样式生成，可批量推理、微调自有数据集，并经 HuggingFace 提供预训练模型与分词器；另提供 Google Colab 界面与 SLURM 微调脚本示例。Python>=3.9，跨主要操作系统运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 164 物种、100 万+ DNA-蛋白质对训练的多物种模型
- temperature/top_p 采样与 match_protein 约束的可控序列生成
- 支持自有 CSV 数据集微调，附 SLURM 作业示例
- 预训练模型与分词器从 HuggingFace 加载

## 适用场景

- 将目标蛋白序列优化为特定宿主（如大肠杆菌）偏好的 DNA 序列
- 为异源蛋白表达实验批量生成多条候选 DNA 序列
- 在自有物种数据上微调密码子优化模型

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L12: The genetic code is degenerate allowing a multitude of possible DNA sequences to encode the same protein. This dege
> L22: from CodonTransformer.CodonPrediction import predict_dna_sequence


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b30510798db1` · [字段定义](../../DATASET.md)*
