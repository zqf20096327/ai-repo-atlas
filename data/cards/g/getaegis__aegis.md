# getaegis/aegis

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/getaegis/aegis) · 组织维护

**面向 AI agent 的本地凭证隔离代理，agent 不接触真实密钥**

部署在 AI agent 与外部 API 之间的本地透明代理（Gate）：agent 请求经 localhost:3100 转发时由 Aegis 在网络边界注入凭证，agent 全程不看到、不存储、不传输真实密钥。配套能力包括域白名单防外传、请求体凭证模式扫描、全量审计日志、按 agent 发放一次性令牌与 RBAC、YAML 声明式策略、AES-256-GCM 加密保管库、Prometheus 指标与 Webhook 告警。同时作为原生 MCP server 提供 Claude Desktop、Cursor、VS Code、Cline、Windsurf 的配置生成，暴露三个工具。需 Node.js ≥ 20，Apache 2.0 开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网络边界透明注入凭证，agent 不接触真实密钥
- 域守卫 + 请求体凭证模式扫描 + 全量审计日志
- 原生 MCP server，提供 aegis_proxy_request 等三个工具
- AES-256-GCM 加密保管库、RBAC、Shamir 密钥分片、多保管库

## 适用场景

- 让 AI agent 安全调用 Slack/GitHub/Stripe 等 API 而不暴露真实密钥
- 防止被入侵或被注入的 agent 将凭证外发到未授权域名
- 审计每个 agent 对每个凭证的实际使用记录

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: Aegis is a local-first credential isolation proxy for AI agents. It sits between your agent and the APIs it calls —
> L49: Aegis is a first-class MCP server. Any MCP-compatible AI agent can use it natively — no HTTP calls needed.
> L107: |**MCP Server**|Native Model Context Protocol for Claude, Cursor, VS Code, Windsurf, Cline|

## 星数曲线

```mermaid
xychart-beta
    title "getaegis/aegis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a644d735a5ce` · [字段定义](../../DATASET.md)*
