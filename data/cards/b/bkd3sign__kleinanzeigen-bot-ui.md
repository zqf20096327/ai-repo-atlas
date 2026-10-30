# bkd3sign/kleinanzeigen-bot-ui

⭐ 17 · TypeScript · AGPL-3.0 · 推送 2026-08-04 · [GitHub](https://github.com/bkd3sign/kleinanzeigen-bot-ui) · 个人维护

** kleinanzeigen-bot 的自托管 Web 管理面板，含 AI 广告生成与自动回复**

为二手交易平台 bot kleinanzeigen-bot 提供基于 Next.js 的自托管 Web 界面：广告 YAML 的增删改查、批量操作、图片管理、与线上状态的自动同步与孤儿广告检测；可运行全部 bot CLI 命令，单一并发 FIFO 队列，每任务启动 Chromium 登录，支持 noVNC 实时观看与 MFA 流程；提供 cron 定时任务、自动降价、多用户 JWT 隔离、消息收件箱与统计仪表盘。AI 功能通过 OpenRouter（GPT-4.1-nano/mini）实现商品照片视觉分析与广告文案生成，以及可人工审核的 LLM 自动回复。AI 为可选功能，去掉后广告管理与调度仍可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传商品照片，AI 生成标题、描述、价格估算并自动选类（582 类）
- LLM 自动回复消息，支持审核模式、升级关键词检测与 AI 消息标记
- 广告全生命周期管理与线上状态自动同步、孤儿检测
- cron 定时任务、自动降价策略与多用户工作区隔离

## 适用场景

- 在一个面板里管理 kleinanzeigen.de 的广告发布与同步
- 拍照后让 AI 自动生成完整商品广告文案
- 让 AI 自动回复买家消息并在发送前人工审核
- 定时自动重发广告并按策略逐步降价

## 场景标签

`AI 写作` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **A self-hosted web interface for kleinanzeigen-bot**
> L64: - **Vision analysis** — Upload product photos, AI extracts details and generates a complete listing
> L172: - **AI auto-responder** — Automatic or review-mode reply generation via LLM (OpenRouter)

## 星数曲线

```mermaid
xychart-beta
    title "bkd3sign/kleinanzeigen-bot-ui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `80abed398d28` · [字段定义](../../DATASET.md)*
