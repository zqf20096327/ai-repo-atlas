# OlgaKalinina101/YourOwnAI

⭐ 18 · Kotlin · Apache-2.0 · 推送 2026-04-29 · [GitHub](https://github.com/OlgaKalinina101/YourOwnAI) · 个人维护

**隐私优先的 BYOK 本地 Android AI 助手客户端**

Kotlin/Jetpack Compose 编写的 Android 聊天应用：用户自带 API 密钥直连 Deepseek、OpenAI、x.ai、OpenRouter（含 Claude/Gemini/Llama 系列）等 200+ 云端模型，也支持在设备上下载运行 Qwen 2.5、Llama 3.2（GGUF）离线推理。对话、记忆、RAG、密钥（Android Keystore 加密）全部本地存储（Room 数据库），无遥测、无后端。功能含多模态附件、语音对话、记忆聚类、可选 Supabase 云同步与局域网桌面 Web 客户端。自述处于 Beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 自带 API 密钥直连多家云端提供商（Deepseek/OpenAI/x.ai/OpenRouter）
- 设备本地 GGUF 模型离线推理（Qwen 2.5 1.7B、Llama 3.2 3B）
- 本地优先存储：Room 数据库 + Keystore 加密密钥 + 零遥测
- 多模态附件（26 个视觉/文档模型）与实时语音对话

## 适用场景

- 用自己的 API key 在手机上与多家模型对话，避免订阅费
- 下载本地模型实现完全离线聊天
- 跨设备同步对话（可选 Supabase）或局域网桌面端访问

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L10: YourOwnAI is a privacy-first Android application that gives you complete control over your AI assistant. Use your o
> L39: - ✅ **Switch providers** freely - Deepseek, OpenAI, x.ai, or local models
> L235: - **Local inference** - Qwen 2.5 1.7B (950MB), Llama 3.2 3B (1.9GB)

## 星数曲线

```mermaid
xychart-beta
    title "OlgaKalinina101/YourOwnAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `47a7fcf93fee` · [字段定义](../../DATASET.md)*
