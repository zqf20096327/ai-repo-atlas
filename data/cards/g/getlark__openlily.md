# getlark/openlily

⭐ 32 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/getlark/openlily) · 组织维护

**本地终端语音助手：唤醒词+可换 LLM+可选工具**

Alexa 式的个人语音助手，在用户本机以终端语音 CLI 运行：麦克风输入→LLM→语音输出，支持可选唤醒词（openWakeWord，本地运行）。核心机制是可切换的 brain（STT/LLM/TTS 组合），预置 OpenAI、Cartesia、OpenAI Realtime 及全本地 brain（MLX Whisper+Ollama+Kokoro，需 Apple Silicon）；工具（网页搜索、浏览器自动化、邮件、Notion 等）逐项 opt-in。限制：本地 brain 需安装 local-models 可选依赖且无网页搜索；本地语音路径需 PortAudio。另提供托管版 asklyla.ai 与可嵌入 Pipecat 的库形式。

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

- 可切换 brain：云端（OpenAI/Cartesia/Realtime）或全本地（MLX Whisper+Ollama+Kokoro）
- openWakeWord 本地唤醒词，无需云服务与 API key
- Silero VAD + Smart Turn v3 本地端点检测，WebRTC 音频模块做回声消除
- 工具 opt-in：网页搜索、Playwright 浏览器、邮件、Notion，可自写工具

## 适用场景

- 在本机或树莓派上搭一个私有语音助手，用唤醒词随时对话
- 不想被绑定单一厂商，自由选择 STT/LLM/TTS 供应商或全本地运行
- 通过对话让助手执行搜索、控制浏览器、发邮件等操作

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: openlily is an Alexa-like personal voice assistant. You talk to it
> L4: through your own mic and speakers — voice in → LLM → voice out — and it can answer
> L30: - **Swappable "brains"** — run a cascade pipeline (separate STT → LLM → TTS) or a

## 星数曲线

```mermaid
xychart-beta
    title "getlark/openlily 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0a0d69a323de` · [字段定义](../../DATASET.md)*
