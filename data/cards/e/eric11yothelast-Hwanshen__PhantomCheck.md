# eric11yothelast-Hwanshen/PhantomCheck

⭐ 28 · Kotlin · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/eric11yothelast-Hwanshen/PhantomCheck) · [官网](https://github.com/eric11yothelast-Hwanshen/PhantomCheck/releases/latest) · 个人维护 · 中文 README

**Android 反诈骗消息管理应用：拦截通知并做 AI 风险分析**

一款 Kotlin + Jetpack Compose 构建的 Android 应用，通过 NotificationListenerService 实时读取 LINE、Instagram、短信等通知内容而不触发已读回执。核心机制：AI 分析前先做零 token 的威胁情报预检（本地 72 小时缓存、fraud.tw、Google Safe Browsing、可选 PhishTank/Chainabuse），再路由到 Mistral/OpenAI/Groq/OpenRouter/Gemini/DeepSeek 等多 AI 配置做诈骗风险分析，含每日配额、离线重试队列、DecisionEngine 双阈值降误报。全部本地存储，无服务器、无账号、无遥测。要求 Android 8.0+ 与通知访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 AI 服务商诈骗分析，按用途路由模型，支持离线重试队列
- 零 token 威胁情报预检：URL/短链/加密货币地址查询 Safe Browsing 等
- AI 助手（RAG 只读聊天）、AI 日记、晨晚报与健康摘要查询
- 11 个桌面小组件、本地日历视图、AI 自动备忘与待办

## 适用场景

- 拦截并预判 LINE/Instagram/短信中的诈骗消息
- 从通知中自动生成备忘、待办与日程提醒
- 在本地管理消息笔记并跟踪长期目标与健康洞察

## 场景标签

`AI 助手` `知识库管理` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L5: An intelligent Android anti-scam message management app: intercepts notification previews without triggering read re
> L22: - 🛡️ **Multi-Provider AI Scam Analysis, Per-Purpose Routing & Offline Retry Queue**: Supports multiple AI profiles 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `838d3c3e1009` · [字段定义](../../DATASET.md)*
