# teabranch/open-responses-server

⭐ 184 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/teabranch/open-responses-server) · [官网](https://open-responses-server.teabranch.dev) · 个人维护

**把任意 OpenAI 兼容后端桥接为 Responses API 的服务器，支持 MCP**

面向开发者的 API 适配服务器：将 Ollama、vLLM、LiteLLM、OpenAI 等 OpenAI 兼容后端包装为 OpenAI Responses API 接口，使 Codex 等 Responses API 客户端可以对接自托管模型。提供有状态会话、工具调用、SSE 流式输出与 MCP 工具支持（Chat Completions 与 Responses 两套 API 均可）；通过环境变量配置后端地址、端口、会话上限等，提供 otc CLI 与交互式配置命令。安装途径为 pip（PyPI 发布）或源码，另提供 Docker 镜像（amd64/arm64/arm/v7）。项目自述为早期阶段但已可用于真实演示；持久化存储、网页搜索、文件搜索、代码解释器等列为待开发项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 作为 OpenAI Responses API 的替代服务端，桥接 Ollama/vLLM/LiteLLM 等后端
- Chat Completions 与 Responses API 均支持 MCP 工具
- 有状态会话与工具调用循环（可配最大 25 次迭代、100 条会话历史）
- 提供 otc CLI、PyPI 发布与 Docker 镜像（linux/amd64、arm64、arm/v7）

## 适用场景

- 让 OpenAI Codex 等仅支持 Responses API 的客户端跑在我自己的本地模型上
- 自托管 LLM 但保持 OpenAI API 兼容，减少客户端改造
- 通过 MCP 给本地模型接入外部工具

## 场景标签

 · 领域:LLM 基础设施/API 适配

## 证据(README 行号)

> L3: A plug-and-play server that speaks OpenAI’s Responses API—no matter which AI backend you’re running.
> L19: ✅ Acts as a drop-in replacement for OpenAI’s Responses API.

## 星数曲线

```mermaid
xychart-beta
    title "teabranch/open-responses-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 183 --> 186
    line [185, 184]
```

2026-10-18 185 → 2026-10-22 184（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d7e371f3d0e0` · [字段定义](../../DATASET.md)*
