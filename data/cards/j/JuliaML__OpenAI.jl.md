# JuliaML/OpenAI.jl

⭐ 119 · Julia · MIT · 推送 2026-06-06 · [GitHub](https://github.com/JuliaML/OpenAI.jl) · [官网](https://juliaml.github.io/OpenAI.jl/dev/) · 组织维护

**社区维护的 Julia 语言 OpenAI API 封装库**

为 Julia 开发者提供 OpenAI API 的非官方封装：包含 create_chat 等便捷函数、基于上游 OpenAI OpenAPI 规范生成的类型化客户端 OpenAIClient，以及通过 StreamCallbacks.jl 实现的流式响应（可输出到任意 IO、捕获分块、自定义回调）。支持通过 OpenAIProvider 结构覆盖默认参数以接入符合 OpenAI 接口的本地 LLM 或第三方服务。API key 建议以环境变量方式设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖完整 OpenAPI 规范的生成客户端（类型化请求/响应模型）
- 基于 StreamCallbacks.jl 的流式响应与自定义回调
- OpenAIProvider 可覆盖参数以接入本地 LLM 或兼容 OpenAI 接口的第三方服务

## 适用场景

- 在 Julia 项目中调用 OpenAI 的对话、模型等 API
- 接入符合 OpenAI 接口规范的本地 LLM 或第三方服务
- 以流式方式处理 LLM 响应并自定义分块处理

## 场景标签

 · 领域:LLM 基础设施/语言绑定

## 证据(README 行号)

> L8: Provides a community maintained Julia wrapper to the OpenAI API.
> L96: The package also ships a generated client in `OpenAI.OpenAIClient`, built from

## 星数曲线

```mermaid
xychart-beta
    title "JuliaML/OpenAI.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-26 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `73bdf5c9d131` · [字段定义](../../DATASET.md)*
