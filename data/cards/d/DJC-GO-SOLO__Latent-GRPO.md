# DJC-GO-SOLO/Latent-GRPO

⭐ 22 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/DJC-GO-SOLO/Latent-GRPO) · 组织维护

**词表空间潜推理的 GRPO 强化学习训练框架官方实现**

论文 Latent-GRPO 的官方代码库，将对词汇空间潜链推理的研究从监督微调扩展到强化学习阶段。仓库提供定制化 SGLang 推理引擎（支持潜 token rollout）、基于 verl-0.4.x 修改的训练栈、低/高难度训练脚本、jsonl 转 parquet 的数据预处理脚本及评测脚本。训练要求从 Latent-SFT 初始化的潜推理检查点启动，直接对未初始化模型做潜 RL 会不稳定。发布 LLaMA3.2-1B 与 Qwen2.5-Math-7B 两组检查点与训练数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定制 SGLang 引擎支持潜 token rollout（Top-k 词汇叠加 + Gumbel-Softmax 采样）
- 基于 verl-0.4.x 修改的 Latent-GRPO 训练管线，含低/高难度脚本
- 支持 GSM8K-Aug、Math-500、AIME-2024/2025、GPQA 等基准评测
- 发布可直接评测的 Latent-GRPO 检查点与 Hugging Face 数据集

## 适用场景

- 对 Latent-SFT 初始化的潜推理模型做 GRPO 强化学习
- 复现论文中的低/高难度数学推理训练与评测
- 将自有 jsonl 数据转为 verl 格式用于潜推理 RL 训练

## 场景标签

`强化学习` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10:  Official implementation of Latent-GRPO, an RL-stage framework for optimizing vocabulary-space latent reasoning.
> L16: - **Code release**: This repository provides the data preparation scripts, customized SGLang rollout engine, verl-b
> L25: - A modified verl-0.4.x training stack for Latent-GRPO.

## 星数曲线

```mermaid
xychart-beta
    title "DJC-GO-SOLO/Latent-GRPO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `716f5346273f` · [字段定义](../../DATASET.md)*
