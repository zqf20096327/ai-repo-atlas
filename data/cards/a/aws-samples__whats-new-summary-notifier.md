# aws-samples/whats-new-summary-notifier

⭐ 50 · TypeScript · MIT-0 · 推送 2026-08-05 · [GitHub](https://github.com/aws-samples/whats-new-summary-notifier) · 组织维护

**自动摘要 AWS What's New 等网页并推送 Slack/Teams 的生成式 AI 应用**

AWS 官方 samples 提供的示例实现：监控 AWS What's New 等网页更新，用生成式 AI 将文章内容摘要为多语言版本，通过 Webhook 推送到 Slack 或 Microsoft Teams。以 AWS CDK 技术栈部署（CloudShell + CodeBuild 自动化），交互式向导选择通知目标、摘要语言并输入 Webhook URL；附带本地 Management Console Web 应用用于管理部署、更新配置、监控构建与查看数据，支持多租户部署选项。面向使用 AWS 云、希望自动跟踪 AWS 更新资讯并做团队通知的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监控 AWS What's New 等网页更新并生成多语言摘要
- 摘要推送到 Slack 或 Microsoft Teams（Webhook）
- deploy.sh 交互式部署向导，经 CloudShell/CodeBuild 自动化
- 本地 Management Console 管理部署与监控构建

## 适用场景

- 自动跟踪 AWS What's New 更新并推送到团队频道
- 把指定网页文章摘要成多种语言进行通知
- 作为 AWS Serverless 生成式 AI 应用的参考实现

## 场景标签

`网页抓取` `AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Whats New Summary Notifier** is a sample implementation of a generative AI application that summarizes the content

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/whats-new-summary-notifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7a2ddad69082` · [字段定义](../../DATASET.md)*
