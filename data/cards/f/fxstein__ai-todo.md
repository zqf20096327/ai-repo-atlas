# fxstein/ai-todo

⭐ 16 · Shell · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/fxstein/ai-todo) · [官网](https://pypi.org/project/ai-todo/) · 个人维护

**给编程 AI agent 用的持久化 Git 版本化任务管理工具**

面向 Cursor、Claude、Copilot 等编程代理的任务管理系统，以 MCP 服务器形式集成：agent 通过自然语言指令创建、拆分、完成、归档任务，全部状态以标准 TODO.md 格式存储在仓库中，随 Git 版本控制，会话结束后任务不丢失。本地运行，无 API 调用、认证或速率限制。提供 uvx 零安装按需运行与 uv tool/pipx 全局安装两种方式，也可作为 CLI 使用，需 Python 3.10+。

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

- 任务以 TODO.md 存储于 Git 仓库，跨会话持久
- MCP 集成，agent 可直接读写任务
- 本地即时运行，无 API 调用与速率限制
- 支持子任务层级、标签组织、归档与 GitHub Issue 引用

## 适用场景

- 让编程 agent 在长期任务间保持待办状态的连续记录
- 用自然语言让 agent 创建、拆分、勾选项目任务
- 在 Git 历史中追溯任务与代码的对应关系

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **AI-native task management for coding agents**
> L30: - **AI-Native** — MCP integration for direct agent interaction

## 星数曲线

```mermaid
xychart-beta
    title "fxstein/ai-todo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f62fb3b5a997` · [字段定义](../../DATASET.md)*
