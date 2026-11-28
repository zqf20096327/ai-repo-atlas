# khushitheonexai-cloud/events-tracker

⭐ 18 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/khushitheonexai-cloud/events-tracker) · 个人维护

**团队活动日历平台，含 AI 化的 Telegram 事件录入与问答**

面向团队的活动日历与追踪工作台：提供周/月双视图、论坛嵌套会话、状态与筛选、负责人分配、事件沟通历史与自动保存编辑。AI 部分通过 Telegram 机器人把转发的邀请、PDF、海报解析为结构化事件草稿，需人工确认后入库，并支持自然语言查询日程；另有每日规则化提醒任务。数据存储在用户自己的 Supabase 项目中。要求 Windows 10/11 与 PowerShell 5.1+，通过 PowerShell 脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram 机器人将邀请/PDF/海报转为结构化事件，确认后才入库
- 自然语言查询团队日程并即时回答
- 周/月双视图与论坛嵌套会话管理
- 数据存于用户自有 Supabase 项目

## 适用场景

- 团队统一管理会议、讲座、论坛日程
- 转发邀请函自动生成日历条目
- 用聊天方式查询近期日程安排
- 为每个活动分配负责人并保留沟通记录

## 场景标签

`聊天机器人` `文档解析` · 领域:对话与助手

## 证据(README 行号)

> L7: Events Tracker is a unified team calendar and tracking workspace built for events, talks, and forums of every scale.
> L28: **🤖 Intelligent event intake** — Forward an invite, PDF, or poster to the Telegram bot and watch it become a struct


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `e2697a145a94` · [字段定义](../../DATASET.md)*
