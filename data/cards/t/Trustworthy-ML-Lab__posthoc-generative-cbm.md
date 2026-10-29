# Trustworthy-ML-Lab/posthoc-generative-cbm

⭐ 21 · Jupyter Notebook · 推送 2026-07-13 · [GitHub](https://github.com/Trustworthy-ML-Lab/posthoc-generative-cbm) · [官网](https://lilywenglab.github.io/posthoc-generative-cbm/) · 组织维护

**CVPR 2025 论文官方代码：将预训练生成模型事后改造为可解释概念瓶颈模型**

Trustworthy ML Lab 发布的 CVPR 2025 论文官方仓库，实现 CB-AE 与 Concept Controller 两种方法：在冻结的预训练图像生成模型（StyleGAN2、DDPM 等）上构建事后可解释的概念瓶颈层，无需真实概念标注图像即可训练。提供概念干预、可控生成、概念预测可视化及可控性定量评测脚本。通过 conda 环境安装，依赖 CUDA 与 GPU，需下载预训练基模型与检查点，面向复现论文与研究生成模型可解释性的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CB-AE：冻结预训练生成模型上事后构建概念瓶颈，无需真实概念标注图像
- Concept Controller：基于优化的概念干预方法，提升可控性
- 支持 StyleGAN2 与 DDPM 等生成模型，提供训练/评测/演示脚本
- 提供 CelebA-HQ、CUB 预训练权重与概念分类器下载

## 适用场景

- 复现 CVPR 2025 论文的概念干预与可控性评测
- 研究生成模型的可解释性与事后概念瓶颈方法
- 对生成图像做概念级干预实现可控生成

## 场景标签

`科研工具` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: This is the official repository for the **CVPR 2025** paper: Interpretable Generative Models through Post-hoc Concep
> L8:  * **CB-AE**: The 1st method for post-hoc interpretable generative models. **CB-AE** can be trained efficiently with

## 星数曲线

```mermaid
xychart-beta
    title "Trustworthy-ML-Lab/posthoc-generative-cbm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dfed66108b6f` · [字段定义](../../DATASET.md)*
