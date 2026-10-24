# instadeepai/nucleotide-transformer

⭐ 927 · Jupyter Notebook · NOASSERTION · 推送 2026-02-24 · [GitHub](https://github.com/instadeepai/nucleotide-transformer) · 组织维护

**基因组学 AI 基础模型集合：DNA/RNA 序列预测与嵌入**

InstaDeep 维护的基因组学深度学习模型仓库，收录 Nucleotide Transformer v3（多物种基础模型，支持功能轨道预测、基因组注释与可控序列生成）、AgroNT（48 种植物基因组）、SegmentNT（单核苷酸分辨率基因组分割）、ChatNT（DNA 对话代理）及 Isoformer、sCT、BulkRNABert、MOJO 等转录组学模型。提供预训练权重（托管于 Hugging Face）、推理代码、微调与推理 Notebook。基于 Jax，Python 3.8，从源码克隆后 pip 安装；许可证为 CC BY-NC-SA 4.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NTv3 支持 1 Mb 长上下文单碱基分辨率建模与可控序列生成
- 模型家族覆盖 DNA 语言模型、基因组分割与单细胞/批量转录组学
- 提供 Hugging Face 预训练权重与微调/推理 Notebook
- 各模型附带论文出处（Nature Methods、NeurIPS 等）

## 适用场景

- 对 DNA/RNA 序列做功能预测与基因组注释
- 获取基因组序列嵌入用于下游分析
- 设计具指定活性水平的增强子序列
- 单细胞与批量 RNA-seq 数据的表示学习

## 场景标签

 · 领域:生命科学/AI 基础模型

## 证据(README 行号)

> L19: Welcome to the InstaDeep AI for Genomics repository! This is where we feature our collection of transformer-based g
> L31: A unified multi-species foundation model that integrates representation learning, functional-track and genome-annot
> L98: Our foundational transformer model for single-cell and spatial transcriptomics data. sCT aims to learn rich represe

## 星数曲线

```mermaid
xychart-beta
    title "instadeepai/nucleotide-transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 925 --> 928
    line [926, 927]
```

2026-10-18 926 → 2026-10-24 927（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `71091395d86c` · [字段定义](../../DATASET.md)*
