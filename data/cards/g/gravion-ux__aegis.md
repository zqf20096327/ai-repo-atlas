# gravion-ux/aegis

⭐ 4 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/gravion-ux/aegis) · 个人维护

**面向开发者的安全优先多智能体系统核心库**

基于 Node.js 18+ 的多智能体系统核心，零运行时依赖。提供任务生命周期状态机、持久化记忆、提供商抽象、默认拒绝的工具注册表、任务与全局预算、专项智能体、编排器、协作式取消与检查点恢复等机制，安全边界均有对应测试覆盖。附 CLI 与 294 个自动化测试；HTTP 提供商目前仅经本地 mock 服务器验证，未接入付费模型。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 默认拒绝工具注册表：per-task 白名单、风险等级上限、审计事件
- 提供商抽象含离线提供商与通用 HTTP 提供商，付费模型需显式开启
- 检查点/恢复经真实进程边界测试，审计日志 append-only 且 HMAC 链接
- 零运行时依赖，294 个自动化测试

## 适用场景

- 搭建需要工具权限与预算管控的多智能体系统
- 以确定性离线提供商先测试编排逻辑再接入真实模型
- 对本地 Ollama/LM Studio 端点运行智能体任务并做检查点恢复

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Project AEGIS is a multi-agent AI system built around a rule that most
> L34: |**Orchestrator**|runs an agent under its declared limits, validates its output, retries only on a retryable provid


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `d02530565d4f` · [字段定义](../../DATASET.md)*
