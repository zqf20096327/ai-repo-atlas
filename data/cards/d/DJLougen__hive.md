# DJLougen/hive

⭐ 40 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/DJLougen/hive) · [官网](https://github.com/DJLougen/hive#readme) · 个人维护

**AI agent 的 CPU 侧编排层：本地路由、上下文压缩与因果记忆**

面向拥有 agent 工具循环的开发者的编排层：将可观测状态下的机械性工具调用路由到 CPU 执行，仅在策略无法决策时升级给 LLM；压缩工具输出与日志以减少进入模型调用的上下文，并通过因果记忆复用先前的修复。提供 HiveStack API（route/compress/remember/recall/step）、MCP 接入文档与单副本 HTTP 服务部署。自带基准测试：相比 LLM-everything 基线，平均 LLM 调用从 7.31 降至 3.04，但解决率由 86% 降至 82%，文档明示结果不构成对用户负载的保证；当前为 v0.7.0 Beta 未发布，PyPI 未上架，需从源码安装。

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

- 基于可观测状态的规则路由，机械步骤在 CPU 执行、无法决策时升级 LLM
- 工具输出与日志的上下文压缩
- 因果记忆复用先前修复方案
- 提供 MCP 接入文档（Cursor / Claude Desktop / Codex）与基准复现脚本

## 适用场景

- 我想降低 agent 循环中重复工具调用的 LLM 成本
- 我想压缩进入模型调用的冗长工具输出
- 我想在 Cursor 或 Claude Desktop 中通过 MCP 使用这套路由与记忆能力

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Hive is an orchestration layer for AI agents: route mechanical tool calls locally, trim repetitive context, and reca
> L16: Your agent shouldn't need a paid reasoning call just to re-run tests after a patch. Hive can handle observable work

## 星数曲线

```mermaid
xychart-beta
    title "DJLougen/hive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e2079dff5f73` · [字段定义](../../DATASET.md)*
