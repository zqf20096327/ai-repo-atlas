# Finn-Hecker/RyokanApp

⭐ 16 · Svelte · GPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/Finn-Hecker/RyokanApp) · [官网](https://ryokanapp.com) · 个人维护

**互动 AI 故事创作应用：本地/云端模型，支持浏览器多人共写**

面向互动故事创作者的 Windows/Android 原生应用（Tauri v2 + Rust + Svelte 5）。用户接入本地模型服务器（LM Studio、llama.cpp、KoboldCPP、Ollama）或云端 API（OpenRouter 等），选择角色或场景后通过对话推进故事。支持 V3 角色卡、Lorebooks 上下文注入、滚动摘要与自动上下文管理。多人模式下房主持有模型连接，好友经邀请链接通过浏览器加入，会话流量经中继以端到端加密同步，数据本地存于 SQLite。发行版页提供预构建包，也可用 Node.js v18+ 与 Rust 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单人或多人在同一同步故事中与 AI 共同创作，浏览器访客免安装免账号
- 接入 LM Studio/llama.cpp/KoboldCPP/Ollama 本地服务器或 OpenRouter 等云端 API
- V3 角色卡导入导出、Lorebooks 关键词注入、聊天克隆分支、多版本回复切换
- 端到端加密的多人会话中继，数据本地 SQLite 存储

## 适用场景

- 用本地或云端模型进行角色扮演式互动叙事
- 与朋友通过浏览器邀请链接共同创作一个故事
- 导入角色卡与世界书，管理分支对话与聊天库

## 场景标签

`AI 写作` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L6: Connect an AI model, choose a character or scenario, and shape a story through your ideas and decisions. Invent your
> L80: * **Local Models:** Connect to LM Studio, llama.cpp, KoboldCPP, Ollama, or other compatible servers.
> L81: * **Cloud APIs:** Use OpenRouter or other compatible providers.

## 星数曲线

```mermaid
xychart-beta
    title "Finn-Hecker/RyokanApp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a9725d2a9969` · [字段定义](../../DATASET.md)*
