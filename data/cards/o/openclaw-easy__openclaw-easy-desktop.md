# openclaw-easy/openclaw-easy-desktop

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/openclaw-easy/openclaw-easy-desktop) · [官网](https://openclaw-easy.com) · 组织维护 · 中文 README

**面向普通用户的 AI 助手桌面应用，免终端接入消息平台**

将开源 AI agent 平台 OpenClaw 封装为 Electron 桌面应用：用户安装后选择模型（默认经 Ollama 本地运行 llama3.2:3b，或填入 Google/OpenAI/Venice AI/OpenRouter 的 API key），扫码或粘贴 bot token 即可让 WhatsApp、Telegram、Discord、Slack、WeChat、飞书、LINE 等渠道获得 AI 助手。OpenClaw 核心随应用打包，无需单独安装。本仓库为可读源码构建版：无账号、无遥测，商业托管层被移除；安装器由私有仓库发布。提供 macOS/Windows 安装包，也可用 Node 22+/pnpm 12 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenClaw 核心内置打包，无需终端、配置文件与单独安装
- 默认本地模型路径：自动安装 Ollama 并从仪表盘管理模型
- 支持 7 种消息渠道接入（WhatsApp/WeChat 扫码配对）
- 多 agent、技能插件（ClawHub）、定时任务与本地 Whisper 语音输入

## 适用场景

- 不写代码就把 AI 助手接入自己的 WhatsApp 或 Telegram
- 用本地 Ollama 模型离线运行助手，对话不出本机
- 用已有 API key 让多家模型服务商驱动消息渠道助手

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L29: **OpenClaw Easy** is that same engine wrapped in a desktop app. You install it like any other
> L31: — scan a QR code, and your messaging apps have an AI assistant. The OpenClaw core ships inside the
> L42: 3. **Pick your AI** under *AI Configuration* — either a **local model** (the default; the app

## 星数曲线

```mermaid
xychart-beta
    title "openclaw-easy/openclaw-easy-desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d2025ab8966c` · [字段定义](../../DATASET.md)*
