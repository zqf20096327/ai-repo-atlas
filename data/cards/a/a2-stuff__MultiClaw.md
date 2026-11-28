# a2-stuff/MultiClaw

⭐ 10 · TypeScript · 推送 2026-04-01 · [GitHub](https://github.com/a2-stuff/MultiClaw) · 组织维护

**自托管的多 AI agent 集群管理平台：单面板调度与编排**

自托管平台，由 React 仪表盘连接一个或多个运行在本地或远程机器上的 Python agent，每个 agent 拥有独立的身份、技能、插件、cron 任务与配置。提供 @mention 任务派发（多 agent 并行执行并汇总结果）、技能市场（ClawHub/SkillSSH）、git 插件安装、多 agent 工作流 DAG 编排、agent 间任务委托、共享记忆库、实时健康监控与审计日志。支持 RBAC 三种角色与 JWT/HMAC 认证，通过 install.sh 交互式向导安装，可注册为 systemd 服务，另提供 CLI 与终端 TUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @mention 派发：无 agent 标签时仪表盘直接回答，2+ 个 agent 并行执行并生成汇总
- 技能市场与 git 插件安装，按 agent 部署
- 工作流构建器将 agent 串成序列/DAG，支持 agent 间任务委托
- 共享记忆库与跨 fleet 配置/密钥同步

## 适用场景

- 在一台面板上统一管理分布在多台机器上的 AI agent
- 并行派发任务给多个 agent 并自动汇总结果
- 为团队提供带角色权限和审计日志的 agent 运维平台

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L45: MultiClaw is a self-hosted platform for managing fleets of AI agents. A central React dashboard connects to one or 
> L71: |**AI Providers**|Anthropic (Claude), OpenAI (GPT-4o), Google (Gemini), OpenRouter, DeepSeek|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `4c34f0ac5138` · [字段定义](../../DATASET.md)*
