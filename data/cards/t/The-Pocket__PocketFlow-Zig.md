# The-Pocket/PocketFlow-Zig

⭐ 16 · Zig · MIT · 推送 2026-01-26 · [GitHub](https://github.com/The-Pocket/PocketFlow-Zig) · 组织维护

**用 Zig 实现的极简 LLM 工作流框架，供开发者构建 Agent 流程**

Python 版 PocketFlow 的 Zig 移植：以节点图组织 LLM 工作流，节点经 prep/exec/post 三阶段执行，通过 action 返回值路由到后继节点；核心组件为类型擦除的 Node 接口（vtable 实现）、Flow 执行引擎与线程安全的共享 Context（内置互斥锁）。核心零外部依赖，附带可选的 Ollama 客户端用于本地 LLM 推理，示例含基于 Ollama 的多节点文档生成。要求 Zig 0.15.0+，以 zig fetch/build.zig.zon 方式集成，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 节点图 + action 路由的流程执行引擎
- vtable 实现类型擦除节点接口，核心零依赖
- 线程安全共享 Context（内置互斥锁）
- 内置可选 Ollama 客户端用于本地 LLM 推理

## 适用场景

- 在 Zig 项目中以节点流方式编排 LLM 工作流
- 构建需要分支路由与共享状态的多步 Agent 流程
- 配合本地 Ollama 做离线 LLM 推理流水线

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Zig implementation of PocketFlow, a minimalist flow-based programming framework for building LLM-powered workflows
> L18: - **Flow execution engine**: Automatic traversal and execution of node graphs

## 星数曲线

```mermaid
xychart-beta
    title "The-Pocket/PocketFlow-Zig 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1cd39e2f893c` · [字段定义](../../DATASET.md)*
