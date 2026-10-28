# Haochen-Wang409/TreeVGR

⭐ 93 · Python · Apache-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/Haochen-Wang409/TreeVGR) · [官网](https://arxiv.org/pdf/2507.07999) · 组织维护

**视觉定位推理评测基准 TreeBench 及训练范式 TreeVGR（ICLR'26）**

论文配套仓库，包含两部分：TreeBench，面向“thinking with images”能力的诊断基准，从 SA-1B 抽样 1K 图像、经 8 个 LMM 专家人工标注与三阶段质量控制，构成 405 个视觉问答对，通过边界框评估与二阶推理考察可追溯视觉证据；TreeVGR，基于 Qwen2.5-VL-7B 初始化的训练范式，用强化学习（RL）联合监督定位与推理。仓库提供本地推理演示脚本，基准、模型权重（TreeVGR-7B 及 CI 版）与训练数据集（RL-37K/SFT-35K）发布在 Hugging Face。安装依赖 requirements.txt 与 flash-attn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TreeBench：405 个视觉问答对，边界框评估与二阶推理
- TreeVGR-7B 基于 Qwen2.5-VL-7B，RL 联合训练定位与推理
- 提供 TreeVGR-RL-37K 与 TreeVGR-SFT-35K 训练数据集
- 已被 VLMEvalKit 支持并被 GLM-4.5V 使用 TreeBench

## 适用场景

- 评测多模态模型的 thinking with images 与视觉定位推理能力
- 复现 TreeVGR 推理结果或获取模型权重
- 使用其 RL/SFT 数据集训练视觉定位推理模型

## 场景标签

`模型评测` `多模态` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L12: **TL; DR**: We propose TreeBench, the first benchmark specially designed for evaluating "thinking with images" capa
> L25: > (Traceable Evidence Enhanced Visual Grounded Reasoning), a training paradigm to supervise
> L27: > explainable reasoning pathways. Initialized from Qwen2.5-VL-7B, it improves V* Bench (+16.8),

## 星数曲线

```mermaid
xychart-beta
    title "Haochen-Wang409/TreeVGR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-28 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `98cc017d0880` · [字段定义](../../DATASET.md)*
