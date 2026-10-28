# nerufuyo/nerubot

⭐ 36 · Rust · 推送 2026-05-24 · [GitHub](https://github.com/nerufuyo/nerubot) · [官网](https://neruwork.com/playground/nerubot) · 个人维护

**Rust 编写的多功能 Discord 机器人，含 AI 聊天等命令**

基于 Rust（2024 Edition）与 Serenity 框架构建的 Discord 机器人，命令覆盖 AI 聊天、整蛊吐槽、踢/封/禁言等管理、趣味命令、统计分析、印尼节日与斋月提醒、计算器与投票等。AI 聊天通过 DeepSeek API 提供，按用户保存会话历史（DEEPSEEK_API_KEY 可选，缺失时该功能不可用）。数据存储使用与 Neruwork 共享的 PostgreSQL 与 Redis，启动时自动执行数据库迁移。提供 git clone 源码运行与 Docker Compose 两种部署方式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 DeepSeek API 的 AI 聊天（/chat、/chat-reset），按用户保存历史
- 踢/封/禁言/警告/清屏等服务器管理命令
- 服务器与用户统计分析（消息统计、命令使用）
- Docker Compose 一键部署，迁移启动自动执行

## 适用场景

- 在 Discord 服务器中部署聊天与管理一体的机器人
- 通过 /chat 命令与 AI 对话并保留个人历史
- 跟踪服务器消息与命令使用统计

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L9: |**AI Chat**|`/chat`, `/chat-reset`|Chat with DeepSeek AI, per-user history|
> L24: - **AI:** DeepSeek API

## 星数曲线

```mermaid
xychart-beta
    title "nerufuyo/nerubot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ccb010bcdae` · [字段定义](../../DATASET.md)*
