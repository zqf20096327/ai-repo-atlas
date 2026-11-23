# Benzo-Fury/cilica

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/Benzo-Fury/cilica) · [官网](https://cilica.si) · 个人维护

**本地优先的桌面笔记应用，内置 AI 助手与无机器人会议摘要**

开源桌面笔记应用：用户以 Markdown 写笔记并按类别组织，内置助手 Cilica 具有全部笔记的读写权限，可分类、总结、改写、提取行动项并回答提问，每次修改可撤销并显示 diff。会议场景下录制麦克风与系统音频，不加入会议机器人，在本地用 Whisper 转写并生成含摘要、决策与行动项的笔记。支持自定义 AI 提供方（含本地模型），笔记、音频与转写保留在本机。当前平台要求 macOS 14.4+（Apple Silicon），Windows/Linux 代码已写但未测试，需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无机器人会议转写：本地 Whisper 转写、说话人标注并生成摘要/决策/行动项
- 内置助手可读写全部笔记，改动可撤销并显示 diff
- 支持自定义 AI 提供方：Anthropic、OpenAI、OpenRouter 或本地模型（Ollama/LM Studio）
- 支持从 45 个应用导入笔记（Obsidian、Notion、Apple Notes、Granola 等）

## 适用场景

- 在本地管理 Markdown 笔记并让 AI 助手整理与总结
- 视频会议后自动生成带说话人标注的转写与会议纪要
- 从 Obsidian/Notion 等应用迁移既有笔记
- 设置每周摘要等定时任务自动整理笔记

## 场景标签

`知识库管理` `AI 助手` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L3:  Local notes app with an AI assistant and a bot-free meeting summariser
> L5: Cilica is a free, open-source desktop notes app with an AI assistant and a meeting summariser. You write in Markdown
> L18: - **Meeting transcription and summaries.** Records any call app with no bot, transcribes on-device with Whisper, la


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `5cb898b927cb` · [字段定义](../../DATASET.md)*
