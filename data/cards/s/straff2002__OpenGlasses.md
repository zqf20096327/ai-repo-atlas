# straff2002/OpenGlasses

⭐ 142 · Swift · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/straff2002/OpenGlasses) · [官网](https://testflight.apple.com/join/1dcAytte) · 组织维护 · 中文 README

**给 iPhone/眼镜等苹果设备用户的私有多模型语音 AI 助手**

Avenkin 是面向个人的隐私型 AI 助手 iOS 应用，覆盖 iPhone、AirPods、Apple Watch 与 Ray-Ban/Oakley Meta 智能眼镜，提供视觉问答、语音翻译、记忆召回、日历/家居等操作执行，并有面向技术员的 Field Assist 与 My Manuals 团队功能（独立访问层级）。AI、语音识别与发音可分别选择并可按请求路由；支持经 Apple MLX 或 llama.cpp 在本机运行 GGUF 模型，配合 SenseVoice 语音识别与 Kokoro 语音实现离线对话。处于 beta，经 TestFlight 分发或从源码构建，源码采用 BSL 1.1 许可，商业使用需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 Claude/Gemini/ChatGPT/Grok 等 500+ 模型经 OpenRouter 接入
- Apple MLX/llama.cpp 本地运行 GGUF 模型，配合 SenseVoice+Kokoro 离线语音对话
- Reading Assistant 与 Blind Assistant 无障碍预设，VoiceOver/Siri/Action Button 支持
- 可接入 Home Assistant、Siri Shortcuts、MCP 工具服务器与 OpenClaw

## 适用场景

- 戴智能眼镜时免手持地问答与语音翻译
- 飞机或无信号环境下在 iPhone 上离线语音对话
- 技术员现场按引导步骤操作并查询设备手册
- 通过语音控制日历、提醒与智能家居

## 场景标签

`AI 助手` `语音 Agent` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L5: Avenkin is a private AI assistant that works for you, not for a platform: your choice of AI, your memory on your dev
> L67: Take your assistant beyond Wi-Fi and mobile coverage. Run compatible local models with **Apple MLX** or **llama.cpp
> L91: Avenkin is in beta. The quickest way in is TestFlight, Apple's app for pre-release builds; building from source is 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `79546a26331a` · [字段定义](../../DATASET.md)*
