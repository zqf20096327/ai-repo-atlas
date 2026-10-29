# Natfii/ZeroAI

⭐ 50 · Rust · NOASSERTION · 推送 2026-06-11 · [GitHub](https://github.com/Natfii/ZeroAI) · 个人维护

**Android 本地优先 AI agent 应用，Kotlin+Rust 原生栈**

面向 Android 的个人 AI agent 应用：Kotlin Compose UI + Rust 核心（源自上游 ZeroClaw 的裁改版）经 UniFFI 桥接，以前台守护服务实现常驻运行。支持云端 API（OpenAI/Anthropic/Gemini/OpenRouter）与本地运行时（Ollama/llama.cpp/LM Studio）及端侧 Gemma/LiteRT-LM 推理；内置 web 搜索、视觉、Rhai 沙箱脚本等工具，可接入 Telegram/Discord 渠道，含 SSH 终端（libghostty-vt）与 AI 自主玩 Game Boy 的 ClawBoy。需自行用 Gradle 构建，面向 Pixel 硬件开发，项目自述为实验性且不接受协作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Rust agent 核心 + UniFFI 桥 + Jetpack Compose 的原生 Android 栈
- 常驻前台服务模型，支持 Telegram/Discord/Google Messages 渠道
- 端侧 Gemma（LiteRT-LM）与本地/云端多后端可选
- SSH 客户端（GPU 加速 VT 终端）与 ClawBoy AI 自玩 Game Boy 模拟器

## 适用场景

- 在 Android 手机上常驻运行个人 AI agent 并接入 Telegram/Discord
- 用手机 SSH 连接远程服务器操作
- 让 AI 通过沙箱脚本与内置工具自主执行任务

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L18: **Zero** is an Android AI agent app built with Kotlin, Rust, and UniFFI. It runs a
> L62: - **On-device** — Gemma 4 E2B-it / E4B-it via LiteRT-LM (Beta)
> L45: Zero is built for people who want an agent that feels personal, local-first, and always available on Android. The g

## 星数曲线

```mermaid
xychart-beta
    title "Natfii/ZeroAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `00f0527b5e3a` · [字段定义](../../DATASET.md)*
