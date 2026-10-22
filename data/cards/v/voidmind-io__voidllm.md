# voidmind-io/voidllm

⭐ 143 · Go · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/voidmind-io/voidllm) · [官网](https://voidllm.ai) · 组织维护

**自托管零知识 LLM 代理与 AI 网关**

用 Go 编写的单二进制自托管 LLM 代理，部署在应用与 LLM 提供商（OpenAI/Anthropic/Azure/Ollama/vLLM/自定义端点）之间，提供 OpenAI 兼容 API、多提供商路由、模型别名、多部署负载均衡与自动故障转移，以及组织/团队/用户/密钥四级 RBAC、速率限制、令牌预算与用量追踪。零知识架构：不存储、不记录任何请求或响应内容，仅持久化元数据。含 Web UI、MCP 网关（代理外部 MCP 服务器、WASM 沙箱 Code Mode）、Prometheus 指标，支持 SQLite/PostgreSQL。以 BSL 1.1 许可发布，另设 Pro/Enterprise 付费档（SSO、审计日志、OTel 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零知识架构：内容仅过内存，无内容日志选项
- 多提供商路由与负载均衡（round-robin/least-latency/weighted/priority）及自动故障转移
- Org>Team>User>Key 四级 RBAC、速率限制与令牌预算实时执行
- MCP 网关：代理外部 MCP 服务器，Code Mode 在 WASM 沙箱中编排多工具 JS

## 适用场景

- 团队统一管理多家 LLM 提供商的访问密钥与预算
- 合规要求下不可记录提示词/响应内容的企业内部 LLM 流量管理
- 多实例 vLLM/Ollama 部署的负载均衡与故障转移
- 通过模型别名在不动客户端代码的情况下切换提供商

## 场景标签

 · 领域:LLM 基础设施/API 网关

## 证据(README 行号)

> L15: VoidLLM is a self-hosted LLM proxy that sits between your applications and LLM providers - OpenAI, Anthropic, Azure
> L49: Your apps speak the OpenAI API to VoidLLM. It authenticates the key, applies RBAC, rate limits and budgets, resolve

## 星数曲线

```mermaid
xychart-beta
    title "voidmind-io/voidllm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 141 --> 144
    line [142, 143, 143]
```

2026-10-18 142 → 2026-10-22 143（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5952bbf7575b` · [字段定义](../../DATASET.md)*
