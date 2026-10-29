# LingFengGold/STReasoner

⭐ 57 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/LingFengGold/STReasoner) · [官网](https://arxiv.org/pdf/2601.03248) · 组织维护

**面向时序时空推理的 LLM 训练框架（SFT+RL 三阶段）**

ACL 2026 Oral 论文的官方实现：通过三阶段流程（时序对齐 SFT、冷启动推理 SFT、基于 S-GRPO 的空间感知强化学习）训练带时序编码器的 LLM，支持 Qwen3-8B/4B/14B、Qwen2.5-14B-Instruct 等基座。附带 ST-Bench 时空推理基准、数据合成流水线与推理/评测脚本；RL 阶段在 verl Docker 容器内运行，硬件要求为 8×A100-80GB。面向时序大模型方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SFT+S-GRPO 强化学习三阶段训练流水线
- LLM 与专用时序编码器结合，支持多款 Qwen 基座
- ST-Bench 多模态时空推理基准与评测脚本
- Network SDEs 多智能体时空数据合成流水线

## 适用场景

- 训练自己的时序推理 LLM 并复现论文流程
- 在 ST-Bench 上评测时空推理任务
- 生成时空合成训练数据

## 场景标签

`强化学习` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L19: - 🚀 **Full Training Pipeline** — First SFT + RL training pipeline for LLM with time series encoder
> L30: **STReasoner** is a framework designed for spatio-temporal reasoning in time series data, trained through a careful

## 星数曲线

```mermaid
xychart-beta
    title "LingFengGold/STReasoner 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-29 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d73c5099de63` · [字段定义](../../DATASET.md)*
