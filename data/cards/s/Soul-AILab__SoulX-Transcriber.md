# Soul-AILab/SoulX-Transcriber

⭐ 302 · Python · Apache-2.0 · 推送 2026-06-22 · [GitHub](https://github.com/Soul-AILab/SoulX-Transcriber) · [官网](https://soul-ailab.github.io/soulx-transcriber/) · 组织维护 · 中文 README

**多说话人语音转录的端到端音频语言大模型框架**

面向多人对话场景的统一端到端大音频语言模型，在单一框架内直接联合建模说话人归属、时间戳分段与转写文本，输出含时间戳、说话人标签与文本的结构化转写结果，适用于重叠语音与快速对话轮换场景。模型基于 Qwen3-Omni-30B-A3B-Instruct 架构，经说话人感知多阶段训练；另提供基于 agent 的多说话人对话仿真数据管线（Qwen3-8B 分析、多说话人 TTS 合成、多维说话人属性检索匹配）。权重托管于 HuggingFace 与 ModelScope，推理推荐 vllm-omni，微调经 ms-swift，支持中英文，Apache 2.0 许可；训练脚本尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单框架联合建模说话人归属、时间戳分段与转写，替代级联管线
- 说话人感知多阶段训练（持续预训练+监督微调）
- 基于 agent 的多说话人对话仿真管线：参考音频多维属性检索与匹配
- 权重发布于 HuggingFace/ModelScope，推理推荐 vllm-omni

## 适用场景

- 会议等多说话人场景的带说话人标签和时间戳的转写
- 研究中对重叠语音、快速对话轮换做说话人分离与识别
- 构造多说话人合成对话数据用于训练与评估

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L41: SoulX-Transcriber is a unified end-to-end large audio language model for **multi-speaker diarization and recognitio
> L44: - **State of the art performance**. SoulX-Transcriber achieves superior performance on the AISHELL-4 and AliMeeting

## 星数曲线

```mermaid
xychart-beta
    title "Soul-AILab/SoulX-Transcriber 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 299 --> 302
    line [300, 301, 301]
```

2026-10-18 300 → 2026-10-21 301（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a09557aac1db` · [字段定义](../../DATASET.md)*
