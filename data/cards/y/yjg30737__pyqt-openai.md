# yjg30737/pyqt-openai

⭐ 148 · Python · MIT · 推送 2026-04-20 · [GitHub](https://github.com/yjg30737/pyqt-openai) · 个人维护

**跨平台桌面 LLM 聊天与图像生成客户端，支持多模型**

基于 PySide6 的跨平台桌面应用（前身为 pyqt-openai），在无需浏览器的情况下与 GPT、Claude、Gemini、Llama 等 LLM 对话，并支持 DALL-E 3、Replicate、GPT4Free 图像生成。聊天记录本地数据库存储，提供提示词管理、导入导出、STT/TTS（OpenAI STT、edge-tts）、界面自定义与快捷键等功能。通过 GPT4Free 与 LiteLLM 提供免费用量。安装方式含源码运行（git clone + pip）、Makefile 与安装包下载；STT 功能需先装 PortAudio。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 与 GPT/Claude/Gemini/Llama 对话及 DALL-E 3/Replicate/GPT4Free 图像生成
- 本地数据库存储聊天历史，支持导入导出与提示词管理
- STT/TTS 交互（OpenAI STT、Whisper、edge-tts）
- 基于 GPT4Free 与 LiteLLM，可基本免费使用

## 适用场景

- 在桌面端直接使用多家 LLM 聊天，不依赖浏览器
- 在会话中生成并管理图像
- 本地保存与管理聊天记录和提示词

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L3:  A cross-platform AI desktop chatbot application for LLM such as GPT, Claude, Gemini, Llama chatbot interaction and 
> L14: **VividNode** is a cross-platform desktop application that allows you to interact directly with LLM(GPT, Claude, Ge
> L19: - **Image Generation**: Generate images using OpenAI's DALL-E 3 or models from Replicate or GPT4Free, directly with

## 星数曲线

```mermaid
xychart-beta
    title "yjg30737/pyqt-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 147 --> 149
    line [148, 148]
```

2026-10-18 148 → 2026-10-24 148（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4757b3649a70` · [字段定义](../../DATASET.md)*
