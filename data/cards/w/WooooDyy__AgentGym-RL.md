# WooooDyy/AgentGym-RL

⭐ — · [GitHub]() · 组织维护

**多轮强化学习训练 LLM Agent 的框架（ICLR 2026 论文）**

论文 AgentGym-RL 的官方实现：通过多轮强化学习训练 LLM 智能体做长程决策。框架分环境、智能体、训练三模块，环境以服务器-客户端 HTTP 协议并行交互，涵盖 WebArena、Deep Search（基于 Search-R1）、TextCraft、BabyAI、SciWorld 五类场景。基于 verl 扩展（vllm 引擎 rollout），支持 PPO/GRPO/RLOO/REINFORCE++ 及 SFT/DPO/AgentEvol，提出渐进扩展交互轮数的 ScalingInter-RL 方法。推荐 CUDA 12.4 + PyTorch 2.4 + Python 3.10，训练数据与基准发布于 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模块化三组件：环境/智能体/训练，统一 HTTP 协议并行环境交互
- 五类真实场景环境：WebArena、Deep Search、TextCraft、BabyAI、SciWorld
- 支持 PPO/GRPO/RLOO/REINFORCE++ 在线 RL 与 SFT/DPO/AgentEvol
- ScalingInter-RL 渐进扩展交互轮数以平衡探索与利用

## 适用场景

- 用多轮 RL 训练 7B 级开源模型完成网页导航等长程任务
- 在自建环境上做 LLM Agent 的 RL 训练实验
- 复现论文在 WebArena 等基准上的评测结果

## 场景标签

`强化学习` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L22: To address these challenges, we introduce **AgentGym-RL**, a new framework to train LLM agents for **multi-turn** i
> L40: - **Training module**: implements reinforcement learning pipelines and other training methods to optimize agent pol
> L64: We make following modifications to verl in order to develop AgentGym-RL:

## 星数曲线

```mermaid
xychart-beta
    title "WooooDyy/AgentGym-RL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 875 --> 879
    line [876, 878, 878]
```

2026-10-18 876 → 2026-10-21 878（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `40815ce4f37c` · [字段定义](../../DATASET.md)*
