# 1amageek/SwiftAgent

⭐ 106 · Swift · 推送 2026-08-19 · [GitHub](https://github.com/1amageek/SwiftAgent) · 个人维护

**Swift 声明式 AI agent 框架：类型安全地组合 Steps 构建流水线**

基于 Apple FoundationModels 的 Swift 6.4 声明式 AI agent 框架，面向 iOS/macOS 开发者。核心机制：以 Step 为构建单元，在 body 中声明式组合（类似 SwiftUI），编译期检查输入输出类型；内置 Transform/Generate/Gate/Loop/Parallel/Race 等 12 种步骤。提供结构化输出（@Generable）、FIFO 会话管理、Memory/Relay 共享状态、EventBus 事件系统，以及 Claude Code 风格的 AgentTools 文件与 Web 工具集（含 Notebook/Dispatch 嵌套子代理）。限制：要求 iOS 26+/macOS 26+，@Generable 不支持 Dictionary 与 enum。经 OpenFoundationModels trait 可接入 OpenAI/Claude/Ollama 等替代模型提供方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Step 声明式组合，编译期类型检查的流水线（12 种内置步骤）
- Claude Code 风格 AgentTools：Read/Write/Edit/Grep/Bash/WebFetch 等 12 个工具
- Notebook/Dispatch 嵌套子代理（RLM 模式），子会话可递归分解任务
- 经 SPM Traits（OpenFoundationModels）支持 OpenAI/Claude/Ollama

## 适用场景

- 在 iOS/macOS 应用中构建类型安全的 AI agent 流水线
- 搭建带文件系统与 Web 工具的编码助手类 agent
- 通过 Dispatch 嵌套子代理处理超出上下文窗口的复杂任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: A type-safe, declarative framework for building AI agents in Swift, built on Apple FoundationModels.
> L18: - **Declarative Syntax** - Build agents by composing Steps in `body`, just like SwiftUI
> L20: - **Built on FoundationModels** - Native Apple AI integration

## 星数曲线

```mermaid
xychart-beta
    title "1amageek/SwiftAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-24 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `eef64e539b21` · [字段定义](../../DATASET.md)*
