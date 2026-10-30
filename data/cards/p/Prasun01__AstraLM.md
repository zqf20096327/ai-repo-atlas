# Prasun01/AstraLM

⭐ 16 · C++ · MIT · 推送 2026-08-29 · [GitHub](https://github.com/Prasun01/AstraLM) · [官网](https://astralm.vercel.app/) · 个人维护

**Android 端本地优先的 AI 聊天客户端，可选接入云端模型**

基于 Flutter 与原生 C++ 推理引擎的 Android AI 助手：本地模式下通过 llama.cpp 在设备 CPU/GPU 上运行量化 GGUF 模型（支持 Google LiteRT-LM 加速），完全离线推理；也可自带 API 密钥切换到 OpenAI、Anthropic Claude、Google Gemini、DeepSeek、Groq、OpenRouter 等云端模型，并通过 Stability AI 与 DALL-E 3 生成图像。密钥本地加密存储，云端请求直连提供商，无代理服务器与遥测。以 GitHub Releases 签名 APK 分发，也可用 Flutter SDK 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- llama.cpp 本地运行量化 GGUF 模型，离线推理无需联网
- BYOK 云端模式支持 OpenAI/Claude/Gemini/DeepSeek/Groq/OpenRouter
- Stability AI（SD3.5）与 DALL-E 3 图像生成
- API 密钥本地加密沙盒存储，无第三方遥测

## 适用场景

- 在手机上离线运行小参数量 LLM 进行私密对话
- 用一个应用切换多家云端模型并自带 API 密钥
- 在移动端生成图像与进行代码/文档工作区编辑

## 场景标签

`AI 助手` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L10: **AstraLM** is an open-source, high-performance AI assistant for Android. Built with Flutter and native C++ inferen
> L15:  - Runs quantized GGUF models directly on device CPU/GPU via `llama.cpp`.
> L19:  - Seamlessly switch to frontier models (OpenAI, Anthropic Claude, Google Gemini, DeepSeek, Groq, OpenRouter).

## 星数曲线

```mermaid
xychart-beta
    title "Prasun01/AstraLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f0818a4a934e` · [字段定义](../../DATASET.md)*
