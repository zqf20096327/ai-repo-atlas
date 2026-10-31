# Ahoo-Wang/fetcher

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/Ahoo-Wang/fetcher) · [官网](https://fetcher.ahoo.me/) · 个人维护 · 中文 README

**面向 TS 开发者的 HTTP 客户端生态，含 OpenAI 流式支持**

基于原生 fetch API 构建的 TypeScript HTTP 客户端生态系统，以 Axios 风格提供类型化请求、拦截器、超时与流式处理。按需组合子包：装饰器声明式服务、事件总线、SSE、OpenAI Chat Completions 封装、OpenAPI 类型生成、React hooks、存储与 CoSec 认证。要求 Node.js 18.20.8+。与 Wow 框架耦合的包已迁移至 Wow 仓库并随其版本化，fetcher 5.x 分支继续接收修复。

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

- 类型化请求、拦截器、超时与流式处理
- fetcher-openai 子包封装 OpenAI Chat Completions
- SSE（fetcher-eventstream）与 React hooks 子包
- 按需选包的模块化生态，包体积小

## 适用场景

- 在 TS 项目中做带拦截器和类型的 HTTP 请求
- 接入 OpenAI API 并处理流式响应
- 为 React 应用提供请求 hooks 与 SSE 支持

## 场景标签

 · 领域:Web 开发/HTTP 客户端库

## 证据(README 行号)

> L17: Fetcher is a TypeScript HTTP-client ecosystem built around the platform
> L47: |OpenAI Chat Completions|`@ahoo-wang/fetcher-openai`|

## 星数曲线

```mermaid
xychart-beta
    title "Ahoo-Wang/fetcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `030eae9c7a1e` · [字段定义](../../DATASET.md)*
