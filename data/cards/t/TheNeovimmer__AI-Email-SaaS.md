# TheNeovimmer/AI-Email-SaaS

⭐ 18 · TypeScript · MIT · 推送 2026-09-14 · [GitHub](https://github.com/TheNeovimmer/AI-Email-SaaS) · [官网](https://normal-human.com/) · 个人维护

**基于 Nylas 的邮件客户端模板，AI 功能已移除**

Next.js 16 全栈邮件客户端示例：Better Auth 邮箱密码登录、Nylas v8 接入邮件与日历（多账号切换、读取线程、发送邮件、webhook、日历事件演示）、Neon Postgres + Prisma 7 存储与线程缓存、tRPC 组织 API。AI 聊天与撰写功能已被 stub（Vercel AI SDK 相关代码移除），Clerk/Stripe/Aurinko 亦已移除，旧 Aurinko 路由返回 410。面向想基于 Nylas 搭建邮件应用的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Nylas v8 grant 机制接入邮件与日历，支持多账号切换
- Better Auth 邮箱密码认证与 tRPC 服务端 API
- 线程列表经数据库缓存，详情实时拉取
- AI 聊天/撰写功能已 stub，相关 SDK 移除

## 适用场景

- 基于 Nylas 快速搭建邮件客户端原型
- 学习 Nylas 多账号授权、webhook 与日历事件接入
- 作为 Next.js + Prisma + tRPC 的全栈示例工程

## 场景标签

 · 领域:邮件/通讯应用

## 证据(README 行号)

> L5: Minimal AI-powered email client. Next.js 16 + Better Auth (email/password) + Nylas (mail + calendar) + Neon Postgres
> L49: - Clerk, Stripe, Aurinko removed. Old Aurinko routes return 410. AI chat/compose stubbed (ai SDK v7 `ai/react`/`ai/

## 星数曲线

```mermaid
xychart-beta
    title "TheNeovimmer/AI-Email-SaaS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `61a80faf8216` · [字段定义](../../DATASET.md)*
