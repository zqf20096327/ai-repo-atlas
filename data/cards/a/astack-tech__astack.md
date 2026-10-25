# astack-tech/astack

⭐ 35 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/astack-tech/astack) · [官网](https://astack.tech) · 组织维护 · 中文 README

**TypeScript 可组合式 AI 应用构建框架，基于流式编程范式**

AStack 是用 TypeScript 实现的可组合 AI 应用框架，采用'一切皆组件'理念与 Flow-Based Programming（FBP）范式、monadic 函数组合及 ReactiveX Observable 流构建。组件通过端口连接组成流水线，支持无锁并发、三种执行模式与统一工具接口，可接入多种 LLM 提供商（示例含 Deepseek）。适用场景包括 Agent、内容生成流水线、数据处理与多模态应用。框架构建于 Hlang 之上并保持与其兼容；README 含与 Haystack 的功能对比表。要求 Node.js v18+，通过 git clone 源码安装，自述处于 Beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 组件化架构 + FBP/monadic 组合构建 AI 系统
- 基于 ReactiveX Observable 流与无锁并发
- Pipeline 三种执行模式与拓扑一次构建复用
- 统一工具接口接入多种 LLM 提供商

## 适用场景

- 构建带工具调用的多轮对话 Agent
- 搭建自动搜索、分析并生成研究报告的流水线
- 以数据流方式编排多组件 AI 工作流

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: AStack is a composable framework designed to simplify the development of AI applications through a "everything is a
> L31: - **Multi-Model Support**: Seamless integration with various LLM providers
> L68: - **AI Agents**: Build autonomous agents that can reason, plan, and execute tasks using tools

## 星数曲线

```mermaid
xychart-beta
    title "astack-tech/astack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d21bfd23c643` · [字段定义](../../DATASET.md)*
