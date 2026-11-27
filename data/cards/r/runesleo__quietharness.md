# runesleo/quietharness

⭐ 711 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/runesleo/quietharness) · [官网](https://leolabs.me) · 个人维护 · 中文 README

**给 AI 编程 Agent 加可靠性边界的一人公司工作系统**

面向用 AI 经营研究、内容、产品与商业化的独立构建者，提供可复用的工作流、模板与工具仓库。核心是 QuietHarness Core：一份 1,604 字节的共享行为边界（不装作看过、按风险验证、不可逆动作先确认），通过安装脚本写入 Claude Code、Codex 或 Cursor 三端配置，支持 dry-run、备份与回滚。附带 OPC First Workflow 离线实验、任务记录结构、单 Writer 写锁与实验性 Attention Inbox/Chat Export/Session Hooks 模块。只需 Git 与 Python 3 标准库，安装器不联网、不需要 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个共享 Core 适配 Claude Code、Codex、Cursor 三端，支持 dry-run、备份与回滚
- 安装器不联网、不登录账号、不需要 API key
- OPC First Workflow Preview 离线实验仅需 Python 3 标准库
- 任务记录含状态、工件、验证与 Owner 写回协议

## 适用场景

- 给正在使用的 AI 编程 Agent 加一层可回滚的工作边界
- 管理多 Agent 协作中的任务接力与验收
- 导出多家 AI 工具的本地聊天记录为统一 Markdown
- 搭建一人公司的业务线与任务结构

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L45: ## QuietHarness Core：可靠执行基础层
> L49: **只用 Claude Code、Codex 或 Cursor 中的一个就能获得同一组核心可靠性边界。** 多端兼容是以后更换工具时可以带走这些边界，不是安装门槛。
> L181: Claude Code、Codex 和 Cursor 都能获得同一组核心可靠性行为，但你只需要安装自己正在使用的客户端。Codex 直接读取 shared `AGENTS.md`，Claude Code 通过薄入口引用它；Cur


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `b794f26ddeb2` · [字段定义](../../DATASET.md)*
