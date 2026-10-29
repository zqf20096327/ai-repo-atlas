# NVlabs/DLER

⭐ 21 · Python · NOASSERTION · 推送 2025-11-11 · [GitHub](https://github.com/NVlabs/DLER) · 组织维护

**RL 训练方法：压缩推理链长度且保持准确率**

NVIDIA 研究团队提出的强化学习训练方法 DLER，通过长度惩罚机制压缩大模型 Chain-of-Thought 推理链：在 DeepSeek-R1-1.5B/7B 上训练出的模型，在 MATH、AIME-24、AMC、Minerva、Olympiad 五个基准上压缩响应长度约 70%（1.5B 模型平均长度降至 2,466 token）而不损失准确率。仓库提供 Hugging Face 模型、基于 VERL 的训练实现（verl-dler），训练环境通过外部指引安装，并给出 SLURM 脚本示例。面向希望缩短推理输出的研究者和开发者。

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

- RL 长度惩罚方法，压缩 CoT 约 70% 不损失准确率
- 在五个数学推理基准上压缩推理轨迹
- 提供基于 VERL 的训练实现 verl-dler
- 基于 DeepSeek-R1-1.5B/7B 训练的模型在 Hugging Face 发布

## 适用场景

- 我想缩短推理模型的输出长度以降低推理成本
- 复现或扩展推理压缩的 RL 训练方法
- 在数学推理任务上对比长度-精度平衡方案

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L9: DLER is an simple RL training approach that delivers state-of-the-art accuracy and response-length balance, reducing
> L13: DLER surpasses previous state-of-the-art reasoning compression methods across five benchmarks—MATH, AIME-24, AMC, M

## 星数曲线

```mermaid
xychart-beta
    title "NVlabs/DLER 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7d7618d3f63b` · [字段定义](../../DATASET.md)*
