# fdueblab/Micro-Agent

⭐ 101 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/fdueblab/Micro-Agent) · 组织维护 · 中文 README

**面向垂域应用的轻量级 AI Agent 框架，以 API 服务交付**

基于 FastAPI 与 litellm 的 Python Agent 框架：核心为 ReAct 执行引擎（Think→Act→Observe），配合 Skills 垂域知识注入、内置 RAG 检索、会话记忆与 MCP 工具集成，通过统一 LLM 接口支持 OpenAI/DeepSeek/Claude/Ollama 等任意 litellm 兼容模型，并支持多 LLM Profile 配置。开发者以三步（编写 Prompt 模板、注册任务、调用 API）将通用 Agent 转为垂域专业智能体，以 uvicorn 或 Docker 启动 API 服务，内置 6 个示例任务参考实现，另含与后端 ioeb_backend 对接的 MCP 封装集成。

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

- litellm 统一接口，一套代码切换 OpenAI/DeepSeek/Claude/Ollama 等模型
- ReAct 执行引擎 + SubAgent 子任务分发 + REPL 沙箱执行
- Skills 垂域知识注入 + 内置 RAG 检索 + MCP 工具集成
- 多 LLM Profile 配置，按任务指定推理模型

## 适用场景

- 为特定行业快速构建专业 Agent 并以 API 服务交付
- 通过 Prompt 模板 + 任务注册将通用 Agent 定制为垂域智能体
- 参考内置示例任务实现代码分析、模型评测等场景

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L12: > 如果你需要为特定行业快速构建一个专业 Agent 并以 API 服务形式交付，Micro-Agent 是最短路径。
> L34: - **LLM Layer** — 通过 litellm 统一接口，一套代码切换 OpenAI / DeepSeek / Claude / Ollama 等任意模型

## 星数曲线

```mermaid
xychart-beta
    title "fdueblab/Micro-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-26 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0780b6406aa0` · [字段定义](../../DATASET.md)*
