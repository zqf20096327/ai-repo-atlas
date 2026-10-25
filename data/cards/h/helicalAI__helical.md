# helicalAI/helical

⭐ 235 · Python · AGPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/helicalAI/helical) · [官网](https://www.helical-ai.com/) · 组织维护

**给计算生物学家：统一 Python 接口调用生物基础模型**

面向计算生物学家、科研人员与 AI 开发者的开源框架，提供基因组学、转录组学与单细胞数据模态上多种预训练生物基础模型（Helix-mRNA、Geneformer、scGPT、HyenaDNA、Evo2、Tahoe-x1 等）的统一访问接口，覆盖模型调用、微调、嵌入提取与在硅实验的完整生命周期，并附带示例 notebook 与 Colab 教程。以 pip 包安装，部分模型（mamba-ssm、Evo2、Tahoe）需 GPU/CUDA 及额外安装步骤，也提供可选的 Singularity/Apptainer 容器方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 接入 RNA 与 DNA 两类多个生物基础模型
- 支持微调、嵌入提取与下游任务（细胞类型注释、药物扰动预测等）
- 自带示例 notebook 与 Colab 教程
- 可选 Apptainer/Singularity 容器运行方式

## 适用场景

- 用统一接口对单细胞 RNA 数据提取细胞/基因嵌入
- 在自有数据集上微调生物基础模型做分类任务
- 对比不同 Geneformer 规模在药物扰动预测上的表现

## 场景标签

`科研工具` `微调` · 领域:学习与行业

## 证据(README 行号)

> L10: This open framework provides access to state-of-the-art Bio Foundation Models across genomics, transcriptomics, and
> L12: Helical simplifies the entire lifecycle of applying Bio Foundation Models — from model access to fine-tuning and in
> L191: - A unified API for all models

## 星数曲线

```mermaid
xychart-beta
    title "helicalAI/helical 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 233 --> 236
    line [234, 235, 235]
```

2026-10-18 234 → 2026-10-25 235（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7b3a14b2169c` · [字段定义](../../DATASET.md)*
