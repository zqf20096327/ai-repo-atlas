# Naruto859/MugenRoutes

⭐ 3 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Naruto859/MugenRoutes) · 个人维护

**自托管 LLM API 网关：管理上游、密钥轮换与代理路由**

基于 FastAPI 的自托管 LLM API 网关，将客户端统一接入一个服务，管理 OpenAI Chat Completions、OpenAI Responses 与 Anthropic Messages 三种上游格式，并在两种方言间翻译请求与响应（含工具调用）。关键机制：按优先级配置上游端点与回退规则、上游 API key 轮换（IST 每日重置）、Webshare 单代理故障恢复与冷却、SSE 流式转发、本地印地语转写。提供 Web 管理面板与 SQLite 存储，支持 Docker Compose 或 Python 部署，默认绑定 loopback。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Anthropic 双方言路由与翻译（含工具调用）
- 上游 key 轮换与每日重置，客户端使用独立网关 key 认证
- Webshare 单代理故障恢复：5 次连续传输失败触发 30 秒冷却
- SSE 流式转发并在上游运行期间保持客户端连接

## 适用场景

- 自托管统一管理多个 LLM 上游端点和密钥
- 为 OpenAI/Anthropic 客户端配置端点回退与故障转移
- 通过代理路由访问上游并管理出口 IP

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Mugen Routes is a self-hosted LLM API gateway for OpenAI Chat Completions,
> L5: service and manage upstream providers, API key rotation, proxy routing, and
> L31:     Client["OpenAI or Anthropic client"] --> Gateway["FastAPI gateway"]


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `697918e85553` · [字段定义](../../DATASET.md)*
