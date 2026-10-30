# yuriy-kulakovskyi/ticker-mind

⭐ 16 · TypeScript · 推送 2026-10-29 · [GitHub](https://github.com/yuriy-kulakovskyi/ticker-mind) · 个人维护

**给订阅用户的市场分析后端：生成 AI 报告并发送邮件通知**

基于 NestJS + Prisma 的模块化后端服务，面向股票行情跟踪场景：管理订阅者的观察列表（watchlist）与股票代码，通过外部 API 获取并缓存市场数据，使用 Groq API 生成 AI 市场分析报告，并通过 Brevo 邮件服务向订阅者发送个性化通知。API 采用 JWT 认证，端点缓存 300 秒。运行需要 PostgreSQL 数据库及 Groq、NewsData.io、Brevo 等多项 API key。README 提供 npm 安装启动命令与完整 REST API 文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 观察列表（watchlist）与 ticker 的增删改查 API
- 通过 Groq API 生成 AI 市场分析报告
- Brevo 邮件服务发送订阅通知
- 市场数据缓存 300 秒，区分缓存读取与手动同步两条路径

## 适用场景

- 我需要一个后端来管理多个股票观察列表
- 我想为订阅者自动生成并发送 AI 市场分析报告
- 我想缓存市场数据以降低外部 API 负载

## 场景标签

`金融量化` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: This is the app that helps in analysing the market, generate automated reports and send news on subscribers' mails a
> L25: `GROQ_API_KEY` - Groq API key for AI-powered report generation

## 星数曲线

```mermaid
xychart-beta
    title "yuriy-kulakovskyi/ticker-mind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `185fcc4812f1` · [字段定义](../../DATASET.md)*
