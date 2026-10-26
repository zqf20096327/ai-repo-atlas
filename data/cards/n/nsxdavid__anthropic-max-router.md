# nsxdavid/anthropic-max-router

⭐ 64 · TypeScript · MIT · 推送 2025-12-21 · [GitHub](https://github.com/nsxdavid/anthropic-max-router) · 个人维护

**把 Claude MAX 订阅转为双格式 API 代理供任意 AI 工具调用**

面向持有 Anthropic Claude MAX 订阅（$100/$200 月付）的开发者：通过 OAuth PKCE 认证，在本地启动 HTTP 代理（默认 localhost:3000），同时暴露 Anthropic 原生 /v1/messages 与 OpenAI 兼容 /v1/chat/completions 两个端点，OpenAI 请求自动翻译为 Anthropic 格式并做模型名映射（gpt-4 等映射到 Claude）。附带交互式 CLI 用于测试 OAuth 流程、文档指南，支持 Bearer token 直通与令牌自动刷新。声明仅供教育研究用途、与 Anthropic 无关联；/v1/models 端点需单独的 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双端点：Anthropic 原生 /v1/messages + OpenAI 兼容 /v1/chat/completions（自动翻译）
- OpenAI 模型名模式匹配自动映射到 Claude 模型
- OAuth PKCE 认证与 8 小时 token 自动刷新
- Bearer token 直通：多用户可用各自 API key 共享一个路由器

## 适用场景

- 让基于 OpenAI SDK/LangChain 的现有工具零代码改用 MAX 订阅计费
- 同一本地地址同时服务 Anthropic 与 OpenAI 格式的两类工具
- 开发团队用各自 API key 共享同一路由实例

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Dual endpoints:** Native Anthropic API + OpenAI-compatible API (auto-translates to Anthropic)
> L43: A standalone HTTP proxy with **both Anthropic and OpenAI endpoints** that lets ANY AI tool use your MAX Plan subscr
> L162: A standalone HTTP proxy server with **dual API endpoints** (Anthropic + OpenAI) that lets **any AI tool or applica

## 星数曲线

```mermaid
xychart-beta
    title "nsxdavid/anthropic-max-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-26 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ba684b329fa2` · [字段定义](../../DATASET.md)*
