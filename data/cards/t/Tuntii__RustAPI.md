# Tuntii/RustAPI

⭐ 64 · Rust · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/Tuntii/RustAPI) · [官网](https://rustapi.cloud) · 组织维护

**Rust Web 框架：编译期路由、自动 OpenAPI、内建 MCP/LLM 支持**

基于 hyper 1.x 与 tokio 的 Rust Web 框架，面向希望少写样板代码又保留性能控制的 API 开发者。通过过程宏在编译期注册路由并生成 OpenAPI 3.1 规范（Swagger UI 位于 /docs），提供 JWT、CORS、限流、熔断、重试、请求重放调试、HTTP/3、后台任务队列等内建能力。AI 相关部分包括 TOON 紧凑序列化格式、将端点自动暴露为 MCP 工具（支持 Claude Desktop/Cursor stdio 集成）以及 cargo rustapi CLI 的脚手架与云端部署。以 crates.io 包形式分发，门面架构隔离内部 crate 变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 过程宏编译期注册路由，自动生成 OpenAPI 3.1 并内建 Swagger UI
- 每个端点自动成为 MCP 工具，支持 stdio 集成 Claude Desktop/Cursor
- TOON 序列化格式降低 LLM 响应 token 数量并带观测头
- 内建熔断/重试/限流/请求重放/HTTP3/后台任务等生产中间件

## 适用场景

- 用 Rust 快速搭建带自动 OpenAPI 文档的 REST API
- 将现有 API 一键转为 AI agent 可调用的 MCP 工具
- 为 LLM 应用后端提供 token 高效的响应格式与服务

## 场景标签

 · 领域:Web 开发框架/后端基础设施

## 证据(README 行号)

> L46: RustAPI is a Rust web framework built on **hyper 1.x** and **tokio**, designed for minimal boilerplate while retain
> L121: ### Native MCP (Model Context Protocol)

## 星数曲线

```mermaid
xychart-beta
    title "Tuntii/RustAPI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-25 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6e0c51184240` · [字段定义](../../DATASET.md)*
