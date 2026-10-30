# canvascomputing/agentwerk

⭐ 28 · Rust · MIT · 推送 2026-10-26 · [GitHub](https://github.com/canvascomputing/agentwerk) · [官网](https://canvascomputing.org/) · 组织维护

**构建多 agent 协作 harness 的 Rust 极简 agentic loop 框架**

Rust 编写的 agentic loop 框架，面向需要构建 agent harness 的开发者。提供 Agent、Task、Event、Knowledge、Werk 等核心 API：通过标签路由任务、事件驱动多 agent 协调、共享知识页面、会话持久化与恢复，支持配置模型提供商与命令/文件/网页工具。README 以编码 harness、深度研究 harness 和 19 agent 模拟 F1 停站三个示例展示用法。另有 Python 绑定。自声明 beta，0.2.0 前 API 可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 标签路由任务 + 事件驱动的多 agent 协调（Werk 核心）
- 共享 Knowledge 页面与 AQL 查询任务/结果/事件
- 会话可保存到目录并恢复（./session）
- 提供 Python 绑定与多个示例（编码/深度研究/恶意软件扫描等）

## 适用场景

- 构建 planner+coder 协作的仓库代码修改 harness
- 搭建多 agent 网络研究并生成带引用报告的系统
- 需要事件驱动、可观测的多 agent 舰队协调场景

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A minimal agentic loop for building efficient harnesses.
> L383: |Collaboration|Pass work and results between agents.|

## 星数曲线

```mermaid
xychart-beta
    title "canvascomputing/agentwerk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6bf8d9e2a101` · [字段定义](../../DATASET.md)*
