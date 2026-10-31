# mims-harvard/Madrigal

⭐ 45 · Jupyter Notebook · MIT · 推送 2026-09-19 · [GitHub](https://github.com/mims-harvard/Madrigal) · [官网](https://zitniklab.hms.harvard.edu/projects/Madrigal) · 组织维护

**多模态模型，从临床前数据预测药物联用效果**

哈佛团队发布的开源深度学习模型：整合分子结构图、知识图谱、细胞活力与转录组学等多模态临床前数据，预测药物组合（药对）的临床结局与不良事件，输出预测分数及其在 DrugBank 全药对中的归一化排名。提供 conda/mamba 环境安装、预训练 checkpoint 推理 notebook、三阶段训练 SLURM 脚本及论文复现图表 notebook。数据与模型经 Harvard Dataverse 分发，预计算预测分数文件达 80 GB；代码 MIT 许可，第三方数据集各有许可条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模态（结构图/知识图谱/细胞活力/转录组学）药物联用效果预测
- 三阶段训练：模态适配编码器、对比模态对齐、按结局微调
- 提供发布 checkpoint 的推理 notebook 与论文全图表复现 notebook
- 支持自定义数据集（binary/multiclass/multilabel 任务）

## 适用场景

- 对指定药对查询预测分数与排名
- 复现论文中药物联用安全性与疗效分析
- 在自己的药物组合数据集上微调训练
- 为临床试验联用方案做临床前风险预筛

## 场景标签

`多模态` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L5: Madrigal is an open-source model for predicting drug combination outcomes from multimodal preclinical data. This rep
> L61: - generate_embeddings.ipynb: compute drug embeddings and predicted scores for a checkpoint, convert them to normali

## 星数曲线

```mermaid
xychart-beta
    title "mims-harvard/Madrigal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6ef33e64412f` · [字段定义](../../DATASET.md)*
