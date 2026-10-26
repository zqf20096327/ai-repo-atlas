# xiaomochn/openclaw-feishu-swarm

⭐ 37 · TypeScript · 推送 2026-03-18 · [GitHub](https://github.com/xiaomochn/openclaw-feishu-swarm) · 个人维护 · 中文 README

**让飞书群内多个 AI 机器人互相对话的 OpenClaw 插件**

OpenClaw 的飞书多 Bot 协作插件，解决飞书机器人彼此看不到对方消息的限制：bot 发出的消息经中继 Registry（默认 wss://claw.devset.top，可自建）按名称匹配转发给被 @的 bot，实现多机器人在同群互相对话。Bot 通过出站 WebSocket 连接，无需暴露端口。可与官方 @openclaw/feishu 插件并存，但自身不注册云文档工具；转发仅在 @mention 或回复链时触发。安装方式为 git clone 源码复制到扩展目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中继 Registry 打通飞书群内多 bot 互相可见的消息转发
- bot_name 名称匹配解决跨应用 open_id 隔离问题，零配置
- 出站 WebSocket 连接，NAT/防火墙环境可用
- 支持自建 Registry（npm/tsx 运行，含 HTTP 降级与 WS 协议）

## 适用场景

- 在飞书群里让多个 AI 机器人角色协作对话
- 多 agent 群聊场景下按角色分工回答用户
- 不想暴露端口的公司内网环境部署多 bot

## 场景标签

`多智能体` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 让飞书群里的多个 AI 机器人互相对话 — OpenClaw 飞书多 Bot 插件
> L40: `feishu-swarm` 是**独立插件**，与官方 `@openclaw/feishu` 插件并存——它不替换官方插件，只添加 Bot Registry 多 Bot 协作功能。
> L246: - OpenClaw — AI Agent 框架

## 星数曲线

```mermaid
xychart-beta
    title "xiaomochn/openclaw-feishu-swarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `897e471b8ac8` · [字段定义](../../DATASET.md)*
