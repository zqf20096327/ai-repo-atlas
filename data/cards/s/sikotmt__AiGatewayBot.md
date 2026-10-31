# sikotmt/AiGatewayBot

⭐ 15 · JavaScript · MIT · 推送 2026-07-28 · [GitHub](https://github.com/sikotmt/AiGatewayBot) · 个人维护 · 中文 README

**部署在 Cloudflare Workers 上的 Telegram AI 聊天机器人网关**

单文件 JavaScript 的 serverless Telegram 机器人，全部逻辑运行在 Cloudflare Workers 与 D1（SQLite）数据库上，无需 VPS、域名、外部库或 Wrangler CLI。作为 Telegram 用户与 AI 服务之间的网关，同时支持 9+ 提供商（Gemini 原生及 OpenAI 兼容 API），管理员可在 Telegram 内完成提供商增删、模型选择、用户封禁、额度控制、人格管理与群发消息。用户侧提供带 10 条记忆的对话、视觉图片分析、OCR 与人格切换。安装方式为下载 worker.js 粘贴到 Cloudflare 在线编辑器部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时接入 9+ AI 提供商，支持 OpenAI 兼容 API 与 Gemini 原生，自动检测类型并拉取模型列表
- Telegram 内建完整管理面板：提供商/模型/用户/人格/额度/群发管理
- 用户侧提供 10 条消息记忆、Vision 图片分析与 OCR、自定义人格
- 单文件零依赖部署于 Cloudflare Workers + D1，适配免费套餐

## 适用场景

- 不买服务器在 Cloudflare 免费套餐上部署自己的 Telegram AI 聊天机器人
- 在一个 Telegram 机器人里统一接入并切换多家 AI 提供商的模型
- 给自己社群的用户提供带额度限制和人格切换的 AI 问答服务

## 场景标签

`模型网关` `聊天机器人` `OCR` · 领域:Agent 开发

## 证据(README 行号)

> L281: |🔌 **Multi-Protocol**|Supports 9+ AI providers simultaneously|
> L294: |💬 **Smart Chat**|AI conversation with 10-message memory window|

## 星数曲线

```mermaid
xychart-beta
    title "sikotmt/AiGatewayBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a9f71e2977b2` · [字段定义](../../DATASET.md)*
