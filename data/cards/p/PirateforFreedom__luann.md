# PirateforFreedom/luann

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/PirateforFreedom/luann) · 个人维护 · 中文 README

**构建与部署多类型 LLM agent 的开发框架与服务**

基于 MemGPT 代码库改造的轻量级 agent 开发框架（原名 TypeAgent）：提供长期/短期记忆模块、基于外部数据源（如 PDF）的基础 RAG 工作流、自定义工具调用、人设与角色扮演，支持创建 MemGPT 等类型 agent（openhands 标记为不支持）。可经 pip 安装后以 `luann server` 启动服务端，在 localhost:8283 提供开发者门户、RESTful API 与客户端，用于构建多用户多 agent 应用。默认使用 SQLite，可通过环境变量连接 PostgreSQL。模型接入层面支持 OpenAI、Azure、Gemini、Claude、vLLM、Ollama 等端点。文档标注 Coming，功能仍在开发中（如前端新版、agent 评测等列入 TODO）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 长期/短期记忆管理与状态管理模块
- 自定义工具定义与调用、基础 RAG 工作流
- 以服务形式部署多用户多 agent 应用（RESTful API + 开发者门户）
- 模型/提供商无关设计，支持 OpenAI、Azure、Gemini、Claude、vLLM、Ollama

## 适用场景

- 开发带记忆与工具调用的对话型 agent
- 将 agent 以服务形式部署给多用户使用
- 基于 PDF 等外部数据源构建知识库问答 agent

## 场景标签

`Agent 框架` `Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L9: Luann makes user easy to build and deploy LLM agents with support for:
> L16: You can also use Luann to deploy agents as a *service*. You can use a Luann server to run a multi-user, multi-agent

## 星数曲线

```mermaid
xychart-beta
    title "PirateforFreedom/luann 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a8d580cfd61a` · [字段定义](../../DATASET.md)*
