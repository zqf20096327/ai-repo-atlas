# BiomedSciAI/biomed-multi-omic

⭐ 63 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/BiomedSciAI/biomed-multi-omic) · [官网](https://research.ibm.com/projects/biomedical-foundation-models) · 组织维护

**构建与运行 RNA/DNA 组学基础模型的 Python 框架**

IBM 相关团队（BiomedSciAI）维护的生物医学基础模型包：支持 scRNA 与 DNA 序列两类数据的基础模型开发、预训练与微调，通过声明式无代码接口配置模块化的模型与训练方法。RNA 侧从 h5ad/TileDB 读取数据，DNA 侧在参考基因组（GRCh38）与 SNP 变异基因组上预训练；提供零样本与微调的下游任务（细胞类型注释、扰动预测、启动子预测等），模型权重托管在 HuggingFace，可用 vLLM 插件做推理。安装从源码克隆并用 uv/pip 完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一包同时支持 scRNA 与 DNA 基础模型的预训练/微调
- 声明式无代码接口控制模型与训练配置
- RNA/DNA 检查点托管于 HuggingFace（BERT/LLaMA/ModernBERT 架构）
- vLLM 插件用于 biomed-rna 模型推理

## 适用场景

- 在自有 scRNA 数据上预训练或微调转录组学基础模型
- 对 h5ad 数据做零样本细胞类型注释与嵌入提取
- 在参考/SNP 基因组上训练 DNA 语言模型并做启动子活性预测
- 用 GUE 基准对 DNA 基础模型做评测对比

## 场景标签

`模型训练` `微调` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Biomedical foundational models for omics data. This package supports the development of foundation models for scRNA 
> L5: `biomed-multi-omic` enables development and testing of foundation models for DNA sequences and for RNA expression,
> L11: - 📈 Zero-shot and finetuning support for diverse downstream tasks: (cell type annotation, perturbation prediction f

## 星数曲线

```mermaid
xychart-beta
    title "BiomedSciAI/biomed-multi-omic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-27 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ef93ba90d585` · [字段定义](../../DATASET.md)*
