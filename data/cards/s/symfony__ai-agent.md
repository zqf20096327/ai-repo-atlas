# symfony/ai-agent

⭐ 35 · PHP · MIT · 推送 2026-10-26 · [GitHub](https://github.com/symfony/ai-agent) · [官网](https://symfony.com/packages/ai-agent) · 组织维护

**Symfony 生态的 PHP AI Agent 构建框架组件**

symfony/ai-agent 是 Symfony AI 系列中的 Agent 组件，基于 Platform 与 Store 组件构建，供开发者创建可与用户交互、执行任务、管理工作流的 AI agent。以 composer 包形式安装，另提供 13 个工具桥接包（Brave Search、MCP、Filesystem、Ollama Web Search、Wikipedia 等）按需扩展 agent 能力。README 声明该组件为实验性，不包含在 Symfony 向后兼容承诺内。仓库为只读子树拆分，问题与 PR 需提交至主仓库。

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

- 基于 Platform/Store 组件的 agent 构建框架
- 13 个可选工具桥接包（MCP、Brave Search、Filesystem 等）
- composer 一条命令安装

## 适用场景

- 在 PHP/Symfony 应用中构建可交互的 AI agent
- 为 agent 挂接搜索、文件系统、抓取等工具
- 通过 MCP 工具桥接入外部工具生态

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: The Agent component provides a framework for building AI agents that, sits on top of the Platform and Store componen
> L4: allowing you to create agents that can interact with users, perform tasks, and manage workflows.

## 星数曲线

```mermaid
xychart-beta
    title "symfony/ai-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fada4c700605` · [字段定义](../../DATASET.md)*
