# damiansire/genai-fullstack-blueprint

⭐ 93 · TypeScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/damiansire/genai-fullstack-blueprint) · 个人维护

**多模态 GenAI 全栈参考架构：Angular + Node.js AI Gateway 脚手架**

TypeScript monorepo 形式提供的多模态生成式 AI 应用参考蓝图（自称 scaffold 而非 turnkey 产品）：Angular 22 独立组件前端 + Node.js/Express 分层后端构成 AI Gateway，接入 Google Gemini（文本生成、Vision OCR、Nano Banana 图像生成）与 OpenAI 双真实 provider，所有插件实现统一 IModelStrategy 端口，含熔断与 FALLBACK_MODEL_CHAIN 回退链。附带 RAG（可选 sqlite-vec）、提示注入启发式与 PII 掩码 guardrails、token/延迟计费观测、SHA-256 精确缓存。安装走 npm workspaces 或 Docker Compose；多租户为 roadmap 未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 IModelStrategy 插件端口接入 Gemini 与 OpenAI，含熔断与多级回退链
- Server-Driven Generative UI：基于 LLM Tool Calls 动态渲染组件，SSE 流式
- RAG 基础设施：可选 sqlite-vec 语义搜索 + 上下文注入，默认关闭
- Guardrails：提示注入启发式校验、PII 掩码、毒性过滤钩子
- LLMOps 观测：按用户/租户的 token 与 TTFT 追踪、OTLP 分布式追踪、精确匹配缓存

## 适用场景

- 作为多模态 GenAI SaaS 应用的起点脚手架进行二次开发
- 搭建带 provider 抽象与回退链的 AI Gateway
- 为 B2B 应用实现 RAG 私有数据问答与 token 计费追踪

## 场景标签

`图像生成` `RAG` `多模态` · 领域:内容生成

## 证据(README 行号)

> L5: This repository is a **reference blueprint** (a scaffold to build on, not a turnkey product) for modern, scalable we
> L46: ||**Express.js**|Minimalist framework for building RESTful APIs.|
> L133: - Routing across the plugins that ship today: three **Google** model plugins (`google-text-bison`, `gemini-image-g

## 星数曲线

```mermaid
xychart-beta
    title "damiansire/genai-fullstack-blueprint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-28 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9fdbabf09121` · [字段定义](../../DATASET.md)*
