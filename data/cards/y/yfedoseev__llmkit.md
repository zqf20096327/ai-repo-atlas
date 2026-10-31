# yfedoseev/llmkit

⭐ 13 · Rust · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/yfedoseev/llmkit) · 个人维护

**Rust 核心、三语言绑定的统一 LLM 客户端库**

以纯 Rust 为核心、提供 Rust/Python/Node.js 三种语言绑定的 LLM 客户端库，宣称接入 100+ 提供商、内置 11,000+ 模型注册表（含定价与上下文限制，无需外部 API 调用即可查询）。功能包括流式输出、工具调用、结构化输出、Prompt 缓存、Extended Thinking 统一 API，以及智能路由、熔断、限流、成本跟踪、护栏与 OpenTelemetry 观测等生产特性。支持本地运行时（Ollama、LM Studio、vLLM）与云端提供商。通过 cargo、pip、npm 安装，也可从源码构建；双许可 MIT/Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Rust 核心，Rust/Python/Node.js 三语言原生绑定
- 100+ 提供商统一 API，本地运行时含 Ollama/LM Studio/vLLM
- 11,000+ 模型注册表内置定价、上下文限制与能力信息
- 生产特性：智能路由、熔断、限流、成本跟踪、护栏、OpenTelemetry

## 适用场景

- 在 Rust/Python/Node.js 项目中用统一 API 接入多家 LLM 提供商
- 查询模型的定价与上下文限制信息用于选型
- 在生产服务中做 LLM 调用的限流、熔断与成本跟踪

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **The production-grade LLM client.** One API for 100+ providers. Pure Rust core with native bindings.
> L5: **11,000+ models** · **100+ providers** · **Rust | Python | Node.js**
> L115: |**Local**|Ollama, LM Studio, vLLM|

## 星数曲线

```mermaid
xychart-beta
    title "yfedoseev/llmkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fbc0a6b581f4` · [字段定义](../../DATASET.md)*
