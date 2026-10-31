# Pedal-Intelligence/saypi-userscript

⭐ 24 · TypeScript · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/Pedal-Intelligence/saypi-userscript) · [官网](https://www.saypi.ai/) · 组织维护

**为 Pi/Claude/ChatGPT 添加多语言语音交互的浏览器扩展**

Say, Pi 是一款面向最终用户的浏览器扩展，为 Pi.ai、Claude.ai 与 ChatGPT 网页端注入语音能力：Silero VAD（ONNX）做实时语音活动检测与智能分段，OpenAI Whisper 做多语言实时转录，配合 TTS 实现语音对话；通过可插拔的 chatbot 抽象层与渐进式 DOM 观察适配各平台。跨 Chrome/Edge/Firefox/Safari，功能覆盖因平台 CSP 与 API 差异而不同。用户从扩展商店安装；开发者需 Node 22+、Python 3.11 与 jq 构建源码。源码公开可见但为专有软件，不允许修改与分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Silero VAD（ONNX Runtime Web/WASM）实时语音检测与智能分段
- OpenAI Whisper 集成的多语言语音识别，实时反馈
- 可插拔 chatbot 抽象层，支持 Pi.ai/Claude.ai/ChatGPT
- TypeScript + XState 状态机 + 事件驱动架构，双测试框架（Jest/Vitest）

## 适用场景

- 在 Pi.ai/Claude.ai/ChatGPT 网页端用语音输入与 AI 对话
- 多语言语音输入并自动检测语言
- 在移动端 Firefox 等环境做语音输入（部分平台）

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: Say, Pi is a browser extension that brings multilingual voice capabilities to AI chatbots. Built with enterprise-gra
> L43: - **OpenAI Whisper integration** for high-quality transcription

## 星数曲线

```mermaid
xychart-beta
    title "Pedal-Intelligence/saypi-userscript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f884bb47dc1f` · [字段定义](../../DATASET.md)*
