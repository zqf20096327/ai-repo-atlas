# HarryHsing/OmniAgent

⭐ 80 · Python · Apache-2.0 · 推送 2026-09-18 · [GitHub](https://github.com/HarryHsing/OmniAgent) · [官网](https://huggingface.co/spaces/harryhsing/OmniAgent-Slides) · 组织维护 · 中文 README

**全模态主动感知视频理解 agent（7B），感知即推理迭代取帧/音频**

基于 Qwen2.5-Omni-7B 的原生全模态 agent，将视频感知形式化为 POMDP 的 Observation–Thought–Action 循环：模型按需调用 get_frames/get_audio/get_clip/answer 结构化动作，感知摘要后清除原始媒体以解耦上下文开销与视频时长。两阶段训练（Agentic SFT 冷启动 + TAURA 强化学习），在十个基准上评测视频理解、音视频理解与时序定位。提供 RL/SFT 权重、gym 式训练环境与推理/评测/Web demo 入口。推理需 1×A100 80GB，训练需 64×A100 80GB+，依赖 CUDA 12.6 与 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OTA 循环按需取帧/音频/片段，替代整段视频前置消费
- 记忆固化：感知摘要为文本后清除原始媒体，上下文随信息需求而非视频时长增长
- 两阶段训练：Agentic SFT（58K 合成轨迹）+ TAURA 强化学习
- 提供 gym 式 agent 环境与单样本推理、Web demo、批量评测脚本

## 适用场景

- 长视频问答与音视频联合理解的推理评测
- 时序定位（temporal grounding）任务
- 训练自己的全模态主动感知模型或复现 SFT/RL 训练流程
- 在统一 OTA 框架内驱动闭源模型做主动视频感知

## 场景标签

`多模态` `强化学习` · 领域:感知与多模态

## 证据(README 行号)

> L13: > **OmniAgent** is, to our knowledge, the first native omni-modal agent for active perception in video understandin
> L31: OmniAgent instead formulates audio-visual exploration as a **POMDP-based iterative Observation–Thought–Action (OTA)
> L46: OmniAgent reframes video perception as reasoning: a single omni model iteratively observes, thinks, and acts on the

## 星数曲线

```mermaid
xychart-beta
    title "HarryHsing/OmniAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-24 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6f49c9b97084` · [字段定义](../../DATASET.md)*
