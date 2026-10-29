# arpy8/ESP32_Voice_Assistant

⭐ 49 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/arpy8/ESP32_Voice_Assistant) · [官网](https://youtu.be/_BZOLwxb_aU) · 个人维护

**ESP32 硬件 + Python 后端的端到端语音助手**

嵌入式与 AI 推理结合的对话语音助手：ESP32-WROOM-32 通过 INMP441 麦克风采集 16 kHz 音频，经 WebSocket 流式发送到本地或 VPS 上的 Python 后端；后端用 faster-whisper 做 STT（tiny 模型 CPU 推理）、Google Gemini 生成回复、Piper TTS 合成语音，8-bit PCM 流回 ESP32 经 LM386 放大播放。半双工模式，按键触发录音。面向硬件与 AI 爱好者，需自行组装电路并提供 Gemini API key，服务器支持 uv 或 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP32 实时音频采集 + WebSocket 流式传输（声称 100ms 以下延迟）
- Whisper tiny CPU 转写 + Gemini 2.5 Flash 生成 + Piper TTS 合成的流水线
- 可调 system prompt 控制 AI 人格
- watcher.py 看门狗自动重启保运行

## 适用场景

- 自制一个硬件语音对话助手
- 学习 ESP32 I2S 音频与 WebSocket 流式架构
- 在本地/VPS 上搭轻量语音 AI 后端

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L10:  This project combines embedded systems and
> L15:  Speech-to-Text (STT) via Faster-Whisper
> L16:  Language Understanding via Google Gemini
> L17:  Text-to-Speech (TTS) using Piper TTS

## 星数曲线

```mermaid
xychart-beta
    title "arpy8/ESP32_Voice_Assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 48 --> 51
    line [50, 49, 49]
```

2026-10-18 50 → 2026-10-29 49（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `baed0340c539` · [字段定义](../../DATASET.md)*
