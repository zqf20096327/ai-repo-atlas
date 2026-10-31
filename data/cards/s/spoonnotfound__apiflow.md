# spoonnotfound/apiflow

⭐ 20 · TypeScript · MIT · 推送 2025-12-09 · [GitHub](https://github.com/spoonnotfound/apiflow) · 个人维护 · 中文 README

**桌面级多上游 AI API 代理与路由控制台**

基于 Tauri + React 的桌面应用，后端用 Axum/Reqwest 做 HTTP 转发：按 Base Path 管理服务并映射到多个 LLM/AI 提供商上游，支持 SSE 流式透传、失败自动重试与按优先级切换、请求级日志审计（方法/路径/状态码/耗时/请求头），并可配置 HTTP/HTTPS/SOCKS 出口代理。面向需要集中管理多家 AI API 的开发者，从 GitHub Releases 获取发行版，源码构建需 npm 与 Tauri 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多服务/多提供商路由，按优先级自动切换与重试
- SSE/流式响应透传
- 请求级审计：方法、路径、上游 URL、状态码、耗时、请求头
- 支持 HTTP/HTTPS/SOCKS 出口代理与局域网地址共享

## 适用场景

- 统一管理多个 LLM 提供商的 API Key 并集中代理
- 应用调用 AI API 失败时自动重试并切换提供商
- 查看 AI API 请求的实时日志与耗时统计

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: ApiFlow 是一款桌面级多上游 API 代理与路由控制台，前端基于 Tauri + React，后端使用 Axum/Reqwest 进行 HTTP 转发。支持流式透传、请求级日志、自动切换与重试，适合集中管理 LLM/AI AP
> L21: - 多服务/多提供商路由：按 Base Path 管理服务，灵活映射到不同上游并可调整优先级。

## 星数曲线

```mermaid
xychart-beta
    title "spoonnotfound/apiflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `244a9bd5608e` · [字段定义](../../DATASET.md)*
