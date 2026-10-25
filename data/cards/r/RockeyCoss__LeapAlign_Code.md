# RockeyCoss/LeapAlign_Code

⭐ 61 · Python · Apache-2.0 · 推送 2026-06-13 · [GitHub](https://github.com/RockeyCoss/LeapAlign_Code) · [官网](https://arxiv.org/abs/2604.15311) · 组织维护

**流匹配模型的后训练对齐方法：构建两步轨迹优化任意生成步**

CVPR2026 论文的官方 PyTorch 实现，来自 ANU 与 ByteDance Seed。LeapAlign 通过奖励梯度经可微生成过程反向传播，使流匹配模型对齐人类偏好；核心机制是构建两步 leap 轨迹代替完整采样轨迹反传梯度，规避显存压力与梯度爆炸，使梯度可传播到任意生成步。提供 Conda 环境搭建脚本、多机多卡训练脚本（默认 2 节点×8 GPU）、HPDv2/GenEval 评测流程，并在 Hugging Face Hub 发布基于 FLUX.1-dev 微调的推理 checkpoint，可通过 diffusers FluxPipeline 加载推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两步 leap 轨迹反传奖励梯度，覆盖任意生成步
- 基于 FLUX.1-dev 的后训练，使用 HPSv2.1/HPSv3 奖励
- 发布 3 个微调后的 FLUX checkpoint，diffusers 可加载推理
- 提供多机多卡训练与 HPDv2/GenEval 评测脚本

## 适用场景

- 对齐文本到图像的流匹配模型以符合人类偏好
- 复现论文的 HPDv2/GenEval 评测结果
- 直接下载微调 checkpoint 用 diffusers 做文生图推理

## 场景标签

`微调` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: ## LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories Official P
> L17: LeapAlign is a post-training method for aligning flow matching models with human preferences by backpropagating rew
> L123: We release **FLUX checkpoints fine-tuned with LeapAlign** on the Hugging Face Hub. All checkpoints are trained by 

## 星数曲线

```mermaid
xychart-beta
    title "RockeyCoss/LeapAlign_Code 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-25 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8d89e2a008f9` · [字段定义](../../DATASET.md)*
