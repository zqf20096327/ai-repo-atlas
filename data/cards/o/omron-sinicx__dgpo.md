# omron-sinicx/dgpo

⭐ 13 · Python · NOASSERTION · 推送 2026-07-26 · [GitHub](https://github.com/omron-sinicx/dgpo) · [官网](https://omron-sinicx.github.io/dgpo) · 组织维护

**面向研究者的训练方法代码：蒸馏引导强化学习保留小型模型 agentic RAG 能力**

ACL 2026 论文 DGPO 的官方实现：针对 0.5B 级紧凑模型在 agentic RAG 强化学习训练中奖励稀疏、训练不稳定的问题，采用教师示范冷启动初始化与训练过程中的持续教师引导。提出 ARCap 细粒度评估指标，分析推理、检索协调与回答合成能力。基于 Search-R1、veRL、RAGEN 实现，以 Pixi 管理环境，需下载 133.66GB 检索索引与语料及 HuggingFace 数据集，含训练与推理任务命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 教师示范冷启动初始化 + 策略优化中的持续教师引导
- ARCap 细粒度指标：评估推理、检索协调与回答合成
- 基于 Pixi 的任务化训练/推理流程（基于 Search-R1、veRL、RAGEN 实现）

## 适用场景

- 复现论文中紧凑模型的 agentic RAG 训练
- 用自选蒸馏方法做冷启动初始化后训练 agentic LLM
- 用 ARCap 指标评估 agentic RAG 模型能力

## 场景标签

`RAG` `强化学习` · 领域:知识与检索

## 证据(README 行号)

> L19: To overcome these difficulties, we propose Distillation-Guided Policy Optimization (DGPO), which addresses the chal
> L21: Comprehensive experiments demonstrate that DGPO enables compact models to achieve sophisticated agentic search beha
> L114: Implementation is built upon Search-R1, veRL, and RAGEN.

## 星数曲线

```mermaid
xychart-beta
    title "omron-sinicx/dgpo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f8f663a6b9d5` · [字段定义](../../DATASET.md)*
