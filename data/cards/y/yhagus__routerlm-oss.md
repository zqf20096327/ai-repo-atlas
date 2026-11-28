# yhagus/routerlm-oss

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/yhagus/routerlm-oss) · 个人维护

**自托管 AI 网关：统一多供应商模型端点、故障转移与成本追踪**

介于本地工具与上游模型供应商之间的自托管网关：为每个应用签发独立 API Key 并限定可用模型，按 Model→Route 顺序做限流/5xx/超时的自动故障转移与账户冷却；记录每请求的 token、缓存读写、首字延迟与美元成本；不存储提示词与响应内容，仅保留凭证脱敏的失败请求捕获（默认 7 天）。通过 Docker Compose 发布镜像运行，含 Caddy 边缘代理、PostgreSQL、Redis、双角色后端与仪表盘。

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

- OpenAI 与 Anthropic 两种客户端格式的统一网关端点（chat/images/speech/transcription/videos）
- Route 级自动 fallback：限流/5xx/超时切换下一 Route，失败账户进入 Cooldown
- 每请求成本追踪（token、缓存读写、TTFT、USD）与 per-key/per-Model 用量视图
- 密钥 AES-256-GCM 加密，不存储提示词内容；支持 Ollama/vLLM 等私有上游

## 适用场景

- 为 Cursor、Claude Code、CI 等多工具统一分发和轮换 API Key
- 多供应商账户间自动故障转移与配额耗尽跳过
- 追踪团队每个请求的模型调用成本
- 接入内网 Ollama/vLLM 私有上游统一管理

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7:  A self-hosted AI gateway with fallback across providers, per-request cost tracking and a dashboard to run it all.
> L20: **RouterLM sits between your tools and those providers:**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `09936881f36d` · [字段定义](../../DATASET.md)*
