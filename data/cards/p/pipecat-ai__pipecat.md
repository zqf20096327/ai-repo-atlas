# pipecat-ai/pipecat

⭐ 16,572 · Python · BSD-2-Clause · 推送 2026-10-18 · [GitHub](https://github.com/pipecat-ai/pipecat) · [官网](https://pipecat.ai) · 组织维护

**给开发者构建实时语音与多模态 AI 代理的 Python 框架**

Pipecat 是一个用于构建实时语音与多模态对话代理的开源 Python 框架，由 Daily 与社区维护。它编排音频/视频、AI 服务、传输层与对话管道，支持单代理或多代理系统（交接、并行分发、共享总线，可跨进程与机器分布式运行）。传输层支持 WebSockets 与 WebRTC。核心框架默认轻量，第三方 AI 服务依赖通过 extras 按需添加。需要 Python 3.11+，用 uv 安装；提供 CLI 脚手架、客户端 SDK（JS/React/Swift/Kotlin/C++/ESP32）、调试工具与 Pipecat Cloud 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 33,339 位贡献者
- 涨星:近 1 天 **+30**(自 20261016 起算)
- 安装:pypi 包 `pipecat-ai` 月下载 1,043,553
- 平台:ANDROID / IOS · 协议:OLLAMA

## 能力要点

- 语音优先管道：集成语音识别、TTS 与对话处理，支持多模态（语音/视频/图像）
- 多代理系统：每个管道即一个代理，支持 handoff、并行 fan-out、sidecar 与分布式部署
- 大量可插拔服务：LLM、STT、TTS、传输、视频、VAD 等数十家服务商
- 官方多平台客户端 SDK：JavaScript/React/React Native/Swift/Kotlin/C++/ESP32

## 适用场景

- 构建语音助手或 AI 陪伴类实时对话应用
- 搭建多代理协作系统（交接、并行、共享总线）
- 开发客服/客户接待等业务型语音代理
- 为语音 AI 应用接入 WebRTC/WebSocket 传输与电话序列化器

## 场景标签

`Agent 框架` `语音 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Pipecat** is an open-source Python framework for building real-time voice and multimodal conversational agents. Bu
> L26: - **Multi-Agent Ready**: Each pipeline is an agent. Compose them with handoff, parallel fan-out, sidecar workers, o
> L87: |LLMs|Anthropic, AWS, Azure, Baseten, Cerebras, Crusoe, DeepSeek, Fireworks AI, Gemini, Grok, Groq, Inception, Mist

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `2d5484ab78be` · [字段定义](../../DATASET.md)*
