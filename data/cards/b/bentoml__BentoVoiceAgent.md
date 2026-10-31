# bentoml/BentoVoiceAgent

⭐ 135 · Python · 推送 2026-07-14 · [GitHub](https://github.com/bentoml/BentoVoiceAgent) · 组织维护

**基于开源模型构建电话语音 Agent 的 BentoML 示例工程**

BentoML 官方示例仓库，演示用开源模型搭建可通过电话号码访问的语音 Agent：Llama 3.1 作为 LLM、XTTS 做文本转语音、Whisper 做语音识别，经 Pipecat 语音管线组织，以 Twilio 作为电话通信通道。LLM 与 XTTS 需先用 BentoVLLM、BentoXTTSStreaming 部署为独立 API 端点，语音 Agent 服务通过环境变量读取端点地址，本地运行需安装 ffmpeg 与 Python 依赖，也可部署到 BentoCloud。限定在 Python 3.11 与 BentoML 1.3.9 环境验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Llama 3.1 + XTTS + Whisper 全开源模型组合
- 经 Twilio 电话接入，提供 /voice/start_call webhook 与 /voice/ws 实时语音 WebSocket 端点
- 基于 Pipecat 语音管线，模型以独立 API 端点形式组合
- 支持部署到 BentoCloud

## 适用场景

- 搭建可通过电话号码呼入的语音助手
- 参考开源模型组合（LLM/TTS/STT）构建语音 Agent 管线
- 学习 BentoML 部署多模型语音服务的架构

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: This repository demonstrates how to build a voice agent using open-source Large Language Models (LLMs), text-to-spee
> L9: - Llama 3.1

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/BentoVoiceAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 133 --> 136
    line [134, 135, 135]
```

2026-10-18 134 → 2026-10-31 135（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2554b96df6c3` · [字段定义](../../DATASET.md)*
