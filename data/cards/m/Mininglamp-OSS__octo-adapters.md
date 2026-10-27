# Mininglamp-OSS/octo-adapters

⭐ 43 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Mininglamp-OSS/octo-adapters) · 组织维护 · 中文 README

**OCTO 职场的第三方适配器集合：桥接 IM 平台、AI 通道与外部服务**

Mininglamp-OSS 维护的 OCTO 第三方集成仓库：提供独立启停的自包含适配器模块，把 Slack、Discord、飞书、Telegram 等 IM 平台与 OpenAI、Anthropic、Claude Agent SDK、OpenClaw 通道等 AI 提供方接入 OCTO，使 Lobster agent 能触达用户所在平台。本次发布含三族参考适配器：Claude Agent SDK WebSocket 网关（DH 密钥交换、AES-CBC、流式回复、会话持久化）、OpenClaw 通道插件、Python 版 Hermes Agent 通道。TypeScript 与 Python 并存，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三族参考适配器：Claude Agent SDK 网关、OpenClaw 通道、Hermes Agent 通道（TS/Python）
- 统一 OCTO 内部信封（channel id + message + agent context），Lobster agent 可切换传输
- 适配器开机从 octo-server 配置加载，无需修改核心服务
- 统一生命周期：连接/认证/路由/分发/恢复（指数退避重连、幂等消息 ID）

## 适用场景

- 把已有 Slack/Discord/飞书/Telegram 聊天栈接入 OCTO 职场
- 让 Claude Agent SDK 或 OpenClaw agent 通过 OCTO IM 协议收发消息
- 为 OCTO 编写新的第三方适配器时参考架构与生命周期约定

## 场景标签

 · 领域:协作平台/AI 集成基础设施

## 证据(README 行号)

> L21: Every adapter in this repo is a self-contained module that can be enabled or
> L23: platforms (Slack, Discord, 飞书, Telegram), AI providers (OpenAI, Anthropic,
> L53: |**Claude Agent SDK gateway**|TypeScript (Node)|WebSocket gateway connecting the Claude Agent SDK to the OCTO IM pr

## 星数曲线

```mermaid
xychart-beta
    title "Mininglamp-OSS/octo-adapters 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b36b9716683e` · [字段定义](../../DATASET.md)*
