# ansvisor/ansvisor

⭐ 253 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/ansvisor/ansvisor) · [官网](https://ansvisor.com) · 组织维护

**给品牌方追踪 AI 搜索可见性并由 agent 起草修复的开源平台**

开源的 agentic AI 搜索执行平台：跨 ChatGPT、Google AI Overviews、Gemini、Claude、Grok 等 AI 平台追踪品牌提示词、提及、引用、竞品与 AI 流量，将信号转化为按 KPI 排序的行动清单，由 Content Agent 起草页面修改，需人工批准后上线。提供 Action Center、对话式 Chat、可定时的 agent 目录、内容编辑器、站点审计与 MCP Server。依赖 Supabase 与至少一家 AI Provider 的 API key；可自托管（Node.js >= 20 / Docker）或使用托管云。

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

- 跨 8+ AI 平台监测品牌可见性、引用与竞品差距
- Agent 将信号转为优先行动并起草修复，人工批准生效
- Agentic Content Editor 按品牌事实与内容规则校验草稿
- 通过 MCP Server 接入 AI 助手与 agent 工作流

## 适用场景

- 追踪品牌在 ChatGPT/Gemini 等 AI 回答中的提及与引用
- 让 agent 起草内容优化方案并按批准流程上线
- 对比竞品的 AI 可见性与 share of voice
- 将 AI 搜索可见性与网站转化、收入数据关联分析

## 场景标签

 · 领域:AI 搜索/品牌可见性分析

## 证据(README 行号)

> L14: Ansvisor is an **open-source, agentic AI Search Execution Platform**. It shows how your brand appears in AI answers
> L18: Track prompts, mentions, citations, competitors, AI traffic, and the sources AI systems rely on. Then act on them i
> L51: - **Agents** — Save a skill, mode and connections as an agent. Pick one from the ready-to-use catalog, run it on a 

## 星数曲线

```mermaid
xychart-beta
    title "ansvisor/ansvisor 星数(近 23 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 150 --> 262
    line [159, 161, 163, 165, 190, 211, 215, 216, 218, 222, 161, 234, 237, 238, 239, 241, 242, 243, 246, 247, 249, 250, 253]
```

2026-10-24 159 → 2026-11-26 253（+94）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `c4c903d8e433` · [字段定义](../../DATASET.md)*
