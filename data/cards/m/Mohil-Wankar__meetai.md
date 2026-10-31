# Mohil-Wankar/meetai

⭐ 14 · TypeScript · 推送 2026-06-06 · [GitHub](https://github.com/Mohil-Wankar/meetai) · [官网](https://meetai-ten-lake.vercel.app) · 个人维护

**与专项 AI 角色实时语音对话的对话平台**

基于 Next.js 15 / React 19 / TypeScript 构建的 SaaS 式对话平台：用户通过实时语音与具备上下文记忆的 AI 角色对话，提供面试教练、语言导师、销售教练、职业导师等多种人格。底层使用 OpenAI Realtime API 与 Stream Video/Chat SDK，数据存于 Neon PostgreSQL（Drizzle ORM），Inngest 负责后台生成摘要、转录与分析。该 README 未提供安装或运行命令，属学术项目（本科毕业设计）。应用面覆盖面试练习、语言学习、销售培训等场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 低延迟实时语音对话，基于 OpenAI Realtime API
- 多种专项 AI 角色（面试/语言/销售/职业/学习助手）
- Inngest 后台自动生成转录、摘要与洞察
- Better Auth 认证与 Polar 订阅计费的 SaaS 架构

## 适用场景

- 与 AI 面试官练习技术和 HR 面试
- 通过互动对话提升外语口语
- 演练销售话术、异议处理与谈判
- 获取个性化的学习辅导与职业建议

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L13: *An intelligent SaaS platform where users can interact with specialized AI agents through natural, real-time voice 
> L17: MeetAI is a next-generation AI conversational platform that enables **real-time human–AI interaction** through voic
> L108: |OpenAI Realtime API|AI Conversations|

## 星数曲线

```mermaid
xychart-beta
    title "Mohil-Wankar/meetai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7439f1ff59d9` · [字段定义](../../DATASET.md)*
