# tercumantanumut/selene

⭐ 172 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/tercumantanumut/selene) · [官网](https://selene.engineer) · 个人维护

**本地优先的 AI agent 桌面应用：聊天写码生图，接入聊天平台**

基于 Electron 的 agent 桌面应用，在用户本机运行 AI：聊天、写代码、Git/PR 管理、生成图像与 UI 组件、Playwright 驱动的内嵌 Chromium 浏览器、屏幕感知（Ghost OS 视觉 sidecar）、语音输入与克隆、定时任务与记忆。可通过原生集成连接 WhatsApp/Telegram/Slack/Discord。支持 Anthropic/OpenAI/Ollama/vLLM/OpenRouter 等多种提供商，可完全离线运行；检索管线按需加载工具以压缩上下文。macOS/Windows 提供签名安装包，数据留在本地设备。

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

- WhatsApp/Telegram/Slack/Discord 原生集成，语音笔记自动转录
- Playwright 驱动的内嵌 Chromium，支持并行隔离与操作回放
- 本地与云端模型可混搭，支持完全离线运行
- 先检索后生成的管线按需加载工具以降低每轮成本

## 适用场景

- 在本机跑一个接入 WhatsApp/Telegram 等聊天平台的个人 AI 助手
- 让 agent 代为做 Git 操作、控制浏览器与写代码
- 生成图像、UI 组件并实时预览编辑

## 场景标签

`AI 助手` `Agent 记忆` `浏览器自动化` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L9: Selene is an agent-first desktop app that runs AI on your machine. Chat, write code, generate images, design UIs, co
> L104: |**Anthropic**|Claude (Opus 5.5, Sonnet 5.5, Fable 5.1, Haiku) via API or Agent SDK|
> L107: |**Ollama**|Any local model; dynamic thinking detection|

## 星数曲线

```mermaid
xychart-beta
    title "tercumantanumut/selene 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 170 --> 173
    line [171, 172, 172]
```

2026-10-18 171 → 2026-10-26 172（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `141b4e6d26ce` · [字段定义](../../DATASET.md)*
