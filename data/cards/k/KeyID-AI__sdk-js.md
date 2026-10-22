# KeyID-AI/sdk-js

⭐ 357 · TypeScript · 推送 2026-06-19 · [GitHub](https://github.com/KeyID-AI/sdk-js) · [官网](https://keyid.ai) · 组织维护

**为 AI agent 提供免注册真实邮箱地址的 TypeScript SDK**

面向 AI agent 开发者的邮件 SDK：agent 本地生成 Ed25519 密钥对，调用 provision() 即可在 KeyID.ai 服务上注册并获得真实邮箱地址，无需人工注册。服务端负责域名管理、轮换、信誉监控与送达性；SDK 提供收发、回复、转发、线程、草稿、联系人、Webhook、允许/屏蔽名单与用量指标等完整邮箱 API，支持定时发送、全文搜索、HTML 邮件与附件。要求 Node.js 18+，无外部依赖，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ed25519 密钥对质询-响应认证，provision() 三步获得邮箱
- 完整邮件 API：收发/回复/转发/线程/草稿/联系人/Webhook
- 支持定时发送、全文搜索、HTML 邮件、附件、自动回复
- 无外部依赖，仅需 Node.js 18+

## 适用场景

- 让 AI agent 拥有独立邮箱以收发邮件
- 构建以邮件为通道的 agent 工作流（定时发送、自动回复、Webhook）
- 为多 agent 系统批量开通可管理的邮件身份

## 场景标签

 · 领域:AI agent 基础设施/邮件通信

## 证据(README 行号)

> L3: **Free email addresses for AI agents. No signup. No human needed.**
> L5: Your agent gets a real email address in 3 lines of code. Send, receive, reply, search — full email capabilities with
> L7: KeyID.ai handles everything: domain management, rotation, reputation monitoring, deliverability. Your agent just gen

## 星数曲线

```mermaid
xychart-beta
    title "KeyID-AI/sdk-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 356 --> 358
    line [357, 357]
```

2026-10-18 357 → 2026-10-22 357（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ce533846def8` · [字段定义](../../DATASET.md)*
