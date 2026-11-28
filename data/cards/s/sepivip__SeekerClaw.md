# sepivip/SeekerClaw

⭐ 324 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/sepivip/SeekerClaw) · [官网](https://seekerclaw.xyz) · 个人维护

**把 Android 手机（含 Solana Seeker）变成 24/7 个人 AI 代理的应用**

在 Android 应用内嵌 Node.js AI 代理（前台服务常驻运行），用户经 Telegram 或 Discord 与其交互：提问、控制手机、定时任务，以及在 Solana 链上用 USDC 交易与向 x402 付费 API 自主支付。内置 64 个工具、22 个技能，支持 MCP 远程工具与自定义技能（Markdown+YAML 格式）。AI 引擎为多供应商配置（Claude/OpenAI/xAI Grok/OpenRouter 或任意 OpenAI 兼容网关）。需自备 API key 或登录凭据；项目处于 Beta，从源码用 Android Studio 构建，也提供 APK 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 内嵌 Node.js 运行时的前台服务代理，经 Telegram/Discord 交互
-  burner 钱包限额自主交易与 x402 付费 API 支付，主钱包始终由用户签名
- 64 内置工具 + 22 技能 + MCP 远程工具，可在聊天中切换模型/供应商
- 持久记忆、自然语言 cron 定时、多搜索后端网页情报

## 适用场景

- 把闲置 Android 手机变成长驻个人代理随时对话
- 在 Telegram 里让代理执行手机操作与定时提醒
- 在设定限额内让代理自主进行 Solana 代币交易
- 让代理按需调用付费 API（行情、旅行、研究等）

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L28: SeekerClaw — winner of the **Solana Mobile Hackathon (April 2026)** — embeds a Node.js AI agent inside an Android a
> L34: **64 built-in tools** (plus MCP remote tools), **22 bundled skills + 5 partner skills**, two-wallet Solana with **c

## 星数曲线

```mermaid
xychart-beta
    title "sepivip/SeekerClaw 星数(近 7 点)"
    x-axis ["2026-10-26", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-22", "2026-11-25", "2026-11-28"]
    y-axis "stars" 318 --> 325
    line [319, 320, 321, 322, 323, 324, 324]
```

2026-10-26 319 → 2026-11-28 324（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `03cb1c91f103` · [字段定义](../../DATASET.md)*
