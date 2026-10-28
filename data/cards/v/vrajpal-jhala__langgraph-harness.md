# vrajpal-jhala/langgraph-harness

⭐ 32 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/vrajpal-jhala/langgraph-harness) · [官网](https://vrajpal-jhala.github.io/langgraph-harness/) · 个人维护

**面向 GitLab 的自托管 AI 编程代理平台**

基于 LangGraph 构建的自托管平台，提供四种代理：MR 审查（webhook 触发读 diff 并发评论）、工作项/任务自主处理（在 Kata Containers VM 沙箱内运行并开 draft MR）、以及带 GitLab 工具访问的交互式聊天。支持 OpenRouter/Gemini/Groq/Ollama/sglang 多模型接入，BullMQ 队列与持久化检查点，评论发布前有筛查与运行中纠偏机制。需 Node.js 22+、Docker 与 GitLab 凭据，通过 npm 本地运行或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种代理共享同一基础：MR 审查、工作项处理、任务处理、聊天
- 代理运行在 Kata Containers VM 沙箱（每沙箱独立 guest 内核）
- 多模型接入：OpenRouter、Gemini、Groq、Ollama 或 sglang
- 持久化检查点支持运行中断后续跑，评论发布前筛查

## 适用场景

- GitLab 团队用 AI 自动审查合并请求
- 指派 issue 后由代理自主开 draft MR 并跟进评论
- 通过聊天界面向 AI 查询项目上下文并执行工具操作

## 场景标签

`代码审查` `编码 Agent` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L5: **Self-hosted AI coding agent platform for GitLab, built with LangGraph**
> L25: - 🔍 **MR Review** — fires on webhook events, reads the diff, drafts comments, publishes them. No polling, no manual
> L47: - **Agent** — Multi-provider LLM (OpenRouter, Gemini, Groq, Ollama, or sglang) with GitLab MCP tools and skill-base

## 星数曲线

```mermaid
xychart-beta
    title "vrajpal-jhala/langgraph-harness 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24", "2026-10-28"]
    y-axis "stars" 28 --> 33
    line [29, 30, 31, 32, 32]
```

2026-10-18 29 → 2026-10-28 32（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7a119af28980` · [字段定义](../../DATASET.md)*
