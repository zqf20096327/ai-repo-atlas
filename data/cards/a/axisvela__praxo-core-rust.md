# axisvela/praxo-core-rust

⭐ 4 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/axisvela/praxo-core-rust) · [官网](https://axisvela.github.io/praxo-core/languages/rust/) · 组织维护

**可嵌入的 Rust AI agent 框架：提供 agent 循环、工具调用与策略控制**

PRAXO-CORE 的原生 Rust 实现，以 crate 形式发布于 crates.io，进程内运行、不依赖托管服务。核心包括带工具注册与分发的 agent 循环、策略钩子、类型化事件、内存、checkpoint、上下文预算、中间件、JSON Schema 校验与插件清单解析。原生支持 OpenAI 兼容模型，Anthropic 与 Gemini 模型通过传输接口由调用方提供，内置 MCP 客户端、子 agent 委托与检索器。README 声明其非托管模型、工作流引擎或安全控制器，不保证沙箱隔离与生产安全认证。

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

- agent 循环含工具注册分发、策略钩子、checkpoint 与中间件
- OpenAI 兼容模型原生支持；Anthropic/Gemini 经调用方传输接口
- 原生 MCP 客户端（stdio 与 Streamable HTTP）与子 agent 委托
- 结构化输出经 JSON Schema 校验，支持流式与 provider 回退

## 适用场景

- 在 Rust 应用中嵌入带策略控制的 agent 循环
- 需要人工审批（HITL）写入工具的 agent 流程
- 通过 MCP 客户端接入工具服务并做 tool calling
- 为 agent 添加 checkpoint 恢复会话与结构化输出校验

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed agent framework. This crate is its native Rust Core: an agent loop with to
> L22: - OpenAI-compatible model: native

## 星数曲线

```mermaid
xychart-beta
    title "axisvela/praxo-core-rust 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-23", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-19 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5b15b6d82188` · [字段定义](../../DATASET.md)*
