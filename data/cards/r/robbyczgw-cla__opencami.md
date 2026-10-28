# robbyczgw-cla/opencami

⭐ 31 · TypeScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/robbyczgw-cla/opencami) · [官网](https://opencami.xyz) · 个人维护

**OpenClaw 的 Web 聊天客户端：浏览器对话界面与工作台**

基于 React/TypeScript/Vite 的 Web 前端，通过 WebSocket 连接本机或远程的 OpenClaw Gateway，提供流式对话、文件/图片附件、语音播放与输入、智能会话标题与追问建议。内建文件浏览器、Memory 查看器、Agent 管理器、技能浏览器与定时任务面板等工作台功能。支持 PWA 与 Tauri 桌面壳（实验性），可通过安装脚本、npm 全局安装或 Docker 运行；需先部署 OpenClaw Gateway 并完成设备配对。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 WebSocket 连接 OpenClaw Gateway，流式对话与设备配对机制
- 内建文件浏览器、Memory 查看器、Agent 管理器、ClawHub 技能浏览器
- 语音播放（ElevenLabs/OpenAI/Edge TTS）与语音输入（Scribe/Whisper/浏览器）
- PWA 安装与 Tauri 桌面壳（macOS/Windows/Linux，实验性）

## 适用场景

- 为自托管的 OpenClaw 提供浏览器聊天界面
- 通过 Tailscale 从外部设备访问本地 Gateway 的对话
- 在统一界面里管理会话、Agent、技能与定时任务

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A beautiful web client for OpenClaw.
> L31: opencami --gateway ws://127.0.0.1:18789 --token <GATEWAY_TOKEN>
> L156: - ⚡ **Real-time streaming** — persistent WebSocket + SSE, token-by-token

## 星数曲线

```mermaid
xychart-beta
    title "robbyczgw-cla/opencami 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9ad3192002c9` · [字段定义](../../DATASET.md)*
