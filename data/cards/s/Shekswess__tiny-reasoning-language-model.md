# Shekswess/tiny-reasoning-language-model

⭐ 53 · Python · 推送 2025-11-24 · [GitHub](https://github.com/Shekswess/tiny-reasoning-language-model) · [官网](https://huggingface.co/collections/Shekswess/tiny-reasoning-language-model-68d924929c17ad8300544ae4) · 个人维护

**135M 小模型逐步推理训练的开源研究流水线**

基于 SmolLM2-135M-Instruct 的后训练研究项目：三阶段流水线（非推理 SFT、带 <think> 标签的推理 SFT、DPO 偏好对齐），配套 YAML 驱动的数据集构建脚本，可流式拉取清洗数据并推送至 Hugging Face Hub，权重与数据集全部公开。训练主要面向 AMD ROCm 硬件（在单卡 MI300x 上完成），提供 cpu 可选依赖。README 声明为研究原型，不适用于日常应用，存在能力受限与幻觉倾向。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三阶段后训练：非推理 SFT → 推理 SFT → DPO
- YAML 配置驱动的数据集构建管线，支持流式下载与自动推送 Hub
- lm-eval-harness 多基准评测，与 SmolLM2-135M-Instruct 基线对比
- 全部阶段权重与数据集发布于 Hugging Face Collection

## 适用场景

- 研究者复现小模型推理能力训练的完整流程
- 参考小模型的 SFT/DPO 数据配比与超参设置
- 改造流水线用于其他底座模型的后训练实验

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: Tiny Reasoning Language Model (trlm) is an open pipeline for teaching a 135M-parameter SmolLM2 based model to handle
> L11: The code is mainly designed to run on AMD (ROCm) hardware and to publish intermediate artefacts to the Hugging Face
> L15: > The current model is not intended to be used in everyday applications. It is a research prototype and should be t

## 星数曲线

```mermaid
xychart-beta
    title "Shekswess/tiny-reasoning-language-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `abfde4b4783e` · [字段定义](../../DATASET.md)*
