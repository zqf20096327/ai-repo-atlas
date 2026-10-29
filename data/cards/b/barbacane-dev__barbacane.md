# barbacane-dev/barbacane

⭐ 29 · Rust · AGPL-3.0 · 推送 2026-10-13 · [GitHub](https://github.com/barbacane-dev/barbacane) · [官网](https://barbacane.dev/) · 组织维护

**以 OpenAPI/AsyncAPI 规范驱动的 Rust API 网关与 AI 网关**

用 Rust 编写的规范驱动型 API 网关：将 OpenAPI 3.x 或 AsyncAPI 3.x 规范编译为密封的 .bca 工件，由数据面执行路由、请求/响应校验、认证鉴权、限流、缓存、原生 ModSecurity/CRS 兼容 WAF 与可观测性。同一中间件链还路由 LLM 流量：ai-proxy 插件将 OpenAI/Anthropic/Ollama 统一到一个 OpenAI 兼容接口，并支持 prompt 守卫、token 限额、成本追踪等 AI 中间件；启用 MCP 后可将 API 操作暴露为类型化 MCP 工具。面向需要用既有规范管理 API 与 AI 流量的开发者与团队。通过源码克隆构建安装，提供 34 个官方 WASM 沙箱插件，标注为活跃开发中，AGPLv3 与商业双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAPI/AsyncAPI 规范即配置，编译为密封 .bca 工件，无独立网关 DSL
- ai-proxy 将 OpenAI/Anthropic/Ollama 统一为 OpenAI 兼容接口，含 glob 路由与 provider 回退
- 内置 ModSecurity/CRS 兼容 WAF（评分/阻断模式、按操作调优）
- 可将 API 操作暴露为 Model Context Protocol（MCP）工具，与 REST 流量共用同一认证限流校验链

## 适用场景

- 用已有的 OpenAPI 规范直接生成并运行生产 API 网关
- 将多家 LLM 提供商统一到一个 OpenAI 兼容入口并做限流与成本追踪
- 把现有 API 以 MCP 工具形式暴露给 AI agent 调用
- 在网关层内联部署 WAF 做 API 请求防护

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: Barbacane is a spec-driven API gateway built in Rust. Point it at an OpenAPI or AsyncAPI spec and it enforces it: r
> L25: - **AI and MCP on the same chain** — `ai-proxy` unifies OpenAI / Anthropic / Ollama behind one OpenAI-compatible su
> L121: |**AI gateway**|`ai-prompt-guard`, `ai-token-limit`, `ai-cost-tracker`, `ai-response-guard`|

## 星数曲线

```mermaid
xychart-beta
    title "barbacane-dev/barbacane 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9b625f2a1b49` · [字段定义](../../DATASET.md)*
