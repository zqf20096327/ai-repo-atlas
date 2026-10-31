# warrence/openclaw-hearth

⭐ 16 · TypeScript · MIT · 推送 2026-05-01 · [GitHub](https://github.com/warrence/openclaw-hearth) · 个人维护

**自托管的家庭多用户 AI 聊天应用，基于 OpenClaw**

面向家庭场景的自托管 AI 聊天应用：在 OpenClaw 之上构建家庭产品层，提供多会话、多用户账户、私聊与角色权限、提醒、长期记忆方向与 AI 图像生成、TTS 等功能；前端为 Vue 3 + Quasar 的移动优先 PWA，后端 NestJS + PostgreSQL，通过 OpenClaw 网关（多 provider）获取模型能力。支持 systemd/launchd 开机自启，可选 Docker 与 Caddy HTTPS。项目自声明为早期版本，不建议生产使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多用户家庭支持：每个成员独立账户与私聊、角色权限
- 自托管部署，数据留在自有硬件，无遥测
- 移动优先 PWA，可离线，流式回复与 TTS、图像生成
- 安装向导自动处理 Node.js、PostgreSQL、OpenClaw 与 HTTPS

## 适用场景

- 家庭成员共享一套自托管 AI 聊天系统，各有独立账户与私聊
- 希望对话与记忆数据留在自己硬件上的用户
- 自托管 AI 助手的日常使用与提醒管理

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5:  A self-hosted household AI chat app built on OpenClaw
> L29: Today, Hearth is focused on becoming a dependable household AI chat experience with:

## 星数曲线

```mermaid
xychart-beta
    title "warrence/openclaw-hearth 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f2aa24259622` · [字段定义](../../DATASET.md)*
