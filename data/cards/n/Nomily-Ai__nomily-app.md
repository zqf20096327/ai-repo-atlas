# Nomily-Ai/nomily-app

⭐ 1,018 · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/Nomily-Ai/nomily-app) · [官网](https://geekis.com) · 组织维护 · 中文 README

**BYOK 录音转写与 AI 摘要的 iOS/Android 原生客户端**

面向录音设备用户（Vobot V05E、Plaud Note Pro、钉钉 A1、TicNote、soundcore Work、Apple Watch、iPhone 导入）的移动端应用：管理本地录音库，通过用户自选的 ASR（Azure Speech 或本地 faster-whisper 兼容端点）转写并做说话人分离，再用自选 LLM 生成摘要、标题与翻译。本仓库为项目入口与文档，可运行客户端在 nomily-ios 与 nomily-android 仓库；不含自托管同步栈，应用按源码可得许可发布，商店版收费情况未说明订阅费由本项目收取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Azure Speech 转写支持最多 10 说话人分离，可选本地 faster-whisper 兼容 ASR 端点（WebSocket 12300 / HTTP 12301）
- LLM 供应商可选 OpenAI / Anthropic / Gemini / OpenRouter / Ollama / 自定义 OpenAI 兼容端点
- iOS/Apple Watch 与 Android 各自原生实现（SwiftUI / Kotlin Jetpack Compose）
- 附本地 ASR 参考服务与 Ollama 局域网部署指引

## 适用场景

- 把 BLE 录音笔或 Apple Watch 的录音转成文字和摘要
- 自带 API key，不依赖托管转写账号
- 在局域网内用本地 Whisper 与 Ollama 完成转写和摘要

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L73: - Transcribes live or recorded audio through Azure Speech or a user-operated
> L76: - Generates summaries, titles, and translations with a configured LLM provider:
> L77:  OpenAI, Anthropic, Gemini, OpenRouter, Ollama, or a custom OpenAI-compatible


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `bf0011169533` · [字段定义](../../DATASET.md)*
