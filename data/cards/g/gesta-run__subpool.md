# gesta-run/subpool

⭐ 116 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/gesta-run/subpool) · 组织维护 · 中文 README

**面向团队的自托管 AI 订阅额度池化与治理网关**

用 Go 编写、内嵌 React 控制台并以 PostgreSQL 持久化的自托管控制平面：管理员将已授权的订阅与 API 账号（Codex、GitHub Copilot、Google Antigravity、OpenAI 兼容账号、百炼 Token Plan 等）汇入池，分发员工级密钥，监控剩余额度与账号健康度，并对外暴露 OpenAI 兼容的 Responses 与 Chat Completions API。优先消耗订阅额度并回落到付费 API，上游凭据加密且不存储对话内容。部署需 Docker Engine 与 Docker Compose，通过 Docker Compose 拉取已发布镜像运行。限制：不覆盖 Coding Plan 等部分额度类型，Google Antigravity 需自备 OAuth 客户端凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 订阅与 API 容量汇入一个受管端点，暴露 OpenAI 兼容 API
- 员工级密钥分配，支持限速、过期与独立吊销
- 优先订阅容量、回落付费 API，按 key 跟踪 token 遥测
- 上游凭据加密，不持久化提示词、响应或源码

## 适用场景

- 团队共享 AI 订阅额度并按员工分配密钥
- 统一审计各账号的剩余额度与使用情况
- 让 Codex 等客户端经统一端点路由请求

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: Subpool is a self-hosted control plane for allocating, governing, and auditing AI subscription capacity across team
> L25: - Expose OpenAI-compatible Responses and Chat Completions APIs.
> L35: Subpool is a single Go service with an embedded React console and PostgreSQL persistence.

## 星数曲线

```mermaid
xychart-beta
    title "gesta-run/subpool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-28 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `de16d7b50863` · [字段定义](../../DATASET.md)*
