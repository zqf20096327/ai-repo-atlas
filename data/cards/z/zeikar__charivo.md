# zeikar/charivo

⭐ 26 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/zeikar/charivo) · [官网](https://charivo.vercel.app) · 个人维护

**构建 Live2D AI 虚拟角色的模块化 TypeScript 框架**

面向开发者的 Live2D AI 角色构建框架，覆盖 LLM 对话、TTS、STT 与实时语音会话，并让模型通过工具调用驱动角色表情、动作、注视与口型。架构分为编排层、有状态 manager、浏览器端客户端与服务器端 provider 包，可在不重写整体的情况下替换组件。支持 OpenAI、Gemini、OpenClaw 作为 LLM/TTS/STT/实时语音的 provider；浏览器直连客户端仅限开发测试，生产路径经由服务器中转。以多个 @charivo/* npm 包分发，@charivo/render-live2d 捆绑 Live2D Cubism SDK，不采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM/TTS/STT/Realtime 四类模态均有独立 manager 与可替换 provider 包
- 模型可通过 setExpression/playMotion/lookAt 工具驱动角色表情动作与注视
- 支持 OpenAI Realtime 与 Gemini Live 两种实时语音，服务端中转路径不暴露密钥
- 提供 Web Speech API 浏览器原生 TTS/STT 与无服务器依赖方案

## 适用场景

- 开发带实时语音对话的 Live2D 虚拟角色应用
- 搭建桌面伴侣类 AI 角色（官方示例 LiveClaw 基于 Electron 与 OpenClaw agent）
- 在浏览器中快速体验完整 Live2D 角色后再接入自有后端

## 场景标签

 · 领域:虚拟角色/多模态 AI 应用框架

## 证据(README 行号)

> L11: Charivo is a modular TypeScript framework for voice, expression, motion, gaze,
> L14: rewriting the whole stack.

## 星数曲线

```mermaid
xychart-beta
    title "zeikar/charivo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-26 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5fe22bf85f32` · [字段定义](../../DATASET.md)*
