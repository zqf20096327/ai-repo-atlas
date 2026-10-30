# TIGER-AI-Lab/VisualWebInstruct

⭐ 39 · Python · MIT · 推送 2026-02-01 · [GitHub](https://github.com/TIGER-AI-Lab/VisualWebInstruct) · [官网](https://tiger-ai-lab.github.io/VisualWebInstruct/) · 组织维护

**经网络搜索构建的约 90 万条多模态推理指令数据集与配套训练管线**

EMNLP25 论文 VisualWebInstruct 的官方仓库：以 3 万张种子图像出发，通过 Google 图片搜索定位相似网页，采集并处理 70 余万独立 URL 的 HTML，经内容抽取、过滤与合成流水线生成约 90 万问答对（40% 为视觉 QA），覆盖数学（62.5%）、物理、金融、化学等学科。仓库同时提供数据处理流水线（两阶段）、基于 MAmmoTH-VL 代码库的微调脚本（Qwen2.5-7B + SigLIP，DeepSpeed ZeRO-3）与 lmms-eval 评测代码，数据与模型托管在 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 900K 问答对，40% 为视觉 QA，来自 700K+ URL 源
- 两阶段流水线：网络数据挖掘 + 答案一致性与对齐校验精炼
- 提供 MAmmoTH-VL 微调与 lmms-eval 评测完整脚本
- 产出模型 MAmmoTH-VL2，提供预训练权重与 HF Space

## 适用场景

- 为视觉语言模型微调获取跨学科推理指令数据
- 复现论文的数据构建与训练评测流程
- 在 MMMU-Pro、MathVerse、DynaMath 等基准上评测自训模型

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L33: Vision-Language Models have made significant progress on many perception-focused tasks, however, their progress on 
> L88: The VisualWebInstruct dataset is available on Hugging Face.

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/VisualWebInstruct 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f46f330f203e` · [字段定义](../../DATASET.md)*
