# huggingface/speech-to-speech

⭐ 13,499 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/huggingface/speech-to-speech) · 组织维护

**用开源模型在本机搭建低延迟语音对话 agent 的框架**

以可插拔级联管道（Silero VAD → Parakeet TDT → Qwen3.5-4B → Qwen3-TTS）在本地运行语音对话，无 API key、无云端依赖；服务端实现 OpenAI Realtime 协议（WebSocket/WebRTC），为 OpenAI Realtime API 构建的应用可指向本机服务器。各阶段提供多种可替换后端，经 CLI 标志选择，支持工具调用、流式说话人分离与可视化口型输出；并作为 Reachy Mini 机器人的对话后端运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.4 天,年发版 5,65 位贡献者
- 涨星:近 1 天 **+12**(自 20261016 起算)
- 安装:pypi 包 `speech-to-speech` 月下载 2,270
- 平台:WINDOWS / MACOS / LINUX · 协议:OPENAI-API

## 能力要点

- 四级级联管道（VAD/STT/LLM/TTS），每级均有多个可互换后端
- 服务端实现 OpenAI Realtime 协议，兼容 OpenAI Realtime 客户端与 Agents SDK、LiveKit Agents
- 默认本地模型，首次下载后可完全离线运行
- 提供工具调用扩展与可选 viseme/说话人分离组件

## 适用场景

- 在自有硬件上搭建本地语音助手
- 把 OpenAI Realtime 客户端切换到自托管服务器
- 为机器人等设备提供对话后端
- 按平台选择本地 STT/LLM/TTS 组合做语音应用原型

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L11: A low-latency voice agent built from open models that **runs entirely on your computer**. One command starts a conv
> L13: The default pipeline is **Silero VAD → Parakeet TDT → Qwen3.5-4B → Qwen3-TTS**, and every stage is swappable. The s
> L76: Every stage has multiple interchangeable backends, selected via CLI flags. The code is designed for easy modificati

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `257fc72c751d` · [字段定义](../../DATASET.md)*
