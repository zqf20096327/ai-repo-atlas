# pmbstyle/Alice

⭐ 323 · TypeScript · MIT · 推送 2026-10-01 · [GitHub](https://github.com/pmbstyle/Alice) · 个人维护

**桌面端语音优先的 AI 助手应用，支持云端与本地模型**

基于 Vue.js/Vite/Electron（后端 Go）构建的桌面 AI 语音助手：提供 VAD 驱动的语音识别、TTS、唤醒词、截图解读、图像生成等能力。记忆系统包含 Hnswlib 向量库的短期上下文、本地 DB 长期记忆、情绪感知摘要与本地 RAG。支持 OpenAI/OpenRouter/DeepSeek/Z.ai/Minimax 等云端以及 Ollama/LM Studio 本地模型（完全本地模式为实验性）。工具层含文件系统、Shell 命令（分级授权）、MCP、自定义 JSON 工具与 Chrome 扩展。提供 Win/macOS/Linux 安装包，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 语音交互：VAD 识别、多 TTS、唤醒词、可打断输出
- 分层记忆：Hnswlib 向量短期上下文 + 本地 DB 长期记忆 + 本地 RAG
- 计算机使用工具：文件浏览、Shell 执行、分级权限管理与 MCP 支持
- 云端（OpenAI/OpenRouter/DeepSeek 等）与本地（Ollama/LM Studio，实验性）双模式

## 适用场景

- 用语音唤醒并对话，让 AI 助手处理日常任务
- 让 AI 在授权下操作本地文件与执行命令
- 接入本地模型实现完全离线的桌面助手
- 对本地文档做 RAG 问答与摘要

## 场景标签

 · 领域:桌面 AI 助手

## 证据(README 行号)

> L3: Say "Hi" to Alice 👋, your open-source AI companion designed to live on your desktop.
> L18: Alice is designed to work with Cloud(OpenAI / Codex subscription, OpenRouter, Z.ai, Minimax, Deepseek) and Local LL

## 星数曲线

```mermaid
xychart-beta
    title "pmbstyle/Alice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 322 --> 324
    line [323, 323]
```

2026-10-18 323 → 2026-10-22 323（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1755c8598e72` · [字段定义](../../DATASET.md)*
