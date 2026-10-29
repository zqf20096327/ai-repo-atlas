# Hiberius/whatsapp-receptionist

⭐ 29 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Hiberius/whatsapp-receptionist) · [官网](https://github.com/Hiberius/whatsapp-receptionist) · 组织维护

**给欧洲中小商户的开源 WhatsApp AI 前台：自动预约与转人工**

多租户 SaaS 应用：通过 360dialog 官方 WhatsApp Business API 接收文本与语音消息（ElevenLabs 语音转文字），由 Anthropic Claude 理解意图、查询 Google Calendar 真实空闲时段并完成预约与提醒，触发守卫或用户请求时转人工并发邮件通知。含 pgvector 知识库 RAG、Stripe 订阅、意大利 SDI 电子发票、GDPR Art.15/17 端点与数据保留任务。技术栈为 Next.js 15 + Supabase，界面语言为意大利语（英文未翻译），RLS 策略在运行时未被实际执行是已知未决项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Google Calendar 真实可用性查询 + 数据库级防双重预约
- 语音消息经 ElevenLabs 转文字后由 Claude 处理
- 多租户架构：每租户独立 WhatsApp 号码、AI 人设与知识库（pgvector RAG）
- GDPR Art.15/17 导出删除、PII 日志脱敏、AES-256-GCM 凭据加密

## 适用场景

- 诊所等预约型商户在 WhatsApp 上自动接待与排期
- 搭建多租户预约 SaaS（已接好 RLS、Stripe、订阅计费）
- 需要欧洲 GDPR 合规与意大利电子发票的 B2B 部署

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L23: A customer sends a WhatsApp message — text or voice note — at 22:40 on a Sunday. The AI understands
> L29: - **Understands intent and books real appointments** on Google Calendar, with confirmations and reminders

## 星数曲线

```mermaid
xychart-beta
    title "Hiberius/whatsapp-receptionist 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24", "2026-10-29"]
    y-axis "stars" 25 --> 30
    line [26, 27, 28, 29, 29]
```

2026-10-18 26 → 2026-10-29 29（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8d55ed06df7e` · [字段定义](../../DATASET.md)*
