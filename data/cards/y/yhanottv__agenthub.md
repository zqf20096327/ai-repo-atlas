# yhanottv/agenthub

⭐ 20 · JavaScript · MIT · 推送 2026-08-01 · [GitHub](https://github.com/yhanottv/agenthub) · 个人维护

**Hermes Agent 的自托管 Web 界面：多智能体组织与成本追踪**

为 Nous Research 的 Hermes Agent 提供浏览器界面（含移动端）：在终端运行的 Hermes 之上加入具名持久智能体组织，CEO/manager/worker 三级排名、向低级别智能体的受追踪委派、以 [[双括号]] 链接的共享记忆并映射到 Jarvis 页面。从 Hermes 自身配置只读读取 skills 与 MCP 服务器并原样展示，按调用记录欧元成本并按模型/智能体/沙龙分摊。无 Hermes 时可对接任意 OpenAI 兼容服务。技术栈为 Node + 无框架 JavaScript + SQLite，共 3 个依赖，无构建步骤；提供 Docker Compose 部署，数据全部留在本地，无遥测。

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

- CEO/manager/worker 三级排名与委派规则服务端强制校验
- 读取 Hermes 配置原样展示 skills 与 MCP 服务器，无需重复声明
- 按调用计算欧元成本，按模型/智能体/沙龙分摊，无资费标记为下限
- 在 /inference/v1 暴露 OpenAI 兼容网关，Hermes 经其调用用户选择的供应商且不接触用户密钥

## 适用场景

- 在浏览器（含手机）中使用和编排多个智能体，而不是在终端操作 Hermes
- 自托管管理智能体对话、共享记忆与模型选择，并跟踪每笔调用的欧元成本
- 让本地智能体通过委派调用 Hermes 的 MCP 服务器（Blender、Unreal、n8n 等）

## 场景标签

`多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: AgentHub lui en donne une, et ajoute une organisation par-dessus : des agents
> L64: |🔀|**Fournisseurs de modèles**|Hermes, AgentRouter, OpenRouter, OpenAI, Gemini, Groq, Together, Ollama et tout endp

## 星数曲线

```mermaid
xychart-beta
    title "yhanottv/agenthub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3f883596200f` · [字段定义](../../DATASET.md)*
