# aayushgames19-hash/claude-gateway-manager

⭐ 118 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/aayushgames19-hash/claude-gateway-manager) · 个人维护 · 中文 README

**Anthropic Messages API 的多账号代理网关：统一接入与负载调度**

OpusFlow 是一个包裹 Anthropic Messages API 的代理/编排层：接收标准 Anthropic Messages API 请求格式（客户端仅改 base URL），在多个授权 Anthropic 账号池间按成本、剩余额度、历史错误率与时延做加权路由，支持按团队/项目/模型的 token 预算上限、限流时的账号回退（声称 200ms 内）、Stripe 计费、Slack/email 告警与实时多语言仪表盘。配置采用单一 YAML 文件；提供从 Tenbin 等代理导入配置的工具。README 声明不绕过限额、与 Anthropic 无隶属关系，MIT 许可。安装仅给出'Download'占位，无具体命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标准 Anthropic Messages API 格式兼容，客户端只需改 base URL
- 多账号池管理：加权路由、健康检查、限流时自动回退
- 按团队/项目/模型设置 token 预算硬/软上限
- Stripe 计费、实时仪表盘与多语言界面（中/英/日/韩）

## 适用场景

- 团队统一管理多个 Anthropic API key 的用量与预算
- 按任务成本把简单请求路由到 Haiku、复杂任务路由到 Opus
- 对 Anthropic API 消费做监控、告警与审计

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: OpusFlow was conceived to solve this by wrapping the Anthropic Messages API in a **unified, policy-driven gateway**
> L43: 1. **Ingress Layer** – Accepts standard Anthropic Messages API format. No client-side changes needed.
> L122: The OpusFlow endpoint is fully compatible with the Anthropic Messages API specification. Any existing client libra

## 星数曲线

```mermaid
xychart-beta
    title "aayushgames19-hash/claude-gateway-manager 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 117 --> 120
    line [118, 119, 118]
```

2026-10-18 118 → 2026-10-28 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8d9c508a624e` · [字段定义](../../DATASET.md)*
