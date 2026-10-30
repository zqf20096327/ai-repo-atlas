# radcrew/real-estate-consultant

⭐ 17 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/radcrew/real-estate-consultant) · [官网](https://real-estate-consultant-fe.vercel.app) · 个人维护

**AI 辅助商业地产搜索与经纪人外联草稿的内部 MVP 应用**

面向商业地产工作流的内部 MVP：房源合法抓取与归一化、基于条件的匹配排序、保存搜索与关注列表，并生成经纪人外联草稿（不自动发送）。前端 Next.js、后端 FastAPI、Supabase 存储数据、AWS Cognito 登录；聊天 LLM 默认经 OpenRouter 或 Hugging Face 调用，可选路由到 AWS Bedrock（嵌入/外联）或 Lambda 自托管 Qwen（条件解析），未配置时关闭。另含 MCP 适配器，向 Cursor、Claude Desktop 等 AI 宿主暴露搜索与外联接口。本地用 pip/npm 启动，前后端及 MCP 均可部署到 Vercel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 房源抓取、匹配排序、保存搜索与关注列表
- 生成经纪人外联草稿（无自动发送）
- LLM 经 OpenRouter/Hugging Face 路由，可选 Bedrock 与 Lambda 自托管 Qwen
- MCP 适配器向 Cursor/Claude Desktop 等 AI 宿主暴露搜索与外联功能

## 适用场景

- 商业地产经纪人按条件搜索并排序房源
- 维护关注列表并生成外联草稿
- 通过 MCP 在 Cursor 等 AI 宿主中调用搜索与外联功能

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L3: Internal MVP for an **AI-assisted commercial real estate search** workflow: intake, lawful listing ingestion, proper
> L15: |**LLM**|OpenRouter and/or Hugging Face|Structured chat for intake, fit summaries, and outreach drafts (`OPENROUTER
> L16: |**LLM (optional)**|AWS Bedrock + Lambda|Per-call-site routing to Bedrock (embeddings, outreach) or a self-hosted Q

## 星数曲线

```mermaid
xychart-beta
    title "radcrew/real-estate-consultant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `924a91f1918a` · [字段定义](../../DATASET.md)*
