# PaccMann/paccmann_predictor

⭐ 53 · Python · MIT · 推送 2026-02-11 · [GitHub](https://github.com/PaccMann/paccmann_predictor) · 组织维护

**药物相互作用预测的 PyTorch 库：抗癌药敏感性与药物靶点亲和力**

PaccMann 的 PyTorch 实现，用于药物相互作用预测，包含抗癌药物敏感性（IC50）预测与药物-靶点结合亲和力预测两类任务。模型读取 SMILES 分子结构与基因表达/蛋白序列等多模态数据，基于多尺度卷积编码器与注意力机制输出预测。提供预训练模型下载，支持在自有数据上评估、微调或从零训练；自带数据需包含 2128 个指定基因的组学数据。面向计算药物研发的科研用户，以 Python 库与示例脚本形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 药物敏感性（IC50）与药物-靶点亲和力双任务预测
- 多模态输入：SMILES、基因表达谱、蛋白序列
- 支持预训练模型评估、微调与从零训练
- 基于多尺度卷积编码器与双模态注意力

## 适用场景

- 用预训练模型预测抗癌化合物对细胞系的敏感性
- 预测药物与靶蛋白的结合亲和力
- 在自有组学数据上微调药物敏感性模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: `paccmann_predictor` is a package for drug interaction prediction, with examples of
> L11: - _Toward explainable anticancer compound sensitivity prediction via multimodal attention-based convolutional encod
> L14: - Data-driven molecular design for discovery and synthesis of novel ligands: a case study on SARS-CoV-2 (_Machine L

## 星数曲线

```mermaid
xychart-beta
    title "PaccMann/paccmann_predictor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-27 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `41b34976f6dc` · [字段定义](../../DATASET.md)*
