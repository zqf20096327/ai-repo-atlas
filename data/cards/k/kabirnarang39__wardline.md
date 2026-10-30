# kabirnarang39/wardline

⭐ 17 · Go · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/kabirnarang39/wardline) · [官网](https://kabirnarang39.github.io/wardline/) · 个人维护

**AI agent 的控制面代理：身份、策略、预算、审计与自动拦截**

单一 Go 二进制形式的自托管代理，部署在 AI agent 与 MCP 服务器、工具、gRPC 上游之间。每次调用经过身份核验、策略判定、预算检查、异常检测并记录审计。提供三种策略后端（YAML/OPA Rego/AWS Cedar），七种检测器学习 agent 正常行为并在异常时阻断。附带 JWT 凭证签发、OIDC/mTLS、RBAC/SCIM、租户隔离、审批工作流、Web 面板与 OpenTelemetry/Prometheus 观测。面向需要在 agent 生产环境实施治理与合规的运维和开发团队。默认身份与面板未鉴权，需开启 credential_issuance 与 rbac。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 七种无监督异常检测器，异常时可自动阻断 agent
- YAML/OPA/Cedar 三种策略后端，单二进制切换
- 结构化 JSON 审计与签名合规证据导出
- JWT 凭证签发、OIDC/mTLS-SPIFFE、RBAC/SCIM 与租户隔离

## 适用场景

- 在 agent 与 MCP 服务器之间强制执行策略与调用预算
- 检测被注入或越权的 agent 并自动阻断
- 满足 agent 调用链的审计与合规留痕要求

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L17: **Wardline** sits between your agents and everything they call: MCP servers, tools, gRPC upstreams. Every call goes
> L37: Anything that calls a tool (an AI agent, your CLI or IDE, an app) can only reach its upstreams by going through War
> L91: - Framework integrations: LangChain, LlamaIndex, OpenAI Agents SDK, CrewAI, raw MCP

## 星数曲线

```mermaid
xychart-beta
    title "kabirnarang39/wardline 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9c2a4d28d9e4` · [字段定义](../../DATASET.md)*
