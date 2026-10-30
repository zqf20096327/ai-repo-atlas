# anaslimem/llm-gateway-core

⭐ 18 · Python · MIT · 推送 2026-01-13 · [GitHub](https://github.com/anaslimem/llm-gateway-core) · 个人维护

**统一多 LLM 提供商接入的 FastAPI 网关：路由/缓存/限流/监控**

基于 FastAPI 的 LLM 网关：将多个模型提供商抽象到统一 API 之后，通过 Provider Router 按请求提示（online/local/fast/secure）动态选路；集成 Google Gemini（云端）与 Ollama（本地）。用 Redis 实现分布式响应缓存与基于 Lua 脚本的令牌桶原子限流（超限返回 429），通过 Prometheus 收集指标、Grafana 可视化，附 Streamlit 前端用于演示测试。整体栈通过 Docker Compose 部署，需 .env 配置 API key 与 Redis/Ollama 地址。

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

- 按请求提示动态选择提供商（online/local/fast/secure 四种模式）
- Redis 分布式缓存与 Lua 令牌桶原子限流（超限 429）
- Prometheus 指标导出与 Grafana 监控面板
- Docker Compose 一键部署完整栈

## 适用场景

- 通过统一 API 接入云端 Gemini 与本地 Ollama
- 对多客户端 LLM 访问做限流与成本控制
- 监控网关请求量、延迟与缓存命中率

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: LLM Gateway Core is a production-grade infrastructure component designed to abstract multiple Large Language Model 
> L16: The gateway is built on a high-performance FastAPI backend, utilizing a provider-agnostic interface that allows for

## 星数曲线

```mermaid
xychart-beta
    title "anaslimem/llm-gateway-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `64786301ae50` · [字段定义](../../DATASET.md)*
