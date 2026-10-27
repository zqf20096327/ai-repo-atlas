# byte271/Openlive

⭐ 37 · Rust · Apache-2.0 · 推送 2026-08-28 · [GitHub](https://github.com/byte271/Openlive) · 个人维护

**给开发者的自托管实时语音 agent 运行时，模型中立**

OpenLive 是用 Rust 实现的开源自托管实时语音 agent 运行时，将截止期敏感的交互连续性与较慢的模型认知分离，保留原生双工提供方能力。功能包括通话优先语音界面、OpenAI 兼容 Piper 神经 TTS 路径（经 LocalAI/openedai-speech）、客户端音频智能（降噪/VAD/回声消除）、agent 工具与沙箱（≤50 多 agent 池）、WebRTC 与 WebSocket 传输、Moshi 原生双工及内置 LLM 提供方目录。提供 Tauri 桌面壳（Windows MSI/macOS DMG）。当前版本 26.7.16，尚缺完整 RTP Opus 媒体面等功能。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互连续性与模型认知分离的架构，保留原生双工能力
- 客户端音频智能：RNNoise 式降噪、Silero 式 VAD、NLNS 回声消除、本地 barge-in
- 多 agent 池（≤50）+ 沙箱文件 I/O + headless 浏览，支持 MCP 工具
- 内置 LLM 提供方目录（NVIDIA NIM、Groq、OpenRouter、Ollama 等）与 Moshi 原生双工

## 适用场景

- 自托管搭建 GPT-Live 式的实时语音对话应用
- 通过 OpenAI 兼容栈（LocalAI/Piper）跑离线神经语音
- 用本地 LLM（Ollama 等）驱动多 agent 语音会话

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: OpenLive is an open, model-neutral runtime for continuous voice agents. It separates deadline-sensitive interaction 
> L28: - Production path: cascade → OpenAI-compatible **Piper** TTS (via LocalAI, openedai-speech, or gateway-local Piper)
> L55: - Built-in LLM provider catalog (NVIDIA NIM, Groq, OpenRouter, Ollama, …) in Settings.

## 星数曲线

```mermaid
xychart-beta
    title "byte271/Openlive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-27 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4b7d1fd8cc07` · [字段定义](../../DATASET.md)*
