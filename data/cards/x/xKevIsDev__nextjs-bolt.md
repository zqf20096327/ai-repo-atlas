# xKevIsDev/nextjs-bolt

⭐ 21 · TypeScript · 推送 2025-11-20 · [GitHub](https://github.com/xKevIsDev/nextjs-bolt) · 个人维护

**Next.js 实现的 Bolt：对话式 AI 全栈 Web 应用生成器**

对 StackBlitz Bolt OSS 项目的 Next.js 重实现，原版基于 Vite 与 Remix。用户通过聊天界面描述需求，AI 生成完整全栈 Web 应用代码，支持前端与后端组件，应用随修改实时自动更新。支持多个 AI 提供商（Anthropic、Google、TogetherAI），侧边栏可导航、选择模型与管理聊天记录。以源码方式安装：克隆仓库后 npm/yarn/pnpm/bun 安装依赖并运行开发服务器，需 Node.js v18+，通过 .env.local 配置环境变量。README 列出错误自动修复、版本控制、部署与 Supabase 集成等待实现项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话式 AI 生成全栈 Web 应用代码（前端+后端）
- 多 AI 提供商支持：Anthropic、Google、TogetherAI
- 实时更新：修改后应用自动更新
- 移动端响应式界面与可定制侧边栏

## 适用场景

- 通过对话快速生成全栈 Web 应用原型
- 在 Next.js 技术栈上搭建类似 bolt.new 的 AI 编程环境
- 自托管并自选 AI 提供商的应用生成工具

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: BoltNext is a cutting-edge application that allows you to build full-stack web applications using the power of AI. B
> L9: * **AI-Powered Code Generation:** Chat with the AI to describe your desired application, and BoltNext will generate 
> L12: * **Multiple AI Provider Support:** Choose from various AI providers like Anthropic, Google, and TogetherAI.

## 星数曲线

```mermaid
xychart-beta
    title "xKevIsDev/nextjs-bolt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7e9e1121ce0f` · [字段定义](../../DATASET.md)*
