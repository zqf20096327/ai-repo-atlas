# smtmRadu/DeepUnity

⭐ 17 · C# · MIT · 推送 2026-09-13 · [GitHub](https://github.com/smtmRadu/DeepUnity) · 个人维护

**Unity 深度学习框架：张量计算、RL 训练与 LLM/TTS GPU 推理**

面向 Unity 开发者的深度学习附加框架（Unity 2022.3.43f1 LTS）：提供带 GPU 加速的张量计算与神经网络模块，以及类似 ML-Agents 流程的强化学习训练工具（DDPG/PPO/SAC/TD3，Bake 生成 Behaviour/Config 资产，支持并行训练与构建版训练）。另含 LLM 全 GPU 推理（HLSL compute shader、KV 缓存、QLoRA SFT 脚本，支持 Qwen/Gemma/MiniCPM 系列）、GPU TTS/STT（pocket-tts、Kokoro 等）与 NPCChatBase 组件，可搭建带语音的游戏 NPC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 张量计算与神经网络（GPU 加速）+ PPO/SAC/TD3/DDPG 强化学习训练
- LLM 全 GPU 推理（HLSL compute shader、KV 缓存、FP16/INT8/INT4 量化）与 QLoRA SFT 脚本
- GPU 流式 TTS（多个引擎、声音克隆）与 Qwen3-ASR/Parakeet 语音识别
- NPCChatBase 组件：Persona、预取加载权重、对话记忆等游戏 NPC 功能

## 适用场景

- 在 Unity 环境中训练智能体的强化学习策略
- 为游戏 NPC 接入本地 LLM 对话与 TTS 语音
- 在 Unity 内直接做张量计算与神经网络前向/训练

## 场景标签

`强化学习` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: DeepUnity is an add-on framework that provides tensor computation [with GPU acceleration support] and deep neural ne
> L16: DeepUnity provides full-GPU inference (HLSL compute shaders, streaming weight upload, KV caching) for the following
> L73: ## Reinforcement Learning

## 星数曲线

```mermaid
xychart-beta
    title "smtmRadu/DeepUnity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3e6c5ef8e7d5` · [字段定义](../../DATASET.md)*
