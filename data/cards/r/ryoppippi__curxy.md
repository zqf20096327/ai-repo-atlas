# ryoppippi/curxy

⭐ 417 · TypeScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/ryoppippi/curxy) · [官网](https://jsr.io/@ryoppippi/curxy) · 个人维护

**让 Cursor 编辑器接入本地 Ollama 的代理服务器**

基于 Deno 与 Hono 的代理 worker：Cursor 编辑器的大模型请求会经过官方 Cursor 服务器转发，无法访问用户本地的 Ollama 服务；curxy 在本地监听端口，将请求转发给 Ollama 并通过 cloudflared 隧道生成公网 URL，用户把带 /v1 的 URL 填入 Cursor 的 OpenAI Base URL 覆盖配置即可使用本地模型。支持通过 OPENAI_API_KEY 环境变量做访问限制。以 JSR 包形式分发，需 Deno 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 转发请求到本地 Ollama 服务器并返回响应
- 自动启动 cloudflared 隧道生成公网访问 URL
- OPENAI_API_KEY 环境变量可选开启访问限制

## 适用场景

- 在 Cursor 编辑器中使用本地 Ollama 模型补全代码
- 不想让代码数据经官方服务器中转时自建通道

## 场景标签

 · 领域:开发工具/LLM 接入

## 证据(README 行号)

> L12: This is a proxy worker for using ollama in cursor. It is a simple server that
> L21: So, we need a proxy worker that can forward the data to the ollama server.

## 星数曲线

```mermaid
xychart-beta
    title "ryoppippi/curxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 415 --> 418
    line [416, 417, 417]
```

2026-10-18 416 → 2026-10-22 417（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b1484ea229ef` · [字段定义](../../DATASET.md)*
