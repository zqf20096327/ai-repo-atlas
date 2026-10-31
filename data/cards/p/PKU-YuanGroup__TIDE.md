# PKU-YuanGroup/TIDE

⭐ 71 · Python · NOASSERTION · 推送 2026-04-30 · [GitHub](https://github.com/PKU-YuanGroup/TIDE) · [官网](https://arxiv.org/abs/2604.26951) · 组织维护 · 中文 README

**面向扩散语言模型的跨架构蒸馏训练框架（论文官方实现）**

北京大学与浙江大学团队的论文官方实现：将 8B dense / 16B MoE 的扩散语言模型教师蒸馏到 0.6B 学生模型，跨架构、跨注意力机制、跨分词器，由 TIDAL、CompDemo、Reverse CALM 三个模块组成。提供两条流水线的预处理、蒸馏训练与 8 基准评测脚本，默认配置需多 GPU（--num_gpus 默认 8，论文实验在 H100 上进行），并在 Hugging Face 发布 6 个蒸馏后学生检查点与 2 个预处理数据集。限制：需离线预处理数据以避免 NCCL 超时，aligned 模式对预处理参数有硬性约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨架构/跨分词器蒸馏：TIDAL 调度、CompDemo 互补掩码、Reverse CALM 三模块
- 两条流水线（LLaDA2→Qwen3-0.6B、WeDLM→Qwen3-0.6B）的完整训练与评测脚本
- 发布 6 个蒸馏学生检查点与 2 个预处理 SFT 数据集
- 8 个基准评测脚本（GSM8K/MATH/BBH/HumanEval 等）

## 适用场景

- 复现论文中的扩散语言模型蒸馏实验
- 将大型 dLLM 教师蒸馏为小模型以降低显存与推理开销
- 对蒸馏后的 0.6B 学生模型跑 8 个基准评测

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L19: This repository is the official implementation of TIDE , the first framework for cross-architecture dLLM distillati
> L5:  🌊 The first cross-architecture distillation framework for diffusion LLMs — 8B dense and 16B MoE teachers into a 0.6
> L9:  1 Peking University &nbsp;·&nbsp; 2 Zhejiang University &nbsp; ( * corresponding author)

## 星数曲线

```mermaid
xychart-beta
    title "PKU-YuanGroup/TIDE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-31 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ea9f76cc20da` · [字段定义](../../DATASET.md)*
