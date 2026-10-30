# inklingfree/inkling

⭐ 15 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/inklingfree/inkling) · [官网](https://inkling.free) · 个人维护

**自托管的 WhatsApp 个人 AI 助理，代管邮件/日历/事务**

运行在独立 WhatsApp 号码上的个人助理：私聊或群聊对话，支持记忆、网页搜索、语音转写（gpt-4o-transcribe）、FLUX 生图、提醒、清单、投票；接入 Gmail/Drive/Google Tasks/Calendar，可选浏览器自动化代办（填表、订票）与经确认后以本人名义发消息。模型可切换 Azure OpenAI（推荐默认）、OpenAI、Claude 或任意兼容 OpenAI Responses API 的服务器；以 Baileys 非官方方式连接 WhatsApp，README 明示违反 WhatsApp 条款、号码可能被封，需用备用号。单 Node.js 进程，无数据库，数据 AES-256-GCM 加密，docker compose 可启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 Gmail/Drive/Calendar/Tasks，邮件草稿与日历事件管理
- 所有以本人名义发出或花钱的操作先经用户确认
- 模型可切换 Azure/OpenAI/Claude/兼容网关，`store:false` 不在提供商侧留存
- 经 Baileys 非官方接入 WhatsApp，README 明示封号风险，需用备用号

## 适用场景

- 在小群里让 AI 助理代管日程、邮件与待办提醒
- 让助理查票、找餐厅并发送预订页，确认后代为操作网站
- 自托管运行、自选模型提供商的私人聊天助理

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: A personal assistant that lives in WhatsApp, for you and a few friends. You text it the way you'd text a friend, on
> L101: WhatsApp (spare number) ──linked device──▶ inkling (Node.js) ──▶ GPT on Azure AI Foundry (or OpenAI, Claude, ...)

## 星数曲线

```mermaid
xychart-beta
    title "inklingfree/inkling 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fd328aff54b6` · [字段定义](../../DATASET.md)*
