# farhan-beg/talaria

⭐ 18 · Kotlin · MIT · 推送 2026-10-13 · [GitHub](https://github.com/farhan-beg/talaria) · 个人维护

**连接 Hermes Agent 服务器的独立 Android 客户端**

面向自托管 Hermes Agent 服务器使用者的 Android 应用，用 Kotlin/Jetpack Compose 编写。提供聊天（流式回复、推理轨迹、工具调用渲染）、Markdown 编写器、语音模式（可调用服务器端 TTS）、会话历史与网关 WebSocket 实时重连、自动化定时提示、Webhook、渠道与档案管理，以及模型、技能、密钥、MCP 服务器、内存等管理面板。通过 Releases 页下载签名 APK 安装（Android 8.0+），不在 Google Play 上架；源码构建需 JDK 17 与 Android SDK。与 Nous Research 无关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式聊天、推理轨迹与工具调用渲染
- 语音模式：听写输入，回复可用手机语音或服务器 TTS 朗读
- 会话历史、中途恢复与 Hermes 网关 WebSocket 实时重连
- 模型/技能/密钥/MCP 服务器/内存等管理面板

## 适用场景

- 在手机上连接并使用我自托管的 Hermes Agent 服务器
- 通过语音与 agent 对话并让回复朗读出来
- 在移动端管理服务器的模型、技能与 MCP 配置

## 场景标签

`聊天机器人` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: An independent Android client for Hermes Agent servers.
> L29: - Session history with filters, mid-turn resume, and live reconnect over the Hermes gateway WebSocket

## 星数曲线

```mermaid
xychart-beta
    title "farhan-beg/talaria 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d898d40ffefc` · [字段定义](../../DATASET.md)*
