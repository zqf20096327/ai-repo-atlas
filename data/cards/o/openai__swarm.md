# openai/swarm

⭐ 22,062 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/openai/swarm) · 组织维护

**面向开发者的轻量多 Agent 编排教学框架**

OpenAI 团队维护的实验性教育框架，用于探索多 Agent 编排模式。核心机制为 Agent（封装 instructions 与 functions）和 handoffs（通过函数返回值转移执行权）两个原语；client.run() 实现补全-工具执行-换 Agent-更新上下文的循环，函数自动转 JSON Schema，支持流式输出与 REPL 调试循环。完全基于 Chat Completions API，无状态运行，默认模型 gpt-4o。README 明确其已被 OpenAI Agents SDK 取代，生产场景建议迁移。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`declining` — 距上次 push 185.6 天,年发版 0,14 位贡献者
- 涨星:近 1 天 **+2**(自 20261016 起算)
- 安装:pypi 包 `git` 月下载无数据

## 能力要点

- Agent 与 handoffs 两个原语表达多 Agent 编排
- 函数自动转换为 Chat Completions tools 的 JSON Schema
- 基于 Chat Completions API 的无状态设计
- 提供 airline、support_bot、triage_agent 等 6 组示例

## 适用场景

- 学习多 Agent 编排与 handoff 模式
- 构建客户服务分流/多 Agent 协作原型
- 在本地 REPL 中流式调试 Agent 对话

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: > Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm. The Agents SDK fea
> L43: Swarm focuses on making agent **coordination** and **execution** lightweight, highly controllable, and easily testa
> L56: The Assistants API is a great option for developers looking for fully-hosted threads and built in memory management

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `d4d9ef450cc7` · [字段定义](../../DATASET.md)*
