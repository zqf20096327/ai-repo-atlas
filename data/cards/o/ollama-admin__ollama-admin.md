# ollama-admin/ollama-admin

⭐ 30 · TypeScript · 推送 2026-08-06 · [GitHub](https://github.com/ollama-admin/ollama-admin) · 组织维护

**Ollama 服务器的 GPU 监控、代理网关与多服务器管理面板**

面向运行多个 Ollama 服务器的团队的 Web 管理面板（TypeScript/Next.js）：通过可选的 GPU Agent（Python sidecar）采集 NVIDIA/AMD/Intel/Apple Silicon 的 VRAM、利用率、温度与功耗；所有 Ollama 流量经 /api/proxy 代理网关，记录 token、延迟、用户与 IP，支持按客户端 API key、角色访问控制、限流与多服务器路由；内含流式聊天、模型目录拉取与 OCR/嵌入工具。安装依赖 Docker 与 Docker Compose，本地开发需 Node.js 20+；面向单机个人用户的场景 README 自述不需要本产品。

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

- GPU Agent 采集 VRAM/利用率/温度/功耗，支持 NVIDIA/AMD/Intel/Apple Silicon
- Observable Proxy 记录每请求的 token、延迟、用户、IP，带指标面板
- 按客户端 API key、角色访问控制（admin/user）、限流与 GitHub OAuth
- 多服务器统一管理：模型拉取、路由、跨服务器模型操作

## 适用场景

- 团队共享 GPU 时追踪谁用了什么模型、消耗多少 token
- 在拉取新模型前判断 VRAM 是否足够
- 为多个 Ollama 实例提供统一入口与审计日志
- 给不同应用/团队分配独立 API key 并按需吊销

## 场景标签

`LLM 可观测性` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6:  Most Ollama UIs give you a chat box. Ollama Admin gives you visibility and control over what's actually happening o
> L52: - **Observable API gateway** — Every request to Ollama flows through a proxy that logs tokens, latency, model, user
> L257: All Ollama traffic goes through `/api/proxy` — never directly from clients to Ollama. This is what turns your Olla

## 星数曲线

```mermaid
xychart-beta
    title "ollama-admin/ollama-admin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `91891ee7c869` · [字段定义](../../DATASET.md)*
