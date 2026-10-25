# second-state/echokit_server

⭐ 593 · Rust · GPL-3.0 · 推送 2026-02-15 · [GitHub](https://github.com/second-state/echokit_server) · [官网](https://echokit.dev/) · 组织维护

**ESP32 语音设备的本地/远程服务端：串接 ASR→LLM→TTS 对话**

EchoKit Server 是 EchoKit 设备与 AI 服务之间的中心组件，通过 WebSocket 与 ESP32 设备通信，驱动 ASR→LLM→TTS 全链路实时语音对话。各阶段均可独立配置：ASR/LLM/TTS 兼容任何 OpenAI 规范的 API 端点（本地或云端），TTS 额外支持 ElevenLabs 流式模式，开箱支持 Gemini 与 Qwen Real-Time 全链路。开发者可通过 config.toml 定制提示词、语音模型与 MCP 服务器以扩展工具能力。以 Rust 实现，需 git clone 后 cargo build 编译运行，并需配套 EchoKit 设备或自刷固件的 ESP32。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ASR/LLM/TTS 三阶段独立配置，均兼容 OpenAI 规范 API 端点
- 开箱支持 Gemini 与 Qwen Real-Time 全链路模型方案
- config.toml 定制 VAD、提示词、语音模型与 MCP 服务器（工具调用）
- 可本地部署或连接预设服务器（美国/台湾/全球节点）

## 适用场景

- 为自制的 ESP32 语音设备搭建对话服务端
- 开发者自选 ASR/LLM/TTS 模型组合部署端到端语音助手
- 通过 MCP 服务器为语音助手扩展外部工具能力

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: EchoKit Server is the central component that manages communication between the EchoKit device and AI services. It ca
> L18: Seamlessly connect **ASR → LLM → TTS** for real-time, natural conversations.
> L24: * **LLM (Language Model):** Connect to any *OpenAI-spec* endpoint — local or cloud.

## 星数曲线

```mermaid
xychart-beta
    title "second-state/echokit_server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 591 --> 594
    line [592, 593, 593]
```

2026-10-18 592 → 2026-10-25 593（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2e4dea087e96` · [字段定义](../../DATASET.md)*
