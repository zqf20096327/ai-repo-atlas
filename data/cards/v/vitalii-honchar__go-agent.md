# vitalii-honchar/go-agent

⭐ 84 · Go · MIT · 推送 2026-05-09 · [GitHub](https://github.com/vitalii-honchar/go-agent) · [官网](https://pkg.go.dev/github.com/vitalii-honchar/go-agent) · 个人维护

**Go 语言 AI Agent 构建库：类型安全、可配工具与输出模式**

面向 Go 开发者的 AI agent 库：以泛型实现类型安全的 agent 定义，通过自然语言配置行为，支持自定义工具（含每工具调用上限）与 JSON schema 校验的结构化输出。LLM 层为抽象接口，当前支持 OpenAI（可扩展其他供应商）。仓库含增量计算与网站分析两个示例工程，提供 make 构建/测试/检查流程。限制：LLM 支持目前仅 OpenAI，运行示例需提供 OPENAI_API_KEY，开发环境要求 Go 1.24.4+。MIT 许可。

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

- Go 泛型实现类型安全的 agent 与输出 schema
- 自定义可扩展工具与每工具调用上限控制
- JSON schema 校验的结构化输出
- LLM 抽象层设计，当前支持 OpenAI、可扩展其他供应商

## 适用场景

- 用 Go 构建带结构化输出与工具调用的自动化 agent
- 为数据分析、网页抓取类应用嵌入 AI agent 能力
- 在需要编译期类型保障的 Go 项目中接入 LLM 工作流

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A powerful, production-ready Go library for building AI agents with configurable behavior, custom tools, and type-sa
> L25: - 🚀 **Multiple LLM Support** - Currently supports OpenAI (extensible to others)

## 星数曲线

```mermaid
xychart-beta
    title "vitalii-honchar/go-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 82 --> 85
    line [83, 84, 84]
```

2026-10-18 83 → 2026-10-29 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `84bf3917bd58` · [字段定义](../../DATASET.md)*
