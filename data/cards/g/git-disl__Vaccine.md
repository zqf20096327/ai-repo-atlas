# git-disl/Vaccine

⭐ 54 · Shell · Apache-2.0 · 推送 2026-01-15 · [GitHub](https://github.com/git-disl/Vaccine) · [官网](https://arxiv.org/abs/2402.01109) · 组织维护

**面向有害微调攻击的 LLM 安全对齐训练方法（NeurIPS 2024）**

NeurIPS 2024 论文 Vaccine 的官方代码：实现一种扰动感知的安全对齐技术，防御用户微调阶段的安全风险。基于 HuggingFace Trainer 定制训练器（核心逻辑约 7 行代码），提供论文全部实验的复现脚本，支持 Slurm 或 bash 运行；使用 Llama2-7B 等门控模型需向 Meta 申请并配置 token。实验基于 H100/A100 40G 以上 GPU，消费级 GPU 需参考其另一仓库 T-Vaccine。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 HuggingFace Trainer 的定制训练器，核心逻辑约 7 行代码
- 覆盖对齐阶段与微调阶段的完整实验复现脚本
- 提供 harmful fine-tuning 防御效果评估工具
- 与同组 Booster/Lisa/Antidote 构成多阶段防御设计

## 适用场景

- 复现论文中的 Vaccine 对齐实验
- 评估模型在有害微调攻击下的安全性
- 与 SFT 基线对齐方法做实验对比

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: Code to replicate the Vaccine paper and tools for evaluating defense against harmful fine-tuning.
> L4: Vaccine is a perturbation-aware safety alignment for large language models (LLMs). The alignment technique is develo
> L10: We implement a customized trainer on top of the original HuggingFace Trainer. The main logistic is only 7 lines of 

## 星数曲线

```mermaid
xychart-beta
    title "git-disl/Vaccine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-27 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8e5e9f814002` · [字段定义](../../DATASET.md)*
