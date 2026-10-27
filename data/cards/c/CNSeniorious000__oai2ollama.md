# CNSeniorious000/oai2ollama

⭐ 78 · Python · 推送 2026-10-14 · [GitHub](https://github.com/CNSeniorious000/oai2ollama) · [官网](https://oai2ollama.vercel.app) · 个人维护

**把 OpenAI 兼容 API 包装成 Ollama 兼容 API 的 CLI 服务**

基于 FastAPI 的 CLI 工具：启动一个本地服务器，接收 Ollama 兼容 API 请求并转发到 OpenAI 兼容后端，使只支持 Ollama 接口的编码代理（如 GitHub Copilot for VS Code）能使用自定义 OpenAI 模型。支持通过 --capabilities 声明 tools/vision/thinking 等能力、--models 补充 /models 端点未返回的模型，可用 .env 配置。提供 uvx/pipx 直接运行与 Docker 构建/运行两种方式，监听端口默认 11434。注意：选项名 capacities 已弃用、改用 capabilities，旧名暂仍可用但发出弃用警告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 转 Ollama 兼容 API 的协议适配服务
- --capabilities 声明 tools/vision/thinking 等能力，恒含 completion
- --models 向 /api/tags 补充 /models 端点未返回的模型
- 支持 .env 配置与 Docker 部署

## 适用场景

- 让 GitHub Copilot for VS Code 等仅支持 Ollama 接口的编码代理使用自定义 OpenAI 模型
- 把已有 OpenAI 兼容后端以 Ollama 协议暴露给本地工具链
- 通过环境变量声明模型能力（视觉/工具调用/思考）供客户端识别

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This is a CLI tool that starts a server that wraps an OpenAI-compatible API and expose an Ollama-compatible API,
> L4: which is useful for providing custom models for coding agents that don't support custom OpenAI APIs but do support O

## 星数曲线

```mermaid
xychart-beta
    title "CNSeniorious000/oai2ollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `308fce1cad4e` · [字段定义](../../DATASET.md)*
