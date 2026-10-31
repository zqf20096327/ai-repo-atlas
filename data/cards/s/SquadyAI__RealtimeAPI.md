# SquadyAI/RealtimeAPI

⭐ 13 · Rust · NOASSERTION · 推送 2026-03-30 · [GitHub](https://github.com/SquadyAI/RealtimeAPI) · 组织维护 · 中文 README

**自托管实时语音 AI 平台：可组合 ASR/LLM/TTS 管线**

Rust 实现的开源实时语音 AI 平台，WebSocket 传输 Opus 音频，支持全对话、纯 ASR、纯 LLM、纯 TTS 与实时翻译五种管线模式。LLM 接入任意 OpenAI 兼容 API（OpenAI/DeepSeek/Qwen/Ollama/vLLM），TTS 支持 Edge/MiniMax/Azure/火山/百度，ASR 默认 WhisperLive，内置 VAD（Silero+SmartTurn）、MCP 工具协议与 function-calling agents。提供一键安装脚本、Docker 镜像与内置 Playground，自称 OpenAI Realtime API 的自托管替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ASR→LLM→TTS 全对话管线，端到端延迟 ≤450ms、单节点 100+ 并发会话
- LLM 支持任意 OpenAI 兼容端点（DeepSeek/Qwen/Ollama/vLLM 等）
- 五种管线模式：全对话/纯ASR/纯LLM/纯TTS/实时翻译
- 内置 MCP 工具协议、function-calling agents、Prometheus 指标与 Langfuse 集成

## 适用场景

- 搭建自托管的实时语音助手或客服机器人
- 构建跨 25+ 语言的实时翻译服务
- 通过语音 function-calling 控制 IoT 设备
- 以更低成本替代按分钟计费的云端 Realtime API

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3:  Open-source real-time voice AI platform with modular ASR, LLM, and TTS pipelines.
> L139: |**LLM**|Any OpenAI-compatible|Default|GPT, DeepSeek, Qwen, Ollama, vLLM, etc.|

## 星数曲线

```mermaid
xychart-beta
    title "SquadyAI/RealtimeAPI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ed0de6234a77` · [字段定义](../../DATASET.md)*
