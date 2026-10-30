# hoangsonww/AI-Gov-Content-Curator

⭐ 30 · TypeScript · MIT · 推送 2026-10-09 · [GitHub](https://github.com/hoangsonww/AI-Gov-Content-Curator) · [官网](https://synthoraai.vercel.app) · 个人维护

**为政府人员聚合、AI 摘要并展示新闻文章的多服务系统**

monorepo 多服务系统：爬虫定时抓取政府网站与公共 API 的文章，后端用 Gemini 生成摘要并存入 MongoDB，Next.js 前端提供浏览、文章问答、偏见分析、相关文章推荐（Pinecone 向量相似度），并通过 Resend 发送每日新闻邮件。进阶组件含 LangGraph/LangChain 多 agent 管线（FastAPI 暴露）、Anthropic+Google 双供应商编排层（16 个 agent、意图路由）、暴露 28 工具的 MCP 服务器与 ACP 层。部署在 Vercel，另提供 Kubernetes/Helm/Terraform 部署工件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬虫+CRON 每日抓取政府网站文章，Gemini 生成摘要存 MongoDB
- 文章问答、偏见分析、向量相似度相关文章推荐
- LangGraph 多 agent 管线与 Anthropic+Google 双供应商 16-agent 编排层
- MCP 服务器暴露 28 工具/14 资源/7 提示词，含 ACP agent 间通信层

## 适用场景

- 政府工作人员每日获取可信来源文章的 AI 摘要
- 订阅每日新闻邮件更新
- 在网页上对文章提问、查看偏见分析与相关文章

## 场景标签

`网页抓取` `文档问答` `AI 写作` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L6: The **SynthoraAI - AI-Powered Article Content Curator** is a comprehensive, AI-powered system designed to aggregate,
> L38: The **SynthoraAI - AI-Powered Article Content Curator** system is designed to provide government staff with up-to-d
> L197:  - AI-powered features such as article Q&A, bias analysis, and related article recommendations using vector simila

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/AI-Gov-Content-Curator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c84c0a3677ec` · [字段定义](../../DATASET.md)*
