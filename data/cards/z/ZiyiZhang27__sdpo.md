# ZiyiZhang27/sdpo

⭐ 22 · Python · MIT · 推送 2026-02-25 · [GitHub](https://github.com/ZiyiZhang27/sdpo) · [官网](https://arxiv.org/abs/2411.11727) · 组织维护

**少步扩散模型对齐的强化学习训练框架（TPAMI 论文代码）**

SDPO 的 PyTorch 官方实现，论文发表于 IEEE TPAMI。面向少步扩散模型（如 SD-Turbo）的下游目标对齐：引入双状态轨迹采样（同时跟踪噪声态与预测干净态）提供密集奖励反馈与低方差混合步优化；用潜在相似度的密集奖励预测减少奖励查询次数；优化密集奖励差分学习目标，并含逐步优势估计、时间重要性加权与步乱序梯度更新。预置 Aesthetic Score、ImageReward、HPSv2、PickScore 四种奖励函数配置，默认配置面向 4× 24GB+ GPU。通过 git clone 加 conda 环境安装，用 accelerate 启动训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双状态轨迹采样提供密集奖励反馈与低方差混合步优化
- 潜在相似度密集奖励预测减少奖励查询成本
- 预置 Aesthetic/ImageReward/HPSv2/PickScore 四种奖励配置
- 默认配置针对 4× 24GB+ 显存 GPU，可用配置文件调参

## 适用场景

- 对少步文生图扩散模型做奖励对齐微调
- 复现论文中 SD-Turbo 等少步设置的训练实验
- 替换不同奖励函数研究扩散模型偏好对齐

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains a PyTorch implementation of **Stepwise Diffusion Policy Optimization (SDPO)**, as presented
> L11: **SDPO** is a novel reinforcement learning framework tailored for aligning few-step diffusion models with downstrea

## 星数曲线

```mermaid
xychart-beta
    title "ZiyiZhang27/sdpo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ec3a94282e3e` · [字段定义](../../DATASET.md)*
