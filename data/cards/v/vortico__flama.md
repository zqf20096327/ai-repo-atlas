# vortico/flama

⭐ 304 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/vortico/flama) · [官网](https://flama.dev) · 组织维护

**把预测与生成模型打包为生产 API 的 Python 服务框架**

面向开发者的模型服务框架：将 scikit-learn、TensorFlow、PyTorch 或 LLM 打包为单一 .flm 便携格式，通过 flama serve 一条命令以 HTTP API 形式运行，并同时暴露 OpenAI/Anthropic/Ollama 兼容端点与内置流式聊天 UI。生成式后端在 Linux 上用 vLLM（CUDA）、Apple Silicon 上用 MLX，加载时自动选择。另含 MCP 原生支持、自描述元数据/离线推理 CLI、基于 flama.json 的多模型部署与官方 Docker 镜像，以及完整的 API 框架功能（CRUD 资源、依赖注入、OpenAPI 文档、JWT 等）。以 pip 安装，无需 Rust 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意主流框架模型打包为单一 .flm 便携格式，一条命令以 HTTP API 服务
- 同时提供 OpenAI/Anthropic/Ollama 兼容端点与内置流式聊天 UI
- 原生 MCP 支持，装饰器声明工具并由类型注解推导 JSON Schema
- Rust 实现核心（路由/JSON 编码/请求解析/压缩），官方 Docker 镜像部署

## 适用场景

- 把训练好的机器学习模型快速变成可调用的生产 API
- 自托管 LLM 服务并让现有 OpenAI/Anthropic/Ollama 客户端直接接入
- 通过 MCP 把工具暴露给 Claude、Cursor 等 AI agent 客户端
- 用 flama.json 与 CI 元数据审查管理多模型部署

## 场景标签

 · 领域:机器学习/LLM 服务与 API 框架

## 证据(README 行号)

> L28: Turn any model into a production API in a single line of code. Serve predictive and
> L34: into a single portable format (the `.flm` file), so every model looks the same to your API
> L41: - 🤖 **Generative AI serving.** Serve LLMs with OpenAI-, Anthropic-, and Ollama-compatible endpoints, side by side.

## 星数曲线

```mermaid
xychart-beta
    title "vortico/flama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 303 --> 305
    line [304, 304]
```

2026-10-18 304 → 2026-10-22 304（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4c1f3a54030e` · [字段定义](../../DATASET.md)*
