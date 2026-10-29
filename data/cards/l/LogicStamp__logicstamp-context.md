# LogicStamp/logicstamp-context

⭐ 85 · TypeScript · MIT · 推送 2026-04-26 · [GitHub](https://github.com/LogicStamp/logicstamp-context) · [官网](https://logicstamp.dev) · 组织维护

**将 TypeScript 代码库编译为确定性架构契约的 CLI，供 AI 编码工具消费**

面向使用 AI 编码助手的 TypeScript 开发者的 CLI 工具：基于 ts-morph/TypeScript 编译器 API 扫描 .ts/.tsx 源码，提取组件 props、hooks、路由等契约并生成依赖图，按目录输出 context.json 与索引 context_main.json，作为 AI 助手的结构化上下文来源。支持 watch 模式、严格模式下的破坏性变更实时检测、git 基线比较、密钥自动扫描与脱敏；仅做分析，不改写源码。通过 logicstamp-mcp 服务器接入 Claude、Cursor 等 MCP 兼容助手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 确定性、可 diff 的架构契约与依赖图（同一代码产生同一输出）
- strict watch 模式实时检测 props/事件/函数移除等破坏性变更
- 支持 git 基线比较（分支/HEAD/tag）
- 自动密钥扫描与脱敏（输出 PRIVATE_DATA 占位）

## 适用场景

- 为 Claude/Cursor 等 AI 编码助手提供结构化项目上下文
- 在 CI 或开发过程中检测接口级破坏性变更
- 审阅提交前生成并核对架构契约差异

## 场景标签

 · 领域:开发者工具/代码分析

## 证据(README 行号)

> L11: LogicStamp Context is a CLI that compiles TypeScript codebases into deterministic, diffable architectural contracts
> L14: Use with logicstamp-mcp to feed structured context into **Claude**, **Cursor**, and other MCP-compatible assistants
> L129: **Under the hood:** the TypeScript compiler API (via ts-morph). **Analysis-only** - it describes your codebase and

## 星数曲线

```mermaid
xychart-beta
    title "LogicStamp/logicstamp-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-29 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b31492dfa043` · [字段定义](../../DATASET.md)*
