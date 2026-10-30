# 10xshivam/Cenra

⭐ 35 · TypeScript · MIT · 推送 2026-04-22 · [GitHub](https://github.com/10xshivam/Cenra) · [官网](https://cenra.10xshivam.dev) · 个人维护

**面向 SaaS 的可嵌入 AI 客服代理，训练于自有文档**

Cenra 是面向现代 SaaS 公司的 AI 支持代理：通过 Firecrawl 与 Jina 抓取并向量化网站、文档与 FAQ，基于 Qdrant、LangChain/LangGraph 与 Gemini API 提供带对话记忆的实时流式回答，以可嵌入 HTML/React/Next.js 的 widget 形式交付。支持 AI 加人工的工单升级、客服分析、工作区管理、JWT 与 Google OAuth 认证，并内置 Dodo Payments 订阅计费。采用 Turborepo monorepo 与容器化 Docker 部署，需 Node.js ≥20 与 PNPM ≥10，配置多个环境变量后方可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从网站/文档/FAQ 自动向量化构建知识库（Firecrawl + Jina）
- 可嵌入 HTML/React/Next.js 的流式客服 widget，LangGraph 维护对话记忆
- AI 自动应答与人工升级的统一收件箱，附请求/解决/升级分析
- 内置订阅计费（Dodo Payments）与工作区管理

## 适用场景

- 在我的 SaaS 产品中嵌入一个懂自有文档的客服机器人
- 自动处理常规客服咨询并将复杂问题升级给人工
- 通过仪表盘追踪客服请求、解决率与升级趋势

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L9: Cenra is a production-ready AI support agent that deeply understands your business context, documentation, and produ
> L15: - **Product-Trained Knowledge**: Train Cenra on your website, docs, and FAQs. Automatically vectorize and ingest bu
> L16: - **Context-Aware Support**: LangGraph-powered conversational memory maintains context across messages and follow-u

## 星数曲线

```mermaid
xychart-beta
    title "10xshivam/Cenra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2d34b51954f6` · [字段定义](../../DATASET.md)*
