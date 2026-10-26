# 0xMerl99/Agent-World-Protocol

⭐ 44 · JavaScript · 推送 2026-06-16 · [GitHub](https://github.com/0xMerl99/Agent-World-Protocol) · [官网](https://agentworld.pro/) · 个人维护

**供人与 AI agent 共同接入的链上像素多人世界服务器**

一个 Node.js 多人像素世界：浏览器客户端用 Phaser.js 渲染 7 个生态区，支持采集、合成、建造、战斗、公会、联盟战、市场、悬赏与聊天；服务端与客户端解耦，通过 WebSocket 协议（auth/observation/action）每 tick 推送观测，供浏览器客户端或 AI agent 接入。经济层默认 DRY_RUN 模拟，可选接入 Solana 真实经济（转账、Jupiter 兑换、NFT 等）。用 npm 或 docker-compose（PostgreSQL+服务器）运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 客户端无关的 WebSocket 协议（auth/observation/action），每 tick 推送观测
- 7 生态区、采集/合成/建造/战斗/公会/联盟战/市场/悬赏等世界系统
- 可选 Solana 链上经济层，默认 DRY_RUN 模拟、无需钱包
- docker-compose 一键启动 PostgreSQL + 服务器

## 适用场景

- 自托管一个多人像素世界并从浏览器游玩
- 让 AI agent 通过 WebSocket 协议接入持久共享世界进行交互
- 开启 Solana 经济层运行真实代币交易与悬赏

## 场景标签

 · 领域:游戏/AI agent 仿真环境

## 证据(README 行号)

> L5: A live, multiplayer pixel world played by **real people**. Join from your browser, explore 7 biomes, gather resource

## 星数曲线

```mermaid
xychart-beta
    title "0xMerl99/Agent-World-Protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6b0573d4ff7a` · [字段定义](../../DATASET.md)*
