# yuyuan12138/Pi

⭐ 3 · TypeScript · 推送 2026-11-14 · [GitHub](https://github.com/yuyuan12138/Pi) · [官网](https://yuyuan12138.github.io/2026/11/09/pi-agent-architecture/) · 个人维护 · 中文 README

**个人 AI 工作舰队操作系统：一个路由会话调度数十个 AI 工作者**

PiAgents 是基于 Pi 框架的个人 AI 工作者协调系统：主路由会话负责理解需求、撰写任务简报、派发与验收，实际执行在干净上下文的子代理中进行。机制包括 subagent_spawn/fork 派发通道、固定验收测试上的 Best-of-N 并行候选、文件系统级结果核验、四层带人审门控的记忆库（SQLite FTS5 全文检索，无向量库）、九种角色模板与带人工门控的自我改进循环。配套 Mission Control Web UI（pi-web-bridge）提供实时子代理面板。验证运行于 pi 1.3.0，不绑定该版本；所有规则与角色简报均为仓库内纯文本，无云依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 路由会话派发数十个 AI 工作者，执行在干净上下文子代理中完成
- Best-of-N 并行候选（N=3，难任务至 5）在同一固定验收测试上隔离运行
- 四层记忆体系（会话观察/日志/提炼概念/来源 wiki）+ SQLite FTS5 检索，写入门控需用户批准
- pi-web-bridge Web 任务控制台（127.0.0.1:7788）含实时子代理面板

## 适用场景

- 从单一会话将任务并行派发给多个 AI 子代理并逐一验收
- 维护跨项目、需人工审批的沉淀知识库与经验记录
- 需要审计追踪的多代理协调开发工作流

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: PiAgents is a personal operating system for coordinating dozens of AI workers from one router conversation. The rou
> L83: |`packages/pi-web-bridge/`|Web mission control (127.0.0.1:7788) for the running session — coordinator conversation,
> L98: One npm package plus eight locally vendored/local extensions (loaded directly from `packages/` so the running Pi al


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `d1192505031e` · [字段定义](../../DATASET.md)*
