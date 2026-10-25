# aqstack/mimir

⭐ 94 · Go · MIT · 推送 2025-12-24 · [GitHub](https://github.com/aqstack/mimir) · [官网](https://aqstack.github.io/mimir/) · 组织维护

**LLM API 语义缓存代理：按语义相似度命中缓存，降低成本与延迟**

Go 编写的代理服务，部署在客户端与 LLM API 之间：将请求转为 embedding，与缓存中历史请求做语义相似度匹配，超过阈值即返回缓存响应，否则转发上游并缓存。作为 OpenAI 兼容的 drop-in 替代代理，客户端只需改指向地址。embedding 提供方可选 Ollama（本地免费）或 OpenAI API，支持可配置相似度阈值、TTL、最大缓存条数。单二进制、无需外部数据库，支持 Docker 部署，暴露 /stats 缓存统计与 /health 健康检查端点。面向希望降低重复/相似查询成本的开发者与运维场景。

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

- 基于语义相似度（默认阈值 0.95）而非精确匹配的缓存命中
- 支持 Ollama 本地 embedding（如 nomic-embed-text）或 OpenAI embedding
- OpenAI 兼容的 drop-in 代理，单二进制零外部依赖，支持 TTL 与缓存上限
- 提供 /v1/chat/completions 缓存端点、/stats 统计与 /health 检查

## 适用场景

- 应用中有大量重复或相似 LLM 查询时降低 API 成本
- 通过语义缓存减少重复请求的响应延迟
- Kubernetes 环境中作为 sidecar/代理统一缓存 LLM 调用

## 场景标签

 · 领域:LLM 基础设施/推理代理

## 证据(README 行号)

> L5: mimir is a drop-in proxy that caches LLM API responses using semantic similarity, reducing costs and latency for rep
> L21: │   Client    │────▶│    mimir    │────▶│  LLM API    │

## 星数曲线

```mermaid
xychart-beta
    title "aqstack/mimir 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-25 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `388a57d91bcc` · [字段定义](../../DATASET.md)*
