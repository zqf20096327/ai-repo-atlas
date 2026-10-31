# vedantxn/nextly

⭐ 41 · TypeScript · 推送 2026-05-10 · [GitHub](https://github.com/vedantxn/nextly) · [官网](https://nextly.live) · 个人维护

**用自然语言提示生成 Next.js 应用的 AI 生成器**

面向开发者与非编程用户的 Next.js 应用生成工具：输入自然语言描述，由 Grok 4 模型生成含 TypeScript 与 Tailwind CSS 的完整 Next.js 代码，并通过 e2b.app 沙箱自动部署提供预览 URL，支持对话式迭代修改。技术栈包含 Clerk 认证、Prisma/PostgreSQL、tRPC、Inngest 后台任务与 E2B 代码执行。README 声明 beta 阶段限制：生成与部署最长约 10 分钟、预览 10-30 分钟后失效、存在速率限制、可能产生 TypeScript 编译错误，适用于中小型项目。本地运行需 Node.js 18+ 与 PostgreSQL，从源码克隆安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言提示生成完整 Next.js 应用（TypeScript + Tailwind CSS）
- E2B 沙箱自动部署并提供即时预览 URL
- 对话式迭代修改已生成应用
- beta 期间使用 Grok 4，README 声明不设使用量上限

## 适用场景

- 快速生成落地页、作品集、博客、仪表盘等原型
- 非编程用户通过提示词获得可运行的 Next.js 代码
- 开发者跳过样板代码搭建中小型项目

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3:  AI-powered Next.js application generator that transforms natural language prompts into production-ready code. From 
> L22: **⚡ Prompt-to-Code Next.js Apps**
> L98: |AI Model|Grok 4|Advanced language model for code generation|

## 星数曲线

```mermaid
xychart-beta
    title "vedantxn/nextly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `893d513e4eb9` · [字段定义](../../DATASET.md)*
