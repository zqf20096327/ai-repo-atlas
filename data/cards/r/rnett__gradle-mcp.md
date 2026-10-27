# rnett/gradle-mcp

⭐ 69 · Kotlin · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/rnett/gradle-mcp) · [官网](https://gradle-mcp.rnett.dev/) · 个人维护

**面向 AI agent 的 Gradle MCP 服务器：探索项目、跑构建、审依赖**

为 Gradle 提供的 Model Context Protocol 服务器，向 AI agent 提供一组构建工程工具：多项目结构映射、后台任务执行与输出捕获、过滤测试运行与日志栈迹访问、依赖与源码搜索、可交互 Kotlin REPL、Compose UI 组件渲染为图片、Gradle 文档索引检索、Develocity Build Scans 发布，以及引导 agent 完成 Gradle 工作流的内置 Agent Skills。使用紧凑数据格式以降低上下文占用。运行需 JDK 21 及以上，通过 JBang 启动，并以 MCP 服务器配置接入客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多项目结构、任务与属性的项目映射工具
- 后台运行构建、过滤测试套件并获取每用例日志与栈迹
- 持久化 Kotlin REPL 与 Compose UI 渲染为图片
- 内置 using-gradle、authoring-gradle-builds 等 5 个 Agent Skills

## 适用场景

- 让 AI agent 探索和诊断 Gradle 多模块项目
- 通过 agent 运行构建与测试并分析失败原因
- 审计依赖与查阅 Gradle 文档、DSL 参考

## 场景标签

 · 领域:开发工具/构建自动化

## 证据(README 行号)

> L9: A Model Context Protocol (MCP) server for Gradle. It gives AI agents the tools they need to explore project structur
> L15: * **Agent Skills**: Built-in workflows that guide AI agents through complex Gradle tasks.

## 星数曲线

```mermaid
xychart-beta
    title "rnett/gradle-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-27 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7f51fbb19316` · [字段定义](../../DATASET.md)*
