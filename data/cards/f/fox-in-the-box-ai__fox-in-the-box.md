# fox-in-the-box-ai/fox-in-the-box

⭐ 88 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/fox-in-the-box-ai/fox-in-the-box) · [官网](https://foxinthebox.io) · 组织维护

**自托管的私有 AI 助手桌面应用：聊天+记忆+远程访问一键安装**

面向个人用户的本地 AI 助手平台：打包 Hermes Agent 与 Hermes WebUI，通过 Docker 容器在本机运行，Electron 桌面端负责安装、引导与自动更新。功能包括流式聊天（26 个斜杠命令、中途转向、会话分支）、基于 mem0+Qdrant 的跨会话语义记忆（嵌入由本地 llama.cpp 模型计算）、多配置文件、技能与 MCP 集成、定时任务、文件/终端/浏览等内置工具。接入 OpenRouter 或其他 API 提供商，可选自动检测本地 Ollama；远程访问通过 Tailscale 实现。安装提供 Windows/macOS 安装包、脚本与 Docker 命令；运行要求 Docker 与至少一个 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mem0+Qdrant 语义记忆，嵌入全部在本地 llama.cpp 计算，无需额外 API key
- 首次启动自动检测已安装的 Ollama，一键切换本地模型
- 26 个斜杠命令，支持流式中途转向、会话分支与后台任务
- Tailscale 一键开关的 HTTPS 远程访问，免端口转发

## 适用场景

- 在自己电脑上运行一个不把对话和记忆上传云端的 AI 助手
- 通过手机或其他设备经 Tailscale 私有链路远程访问本机助手
- 用 OpenRouter 一个 key 访问多家模型，或在本地 Ollama 模型间切换

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13: Fox in the Box bundles a full AI assistant — agent, chat UI, persistent memory, and secure remote access — into one
> L33: - **Remembers across sessions.** Your assistant picks up where you left off. Memory is on by default for fresh inst
> L66: - Persistent memory across sessions, stored locally in **Qdrant** (vector DB) + **mem0** — **on by default** for fr

## 星数曲线

```mermaid
xychart-beta
    title "fox-in-the-box-ai/fox-in-the-box 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 86 --> 89
    line [87, 88, 88]
```

2026-10-18 87 → 2026-10-30 88（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f06c650c5e7e` · [字段定义](../../DATASET.md)*
