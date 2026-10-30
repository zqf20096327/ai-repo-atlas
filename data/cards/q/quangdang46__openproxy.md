# quangdang46/openproxy

⭐ 29 · Rust · MIT · 推送 2026-10-23 · [GitHub](https://github.com/quangdang46/openproxy) · 个人维护

**本地单二进制 AI 代理路由：把编码工具接入 40+ 供应商并自动降级**

以单一二进制形式运行在 127.0.0.1:4623 的本地 AI 路由器，对外提供 OpenAI 兼容 API。Claude Code、Cursor、Codex、Copilot 等编码 CLI 将 base URL 指向它后，OpenProxy 把请求路由到已配置的供应商（OAuth 订阅 / API key / 免费层），在一个供应商限流或出错时按 combo 链自动降级，多账号轮询，并通过 RTK 压缩工具调用结果（典型节省 20-40% 输入 token）。内嵌本地仪表盘用于配置、配额追踪与请求日志，所有状态存于 ~/.openproxy/ 的 SQLite，无需云端组件。部分常量编译进二进制，修改需重新构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ 供应商接入，支持 OAuth 订阅 / API key / 免费层三类认证
- combo 有序模型链，限流或出错时自动降级，多账号轮询
- RTK 压缩工具调用结果，典型减少 20-40% 输入 token
- 面向 AI agent 的无人值守安装与 --robot JSON 输出、声明式 provider apply

## 适用场景

- 让 Claude Code / Cursor / Codex 等编码工具共用一套本地路由与多供应商降级链
- 先用完订阅配额，再降级到付费或免费供应商
- 通过本地仪表盘管理多账号配额与请求日志

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Single-binary AI router for AI coding tools.**
> L41: OpenProxy runs as one binary on `127.0.0.1:4623`. Point any tool that speaks the OpenAI Chat Completions API at it 
> L43: - routes the request to a provider you've configured (OAuth, API key, or free)

## 星数曲线

```mermaid
xychart-beta
    title "quangdang46/openproxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-30 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `2e845c386284` · [字段定义](../../DATASET.md)*
