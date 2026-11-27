# Renanuya/buymeatokens-oss

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/Renanuya/buymeatokens-oss) · [官网](https://buymeatokens.com) · 个人维护

**让开源开发者接受 AI token 赞助的自建筹资页面**

面向开源开发者的赞助平台：创作者用 GitHub 登录认领个人页面，支持者购买"token 捆绑包"，款项直接进入创作者自己的 Stripe、PayPal 或 Base 链上的 USDC 钱包，平台不经手资金也不抽成。关键机制包括 AES-256-GCM 加密存储的受限 Stripe 密钥、PayPal IPN 验证、链上 Transfer 日志核验、README SVG 徽章。可选 AI 功能基于 Gemini 或 Groq 免费额度从 README 草拟项目描述，设每日上限。要求 Node.js 26 与 Docker 运行本地 Postgres。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支付直达创作者自己的 Stripe/PayPal/USDC 钱包，平台不抽成
- Stripe 受限密钥 AES-256-GCM 加密存储，无需 webhooks
- 三种支付通道：Stripe、PayPal IPN、Base 链上 USDC（实验性）
- 可选 AI 描述草拟（Gemini/Groq 免费额度，按创作者与每日限额）

## 适用场景

- 为开源项目接受社区对 AI 用量的赞助
- 在项目 README 挂徽章展示筹集进度
- 自托管一个不抽成的赞助页面平台

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: Open source developers get a page where supporters fund the AI tokens behind their projects.
> L29: |**Write with AI**|Optional: drafts the project description from the repository's README (Gemini or Groq free tiers


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `8200b62e4502` · [字段定义](../../DATASET.md)*
