# MacPaw/ComposablePipelines

⭐ 26 · Swift · Apache-2.0 · 推送 2026-09-21 · [GitHub](https://github.com/MacPaw/ComposablePipelines) · 组织维护

**Swift 声明式 AI 管道 DSL：编写、编译与执行中间表示框架**

MacPaw 开源的 Swift 6.1+ 包，将 AI 管道分为三层：result-builder 声明式前端、Codable AST 中间表示、可插拔 Executor 后端。前端管道经 lowering 生成 AST，编译器分析 @State 数据依赖并产出执行图，由 walker 解释执行，支持基于 epoch 的增量重执行、循环与分支等原生控制流。自带 MockExecutor 与 OpenAIChatExecutor（可连任意 OpenAI 兼容端点），并提供 cp-demo 三步管道示例与 cp-agent 工具调用编码代理示例。模型与工具步骤全部委托给用户实现的 Executor，运行于 macOS 14+/iOS 17+/Linux，依赖仅 Foundation 与 swift-syntax。本仓库为只读镜像，上游为闭源 Elix 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SwiftUI 风格 result-builder DSL，声明式编写 AI 管道
- Codable AST 作为中间表示与客户端/后端边界（线格式）
- 编译器从 @State 数据依赖推导执行图，walker 支持 epoch 增量重执行
- Executor 后端可插拔，内置 MockExecutor 与 OpenAIChatExecutor

## 适用场景

- 用声明式 DSL 构建含循环、分支与工具调用的 AI agent
- 在客户端生成管道 AST、发送到远端后端编译执行
- 接入本地模型或任意 OpenAI 兼容端点运行管道

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: **An intermediate representation and compiler for AI pipelines in Swift.**
> L79: - **Bring your own runtime.** The walker never runs a model itself; it calls an `Executor` you
> L81:  tests, and a Foundation-only `OpenAIChatExecutor` talks to any OpenAI-compatible endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "MacPaw/ComposablePipelines 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `55c79dcabf5b` · [字段定义](../../DATASET.md)*
