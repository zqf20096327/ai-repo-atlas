# verl-project/laminar

⭐ 13 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/verl-project/laminar) · [官网](https://doi.org/10.1145/3767295.3803580) · 组织维护

**面向 LLM 与长程 agent 的可扩展 RL 后训练框架**

基于 verl 与 Uni-Agent 构建的强化学习后训练框架，将 rollout 与训练解耦为独立循环：数据平面（ExperienceBuffer）缓存轨迹供训练器采样，权重平面（Relay）通过 UCX/NCCL 发布权重供推理副本拉取。支持轨迹级异步、版本混合/一致 rollout、动态 repack 与多检查点并发评估，并提供故障恢复以避免单副本失败阻塞集群。README 给出 SWE agent 训练配方与基准结果，通过 uv 管理依赖，训练后端可选 Megatron-LM 或 FSDP2，推理后端为 vLLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- rollout 与训练完全解耦：数据平面与权重平面无同步步障
- 轨迹级异步：版本混合部分 rollout 与版本一致 rollout 两种模式
- 多检查点并发评估（laminar.eval）与动态 repack
- 故障容忍执行：推理副本与训练器均可恢复

## 适用场景

- 在大规模集群上对 LLM 或 agent 做 RL 后训练
- 训练 SWE agent 并在 SWE-bench Verified 上评估
- 需要异步 RL 训练与推理副本解耦的场景

## 场景标签

`强化学习` `模型训练` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Laminar is a scalable reinforcement learning (RL) post-training framework for large language models (LLMs) and long-
> L48:  - **verl**: Distributed model training (Megatron-LM, FSDP2) and inference (vLLM) backends.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `75ee8652ab87` · [字段定义](../../DATASET.md)*
