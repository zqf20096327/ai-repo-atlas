# Nexus-Router/nexus

⭐ 436 · Rust · MPL-2.0 · 推送 2026-03-16 · [GitHub](https://github.com/Nexus-Router/nexus) · [官网](https://nexusrouter.com) · 组织维护

**统一接入层：聚合 MCP 服务器与多家 LLM 供应商并治理 AI 调用**

用 Rust 编写的自托管网关：将多个 MCP 服务器（STDIO/SSE/streamable HTTP）聚合到单一端点，并对 OpenAI、Anthropic、Google、AWS Bedrock 四家 LLM 供应商提供统一路由接口，支持工具调用。治理能力包括基于用户/组的访问控制、多级请求与 LLM token 限流（内存或 Redis 后端）、OAuth2/CORS/CSRF/TLS。通过自然语言模糊搜索跨工具检索。安装支持一键脚本、Docker 镜像或 cargo 源码编译，TOML 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器聚合（STDIO/SSE/streamable HTTP）经单一端点暴露
- 四家 LLM 供应商统一路由，支持工具调用与并行执行
- 多级限流：全局/按 IP/按服务器/按工具，LLM token 限流按滑动窗口计输入 token
- OAuth2 客户端识别、基于用户组的 MCP 访问控制

## 适用场景

- 把散落各处的 MCP 服务器和 LLM API 收敛为一个统一入口
- 按用户或用户组限制对特定工具/模型的访问与用量
- 对 LLM 调用做 token 级成本控制与限流

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Plug in all your MCP servers, APIs, and LLM providers. Route everything through a unified endpoint.
> L9: - **LLM Provider Routing**: Unified interface for OpenAI, Anthropic, Google, and AWS Bedrock LLM providers with full
> L364: Nexus provides a unified interface for multiple LLM providers, allowing you to route chat completions through vari

## 星数曲线

```mermaid
xychart-beta
    title "Nexus-Router/nexus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 435 --> 437
    line [436, 436]
```

2026-10-18 436 → 2026-10-31 436（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `dd6dc0e43bf0` · [字段定义](../../DATASET.md)*
