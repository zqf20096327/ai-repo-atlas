# Logos-Flux/spark-voice-pipeline

⭐ 19 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/Logos-Flux/spark-voice-pipeline) · 组织维护

**DGX Spark 上的实时语音助手管线（766ms 首音频延迟）**

部署在 DGX Spark（GB10 GPU、128GB 统一内存）上的流式语音助手管线：Whisper.cpp 做 STT，Ollama 提供 LLM 对话，VibeVoice-Realtime-0.5B（7 种预置音色）做流式 TTS，客户端通过 WebSocket 双向流式收发音频。关键机制为句级流式——LLM 生成中即按句子边界送 TTS，实测首音频约 766ms、TTS RTF 0.48x。三个服务默认绑定回环地址且无内置鉴权，README 提示远程访问需经 SSH 转发或带鉴权的反向代理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 句级流式：不等完整回复即按句边界送 TTS
- 实测首音频 ~766ms、TTS RTF 0.48x
- Whisper(STT) + Ollama(LLM) + VibeVoice(TTS) 全 WebSocket 流式架构
- VibeVoice 0.5B 提供 7 种预置音色（不支持克隆，克隆需 1.5B）

## 适用场景

- 在本地 DGX Spark 上搭建低延迟语音对话助手
- 用笔记本麦克风/扬声器远程连接 Spark 语音服务
- 参考其句级流式方案构建自己的流式 TTS 管线

## 场景标签

`语音 Agent` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L20: Real-time voice assistant on DGX Spark with 766ms latency to first audio.
> L69: # Terminal 1: Whisper STT
> L71: ./whisper-server -m models/ggml-large-v3-turbo-q8_0.bin --host 127.0.0.1 --port 8025
> L140: |`OLLAMA_URL`|`http://localhost:11434/api/chat`|Orchestrator → Ollama endpoint|

## 星数曲线

```mermaid
xychart-beta
    title "Logos-Flux/spark-voice-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `c0d9fd6a440e` · [字段定义](../../DATASET.md)*
