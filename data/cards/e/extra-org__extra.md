# extra-org/extra

⭐ 117 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/extra-org/extra) · [官网](https://docs.extra-ai.co/docs/introduction) · 组织维护

**把现有产品接入 AI 助手的编排引擎，无需重写后端**

面向产品团队的 AI 编排引擎：通过 YAML 定义 orchestrator 与多个 AI specialist，将用户请求路由到各专家代理，由其调用既有 API、工具与 MCP 服务器执行真实产品工作流。业务逻辑、数据与鉴权保留在用户后端，LLM 之外完成授权。以 Docker 镜像提供 generate 脚手架与 agent-manager 服务（对话 API、历史、可嵌入聊天组件），支持 Anthropic/OpenAI/Gemini/Bedrock 云端或本地 Ollama 模型，另含 Langfuse 追踪与人工审批。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 定义 orchestrator 与 AI specialist 的显式编排图
- 复用既有 API 与业务逻辑，无需后端重写
- Docker 一键生成脚手架并运行 agent-manager（API/历史/聊天组件）
- 本地工具、MCP、LLM 之外授权与人工审批

## 适用场景

- 为我的产品嵌入能执行真实工作流的 AI 助手
- 用现有 API 搭建多专家路由的客服/计费代理
- 本地 Ollama 或云端模型运行产品级 agent 服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Turn your product into an AI-powered assistant.
> L104: Extra executes an explicit orchestration graph.

## 星数曲线

```mermaid
xychart-beta
    title "extra-org/extra 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-26 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fd16dcb03224` · [字段定义](../../DATASET.md)*
