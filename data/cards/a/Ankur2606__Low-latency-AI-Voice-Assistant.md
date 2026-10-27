# Ankur2606/Low-latency-AI-Voice-Assistant

⭐ 27 · Jupyter Notebook · MIT · 推送 2026-04-15 · [GitHub](https://github.com/Ankur2606/Low-latency-AI-Voice-Assistant) · [官网](https://low-latency-ai-voice-assistant-ui.streamlit.app/) · 个人维护

**端到端 AI 语音助手管线：Whisper 识别、LLM 生成、Edge-TTS 合成**

构建语音对话闭环的开源管线：faster-whisper(tiny) 在 16kHz 单声道输入上做语音识别并内置 VAD 静音检测，文本交由 Hugging Face LLM 生成回答（限制 60 token / 2 句），再经 edge-tts 合成语音，音高、男/女声、语速可调。提供终端实时交互（main.py）与 Streamlit 网页（app.py）两种运行方式，需自备 Hugging Face API token；README 提及通过异步推理与 WRTC 流式框架将延迟控制在 500ms 以下的优化方向。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- faster-whisper(tiny) 语音识别 + 可调阈值 VAD 静音检测
- Hugging Face LLM 生成回答并限制输出为 2 句 / 60 token
- edge-tts 合成，音高、声线（男/女）、语速可调
- 终端实时模式与 Streamlit 网页两种运行入口

## 适用场景

- 在终端或网页进行实时语音对话交互
- 学习 STT-LLM-TTS 三段式管线的搭建方式
- 在可调 TTS 参数下定制合成语音的音高与语速

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L11: This repository contains an end-to-end AI Voice Assistant pipeline. The system converts voice input to text using O
> L16: - **Speech-to-Text (STT):** Converts spoken language to text using the `faster-whisper` model.

## 星数曲线

```mermaid
xychart-beta
    title "Ankur2606/Low-latency-AI-Voice-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `334eb6f7b847` · [字段定义](../../DATASET.md)*
