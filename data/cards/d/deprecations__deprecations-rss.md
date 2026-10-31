# deprecations/deprecations-rss

⭐ 18 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/deprecations/deprecations-rss) · [官网](http://deprecations.info/) · 组织维护

**AI 厂商模型弃用公告的 RSS/JSON 聚合订阅源**

每日由 GitHub Actions 抓取 OpenAI、Anthropic、Google、AWS Bedrock、Cohere、Groq、xAI、Azure 等 9 个厂商的模型弃用页面，抽取模型 ID、下线日期等元数据，以 RSS、JSON Feed 与 Raw JSON 三种格式发布在 deprecations.info，无需认证或 API key。多区域生命周期日期不一致时，按模型 ID 折叠并取最早日期，可能残留区域差异。README 提供 Feedly、邮件、Slack 订阅方式及 Python/TypeScript/Shell/Ruby 的自动化示例代码。面向依赖第三方 AI 模型的开发与运维者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每日抓取 9 个 AI 厂商的弃用公告页面
- 提供 RSS、JSON Feed 与 Raw JSON 三种格式，无需认证
- 结构化元数据含模型 ID、下线日期、厂商
- 附 Python/TypeScript/Shell/Ruby 自动化通知示例代码

## 适用场景

- 在 RSS 阅读器中跟踪所用 AI 模型的下线时间
- 应用依赖的模型被弃用时自动创建 GitHub Issue 或发送告警
- 向团队 Discord/Slack 频道推送弃用通知

## 场景标签

 · 领域:AI 基础设施/信息聚合

## 证据(README 行号)

> L9: Never miss an AI model shutdown again. Track AI model deprecation announcements
> L51: 1. GitHub Actions runs daily at 2 AM UTC
> L52: 2. Scrapes each provider's deprecation page

## 星数曲线

```mermaid
xychart-beta
    title "deprecations/deprecations-rss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e3db8e7df937` · [字段定义](../../DATASET.md)*
