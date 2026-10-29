# DonDebonair/slack-machine

⭐ 769 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/DonDebonair/slack-machine) · [官网](https://dondebonair.github.io/slack-machine/) · 个人维护

**面向开发者的可扩展 Slack 聊天机器人框架**

基于 Python 的 Slack 机器人开发框架，通过插件系统组织机器人功能，支持正则匹配、Slash 命令、Blocks、Modals、各类 Slack 事件响应等插件 API。底层使用 Slack Events API 与 Socket Mode（无需暴露到公网）、Slack Web API，基于 AsyncIO 并发处理通信。支持 Redis、DynamoDB、SQLite 及内存等持久化存储，可调度任务和事件。面向想把 Slack 工作区开发为 ChatOps 工具的开发者，通过 uv/Poetry/pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件系统构建 Slack 机器人，正则/命令/事件等多种响应方式
- Socket Mode 运行，无需将机器人暴露到公网
- 支持 Redis/DynamoDB/SQLite/内存持久化存储
- 基于 AsyncIO 并发处理与 Slack 的通信

## 适用场景

- 为团队工作区开发 ChatOps 机器人
- 组织多个插件功能构建自定义 Slack bot
- 在私聊、频道、线程中响应消息与交互组件

## 场景标签

 · 领域:开发工具/聊天机器人

## 证据(README 行号)

> L10: Slack Machine is a simple, yet powerful and extendable Slack bot framework. More than just a bot, Slack
> L11: Machine is a framework that helps you develop your Slack workspace into a ChatOps powerhouse. Slack Machine is buil

## 星数曲线

```mermaid
xychart-beta
    title "DonDebonair/slack-machine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 768 --> 770
    line [769, 769]
```

2026-10-18 769 → 2026-10-29 769（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `19c646afe1d2` · [字段定义](../../DATASET.md)*
