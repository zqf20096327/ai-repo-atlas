# alirezas81/OpenVoice-CRM

⭐ 5 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/alirezas81/OpenVoice-CRM) · 个人维护

**开源实时语音对话与电话客服 CRM 骨架，本地麦克风接入**

基于 Pipecat 管线的多语言实时语音代理 MVP：Silero VAD 判定说话边界并支持打断、Groq Whisper 做语音识别、本地文本知识库经 Chroma 向量索引与 LangChain 检索生成有依据的回答、默认 Anthropic Claude 3.5 Sonnet（可切换 Haiku 或 Groq）、Edge TTS 合成语音。音频与转录默认不落盘。电话/Asterisk SIP 传输路径仅为架构目标，适配器尚未包含，当前仅本地麦克风/扬声器链路可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Silero VAD 检测语音边界，新语音可打断进行中的回答
- 本地知识库 + Chroma + ONNX 多语言嵌入 + LangChain 检索的 RAG 问答
- 默认 Claude 3.5 Sonnet，可配置 Haiku 或 Groq 聊天模型
- Edge TTS 提供 40+ 语言/地区语音

## 适用场景

- 搭建多语言语音客服/销售代理的原型
- 基于自有业务知识库做语音问答
- 在本地环境测试 Pipecat 音频管线

## 场景标签

`语音 Agent` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L7: An open-source foundation for real-time, multilingual voice support and sales agents. OpenVoice-CRM combines Pipecat
> L20: The microphone/speaker path, VAD, STT, local knowledge retrieval, LLM selection, and TTS are implemented in this MV
> L28: - **Claude-first LLM:** Anthropic Claude 3.5 Sonnet by default; Claude 3.5 Haiku is configurable for a lower-latenc


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `555bd159017b` · [字段定义](../../DATASET.md)*
