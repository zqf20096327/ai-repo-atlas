# shehzaadzd/MINERVA

⭐ 322 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/shehzaadzd/MINERVA) · 组织维护

**知识图谱上做强化学习路径推理的问答 agent 代码库**

ICLR 2018 论文《Go for a Walk and Arrive at the Answer》的官方代码与预训练模型。MINERVA 是一个强化学习 agent：从查询实体节点出发，在实体-关系知识图谱中学习条件于输入查询的路径导航，到达答案实体。提供 pip 依赖安装、run.sh 脚本训练、预训练模型加载与 Hits@k/MRR 评估输出，支持自定义三元组格式数据集。基于 TensorFlow 实现。

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

- 在知识图谱上按查询条件导航到答案实体的 RL agent
- 提供预训练模型可直接用于查询回答
- 输出 Hits@{1,3,5,10,20} 与 MRR（Countries 为 AUC-PR）评估
- 支持自定义 (e1, r, e2) 三元组格式数据集

## 适用场景

- 在知识图谱数据集上训练与评估路径推理问答
- 用预训练模型直接做知识图谱查询回答
- 复现论文实验结果

## 场景标签

`知识图谱` `强化学习` · 领域:知识与检索

## 证据(README 行号)

> L4: Code and models for the paper Go for a Walk and Arrive at the Answer - Reasoning over Paths in Knowledge Bases using
> L8: MINERVA is a RL agent which answers queries in a knowledge graph of entities and relations. Starting from an entity 

## 星数曲线

```mermaid
xychart-beta
    title "shehzaadzd/MINERVA 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 321 --> 323
    line [322, 322]
```

2026-10-29 322 → 2026-10-30 322（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `11510356da2d` · [字段定义](../../DATASET.md)*
