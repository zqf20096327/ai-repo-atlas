# prasadus92/vertex-proxy

⭐ 18 · Python · MIT · 推送 2026-07-11 · [GitHub](https://github.com/prasadus92/vertex-proxy) · [官网](https://pypi.org/project/vertex-proxy/) · 个人维护

**本地代理：把 Anthropic/Gemini/OpenAI 协议客户端接入 Vertex AI**

运行于 127.0.0.1:8787 的本地 Python 代理，接收 Anthropic Messages、Gemini generateContent、OpenAI Chat Completions 三种 API 请求，转换并转发到 Google Cloud Vertex AI 的 publisher-model 端点，自动处理服务账号短时 OAuth token 的刷新循环。支持流式输出、Claude 模型 ID 别名映射、Vertex MaaS 伙伴模型（Kimi/GLM/MiniMax/Qwen/Grok）路由，以及可选的本地 Ollama 后端自动发现。面向已有静态 URL API 客户端（Claude Code、Hermes Agent、Cline 等）的开发者，目标是消耗 GCP 额度、统一计费或获得更高配额。默认无鉴权，仅设计为本地回环使用。

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

- 三种公共 API 协议到 Vertex AI 的请求转换与流式支持
- 自动服务账号 token 刷新（默认 50 分钟周期）
- OpenAI↔Anthropic 协议互译，OpenAI SDK 客户端可直接调用 Claude
- 可选 Ollama 本地后端自动发现与路由
- 提供 Prometheus /metrics 与可选 bearer-token 鉴权

## 适用场景

- 让 Claude Code、Hermes Agent 等客户端改走 Vertex AI 计费
- 统一多家模型供应商到 GCP 项目账单
- 把本地 Ollama 模型纳入同一 OpenAI 兼容入口

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A small, local-only proxy that bridges **any tool speaking the Anthropic Messages API, Gemini API, or OpenAI Chat Co
> L19: The problem: Vertex uses **short-lived OAuth access tokens** from a service-account key. Most tools expect a static
> L21: vertex-proxy runs on `127.0.0.1:8787`, handles the auth refresh loop, and translates between the public API shapes 

## 星数曲线

```mermaid
xychart-beta
    title "prasadus92/vertex-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `86de3bcb184e` · [字段定义](../../DATASET.md)*
