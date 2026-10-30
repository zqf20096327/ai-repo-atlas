# gemma-facet/cloud-services

⭐ 16 · Python · MIT · 推送 2025-11-27 · [GitHub](https://github.com/gemma-facet/cloud-services) · [官网](https://facetai.mintlify.app) · 组织维护

**面向非技术用户的 Gemma 3 微调无代码 Web 平台（GSoC'25）**

由两名 Google Summer of Code 学生在 DeepMind 开发的开源无代码 Web 平台，管理 Gemma 3 系列多模态模型微调全流程：数据预处理（本地文件与 Hugging Face）、数据增强、SFT/DPO/ORPO/GRPO 训练、LoRA/QLoRA 量化、模型导出（GGUF、Hub、GCS）、评测与一键部署到 GCP Cloud Run。100% IaC，可用 Terraform 单命令部署到自己的 Google Cloud 项目，也提供免费线上平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无代码管理 Gemma 3 文本与多模态微调全流程
- 支持 Transformers/Unsloth、SFT/DPO/ORPO/GRPO、LoRA/QLoRA 量化
- 模型导出为 Adapters/合并/量化/GGUF 并一键部署 GCP Cloud Run
- 100% IaC，Terraform 单命令部署到自有 Google Cloud 项目

## 适用场景

- 不写代码就能微调 Gemma 3 模型
- 集中管理多数据集、多模型的微调实验
- 微调完成后直接导出 GGUF 或部署到 GCP 做推理

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: Developed by two Google Summer of Code students at DeepMind, Facet AI is a no-code web platform to manage the fine-t
> L9: Cookbooks and Colab notebooks are amazing, except that they don't scale when you have multiple datasets, models, and

## 星数曲线

```mermaid
xychart-beta
    title "gemma-facet/cloud-services 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2d901478ed9a` · [字段定义](../../DATASET.md)*
