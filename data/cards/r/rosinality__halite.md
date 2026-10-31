# rosinality/halite

⭐ 14 · Python · MIT · 推送 2025-12-03 · [GitHub](https://github.com/rosinality/halite) · 个人维护

**LLM 训练/推理/评测一体化加速框架，支持 RLHF 后训练**

基于 PyTorch 从零构建的 LLM 加速框架，覆盖预训练、后训练（RLHF/PPO 等对齐技术）、推理与评测。核心机制：用 SlickConf 以 Python 代码定义配置，可在不改框架代码的情况下组合变换器组件、更换优化器；内置受 SGLang 启发的推理引擎，训练与推理模式可无成本切换；设计支持多维并行（不限于 FSDP）并以声明式方式转换其他框架的 checkpoint。作者声明为进行中项目，配置系统与框架紧耦合，上手门槛需注意。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- RLHF/PPO 等 LLM 后训练加速实现
- SlickConf 配置系统：配置内组合架构组件，无需框架级代码修改
- 内置推理引擎支持训练/推理模式免 checkpoint 切换
- 声明式转换其他框架的模型 checkpoint

## 适用场景

- 实现与加速 LLM 对齐/后训练实验
- 通过配置组合与修改新型 transformer 架构
- 在同一框架内完成采样推理与模型评测
- 小规模探索性预训练实验

## 场景标签

`模型训练` `强化学习` `推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Halite is an acceleration framework for pre-training, post-training, inference and evaluation of large language mode
> L7: - **Post-Training**: Halite starts from my earlier work for accelerating post-training of LLMs especially RLHF and P
> L10: - **Inference**: Most post-training method requires to sample from the model, a lot. It is crucial to sample effici

## 星数曲线

```mermaid
xychart-beta
    title "rosinality/halite 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a07822a52e68` · [字段定义](../../DATASET.md)*
