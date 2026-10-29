# GuLu9527/flashclaw

⭐ 29 · TypeScript · MIT · 推送 2026-03-07 · [GitHub](https://github.com/GuLu9527/flashclaw) · 个人维护 · 中文 README

**给个人用户的可插拔 AI 助手：飞书/Telegram 对话接入**

基于 TypeScript 的个人 AI 助手服务，通过飞书、Telegram 等消息渠道对话，默认接入 Anthropic Claude API（可切换 openai-provider）。采用乐高式插件架构，渠道、工具、Provider 均为可插拔插件并支持运行时热加载；内置定时任务（cron/interval/once，带并发控制与自动重试）、多层级持久记忆（用户/会话/全局）、SOUL.md 人格设定、多 Agent 路由与上下文窗口保护。通过 npm 全局安装，以 CLI 守护进程方式在 Windows/Linux/macOS 运行，长连接无需公网服务器。注意：AI Agent 直接在本机运行，可访问所有文件和执行命令，README 提示仅在可信环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 乐高式插件架构，渠道/工具/Provider 可插拔并支持热加载
- 飞书、Telegram 原生长连接支持，无需公网服务器
- cron/interval/once 定时任务，含精确定时、并发控制、超时保护与指数退避重试
- 用户/会话/全局三层持久记忆，跨会话互通

## 适用场景

- 在飞书或 Telegram 私聊、群聊中随时与 AI 助手对话
- 让助手每天定时执行提醒或任务
- 通过安装插件扩展搜索、浏览器控制、语义记忆等能力
- 为不同群组或会话配置不同人格与 Agent

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: > 闪电龙虾 - 快如闪电的 AI 助手
> L108: AI_PROVIDER=anthropic-provider    # 可选：anthropic-provider（默认）、openai-provider
> L302: |飞书|✅ 完整支持|WebSocket 长连接|

## 星数曲线

```mermaid
xychart-beta
    title "GuLu9527/flashclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d44493ed3694` · [字段定义](../../DATASET.md)*
