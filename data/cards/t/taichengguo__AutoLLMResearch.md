# taichengguo/AutoLLMResearch

⭐ 16 · Python · 推送 2026-05-12 · [GitHub](https://github.com/taichengguo/AutoLLMResearch) · [官网](https://arxiv.org/abs/2605.11518) · 个人维护

**训练可自动提出 LLM 实验配置的强化学习 agent 研究代码**

论文官方代码：训练一个 RL 驱动的 LLM agent，为语言模型训练任务提出超参数、数据配比、模型架构与 RL 超参数配置。三阶段流程：LMConfigGym 离线基准模拟环境、基于 LlamaFactory 的策略蒸馏 SFT 预热（Qwen3-1.7B/4B）、基于 verl + SGLang 的多轮 GRPO 强化学习。评测数据来自 HW-GPT-Bench、StepLaw、ADMIRE-BayesOpt 与 RegMix。硬件要求 ≥4× 80GB GPU，脚本中含需填充的路径占位符。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LMConfigGym 提供 4 个任务（RL 调参/架构/数据配比/指令微调）的 gym 式离线环境
- 三阶段训练：环境模拟 → 策略蒸馏 SFT → 多轮 GRPO（verl + SGLang）
- 测试 Qwen3-1.7B/4B/8B/14B 作为基础模型
- 提供验证、训练集评测与 best-of-N 轨迹合成脚本

## 适用场景

- 复现论文中配置推荐 agent 的训练流程
- 在离线基准数据上做 LLM 配置优化实验
- 基于 verl/SGLang 框架扩展多轮工具增强 RL 研究

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: AutoLLMResearch is an RL-trained LLM agent that proposes configurations (hyperparameters, data mixtures, model archi
> L56: ### 3. Multi-Turn RL — GRPO on top of verl
> L88: Hardware: RL configs assume ≥4× GPUs (80GB class; adjust `trainer.n_gpus_per_node`, `*.ppo_micro_batch_size_per_gpu

## 星数曲线

```mermaid
xychart-beta
    title "taichengguo/AutoLLMResearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f835d0884a55` · [字段定义](../../DATASET.md)*
