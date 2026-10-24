# AlephantAI/AIephant-AI-Agent-Gateway

⭐ 114 · Rust · GPL-3.0 · 推送 2026-06-12 · [GitHub](https://github.com/AlephantAI/AIephant-AI-Agent-Gateway) · [官网](https://alephant.io) · 组织维护 · 中文 README

**自托管/托管的 OpenAI 兼容 AI 网关：路由、管控与观测多提供商 LLM 流量**

用 Rust 编写的 OpenAI 兼容 AI Agent 网关，面向生产 AI 应用：统一 API 面（/v1/*、/router、provider 直通），适配 50+ 提供商与 320+ 模型及自定义后端，提供策略路由、重试与回退、KV/语义缓存、虚拟密钥、请求日志与审计。可作为 Alephant Cloud 托管 SaaS 使用，或从源码自托管（需 Rust 工具链与 PostgreSQL，可选 Redis/Qdrant/S3）。当前为 0.2.0-beta 版本，公开 API 可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容统一入口，适配 50+ 提供商、320+ 模型与自定义后端
- 策略路由、重试回退、429 处理与 fail-open 缓存路径
- 网关侧 KV 缓存与语义缓存，路由/密钥变更免重启热加载
- 虚拟密钥隔离、请求日志与可选请求体归档

## 适用场景

- 多个 LLM 提供商接入收敛为一个 OpenAI 兼容端点
- 团队对 AI 流量做密钥管控、配额策略与审计
- 在自有基础设施内自托管网关并保留提供商凭据控制权

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L41: Alephant AI Gateway is an OpenAI-compatible control layer for production AI applications, available as hosted SaaS 
> L68: |One API surface|OpenAI-compatible `/v1/*` and `/ai/*` routes for chat, responses, embeddings, images, and provider

## 星数曲线

```mermaid
xychart-beta
    title "AlephantAI/AIephant-AI-Agent-Gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-24 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f713a53652d2` · [字段定义](../../DATASET.md)*
