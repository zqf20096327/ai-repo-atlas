# avikalpg/whatsapp-ai-filter

⭐ 18 · TypeScript · GPL-3.0 · 推送 2026-04-15 · [GitHub](https://github.com/avikalpg/whatsapp-ai-filter) · [官网](https://whatsapp-ai-filter.vercel.app) · 个人维护

**本地运行的 WhatsApp 群消息 AI 过滤通知机器人**

运行在用户本地电脑上的 NodeJS/TypeScript 应用：通过 WhatsApp Web 会话持续监控指定群组，将新消息发送给 AI API（Perplexity AI 或 OpenAI）分析，按用户配置的关键词与主题判断相关性，命中时以私信形式通知用户并附带原消息链接。需提供至少一个 AI API key，用 setup.sh 交互式完成依赖安装、构建、PM2 配置与 WhatsApp 扫码认证；脚本面向 Unix-like 系统，Windows 需经 WSL 或 Git Bash 运行，另附带 Next.js 落地页。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于关键词/主题定制的 AI 相关性过滤
- 实时监控指定 WhatsApp 群并以私信通知（含原文链接）
- 支持 Perplexity AI 与 OpenAI 双提供商（至少需一个 API key）
- 本地运行，通过 setup.sh 一键完成安装、PM2 部署与扫码认证

## 适用场景

- 减少多个 WhatsApp 群的消息干扰，只接收感兴趣内容
- 及时获知群里关于特定话题或地点（如聚会）的讨论
- 在本地私密运行，避免消息数据交由第三方托管服务

## 场景标签

 · 领域:通讯/个人效率工具

## 证据(README 行号)

> L15: WhatsApp-AI-Filter is an open-source project designed to help you manage information overload in WhatsApp groups. R
> L105:  * New messages in those groups will be sent to the configured AI API (Perplexity AI or OpenAI) for analysis.

## 星数曲线

```mermaid
xychart-beta
    title "avikalpg/whatsapp-ai-filter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `c0a9ec1f59a9` · [字段定义](../../DATASET.md)*
