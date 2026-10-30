# soapbucket/sbproxy

⭐ 53 · Rust · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/soapbucket/sbproxy) · [官网](https://sbproxy.dev) · 组织维护

**单二进制企业 AI 网关：统一管控 API、模型与 MCP 流量**

Rust 编写的单一二进制网关，将 HTTP API、AI 模型调用（70 个原生 provider、200+ 模型、一个 OpenAI 兼容端点）与 MCP/agent 工具调用纳入同一请求管线，使限流、护栏、预算与审计对三类流量一致生效。策略引擎含 CEL、Rego、Lua、JS 与沙箱 WebAssembly，进程内扩展无需 sidecar；提供哈希链 Ed25519 签名的防篡改审计日志、OWASP LLM Top 10 覆盖评级、按摘要锁定 MCP 工具契约、语义缓存与本地模型托管。面向企业运维与开发者，Apache-2.0 发布，Rust 1.95+ 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制统一 HTTP API / 70 provider 模型调用 / MCP 流量的策略管线
- 进程内五种策略引擎（CEL/Rego/Lua/JS/Wasm）扩展，无需 sidecar
- 哈希链 Ed25519 签名审计日志，`sbproxy audit verify` 可重验防篡改
- OWASP LLM Top 10 (2026) 覆盖评级与七种作用域的预算硬拒绝

## 适用场景

- 给企业内外的 LLM API 调用统一加护栏、预算与审计
- 在不自控上游的前提下安全暴露/联邦 MCP 工具
- 在同一网关内托管本地模型并复用密钥与用量账本
- 将既有 HTTP API 纳入统一策略与限流管理

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: sbproxy is a single Rust binary that puts one policy engine in front of three kinds of traffic: HTTP APIs, AI model
> L26: - **Serve models locally, on the same binary.** `sbproxy run` starts a managed local model and hands it the same ke

## 星数曲线

```mermaid
xychart-beta
    title "soapbucket/sbproxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-30 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d52fa81d6eb8` · [字段定义](../../DATASET.md)*
