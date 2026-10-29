# sanidhyy/lovable-clone

⭐ 24 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/sanidhyy/lovable-clone) · [官网](https://clone-vibe.vercel.app) · 个人维护

**开源 Lovable 克隆：通过对话让 AI 生成应用与网站的 Next.js 应用**

基于 Next.js 16、React、TypeScript、Prisma、PostgreSQL（Neon）与 Tailwind 的 Web 应用，用户通过与 AI 对话创建应用和网站。AI 部分使用 OpenAI SDK 与 Inngest Agent Kit，代码沙箱执行依赖 E2B，认证由 Clerk 提供，支持订阅功能，内网穿透用 Ngrok。部署目标为 Vercel，本地运行需配置多个第三方服务的 API key，依赖用 pnpm/npm 安装。README 未声明维护状态承诺，提供 Issues/PR 贡献渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话式 AI 生成应用与网站，含 Demo 与 Code 视图
- E2B 沙箱执行生成代码，Inngest Agent Kit 编排 agent
- Clerk 认证与订阅功能
- Next.js 16 + Prisma + PostgreSQL(Neon) + tRPC 技术栈

## 适用场景

- 想自托管一个对话式 AI 应用生成器
- 学习此类 AI builder 的完整工程实现
- 在其基础上二次开发自己的 AI 建站产品

## 场景标签

`AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered application builder built with Next.js 16
> L156: - @inngest/agent-kit: ^0.13.2
> L198: - openai: ^7.5.0

## 星数曲线

```mermaid
xychart-beta
    title "sanidhyy/lovable-clone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `55c944999726` · [字段定义](../../DATASET.md)*
