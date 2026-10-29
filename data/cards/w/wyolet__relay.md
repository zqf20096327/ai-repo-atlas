# wyolet/relay

⭐ 29 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/wyolet/relay) · [官网](https://docs.wyolet.com) · 组织维护

**自托管 LLM 网关：统一端点路由多家提供商并管理密钥**

用 Go 编写的可自托管 LLM 路由器/网关，在 OpenAI、Anthropic、Bedrock、Vertex、Azure、Ollama、Groq 等提供商前放置单一 OpenAI/Anthropic 兼容端点。核心机制：自有 API 密钥池化与自动故障转移、按密钥的模型/提供商访问策略与限流、用量与成本计量（Postgres/ClickHouse 存储）、Prometheus 指标、Kubernetes 原生部署。一条 Docker 命令可启动含管理 UI、数据库与预置 400+ 模型目录的完整实例。批量处理功能标注为进行中（in progress）。Apache-2.0 许可，另提供商业托管与支持联系方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 OpenAI/Anthropic 兼容端点接入多家提供商，无需改代码切换上游
- 密钥池化、自动故障转移与按密钥的访问策略/限流
- 用量与成本计量存入 Postgres/ClickHouse，Prometheus /metrics
- Docker 一条命令启动完整实例（API+管理 UI+数据库+预置 400+ 模型目录）

## 适用场景

- 统一团队对多个 LLM 提供商的调用入口，不改动现有 SDK 代码
- 发放限额的临时密钥给外部用户而不暴露真实提供商密钥
- 自托管环境下观测每个请求的成本与用量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L22: Wyolet Relay puts a single **OpenAI- and Anthropic-compatible** endpoint in front
> L53: - **One API, every provider.** OpenAI- and Anthropic-shape endpoints in front of
> L83: Relay runs two listeners: a **data plane** that accepts your inference requests

## 星数曲线

```mermaid
xychart-beta
    title "wyolet/relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dfd94fb2d88f` · [字段定义](../../DATASET.md)*
