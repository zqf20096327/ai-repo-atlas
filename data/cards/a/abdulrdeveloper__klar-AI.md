# abdulrdeveloper/klar-AI

⭐ 13 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/abdulrdeveloper/klar-AI) · [官网](https://klar.abdulrdeveloper.me) · 个人维护

**面向学生的免费 AI 家教：免登录即可对话**

基于 Next.js 16 与 React 19 的开源 AI 家教 Web 应用，面向学生提供即时问答，支持英语、罗马乌尔都语与乌尔都文回答。提供 Flash/Speed/Smart/Thinking/Coder/Deep 六种回答模式，模型路由优先 Mistral、不可用时回退 Groq（基于 Vercel AI SDK）。游客可直接使用 /chat，注册后经邮箱验证获得带保存历史的仪表盘；会话由 JWT cookie 保护，密码 bcrypt 哈希，Upstash Redis 做限流，Resend 发送邮件。自部署需 Node.js 20+、pnpm、PostgreSQL 及各 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六种回答模式（Flash/Speed/Smart/Thinking/Coder/Deep）
- Mistral 优先、Groq 回退的模型路由
- 免登录即用，注册后保存逐会话历史
- JWT 会话、bcrypt、Redis 限流与邮件验证的安全机制

## 适用场景

- 学生做作业时即时提问并要求引导式解答
- 用乌尔都语/罗马乌尔都语学习，技术术语保留英文
- 自行部署一份可保存对话历史的 AI 家教服务

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5:  Klar is a free, open-source AI tutor for students. Ask a question and start
> L20: Klar is built for school prep, coding help and quick explanations. It is told
> L40: Each mode routes to Mistral first and falls back to Groq if the first provider

## 星数曲线

```mermaid
xychart-beta
    title "abdulrdeveloper/klar-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `08c04d3c4101` · [字段定义](../../DATASET.md)*
