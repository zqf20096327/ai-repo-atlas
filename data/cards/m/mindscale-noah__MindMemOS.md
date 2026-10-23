# mindscale-noah/MindMemOS

⭐ 918 · Python · 推送 2026-10-19 · [GitHub](https://github.com/mindscale-noah/MindMemOS) · [官网](https://mindmemos.cn) · 组织维护 · 中文 README

**AI agent 长期记忆操作系统：跨 agent 持久记忆与技能蒸馏**

面向 AI agent 的记忆操作层（Memory OS）：以服务形式持久化用户画像、偏好、项目事实、工具经验与技能候选，让 OpenClaw、Claude Code、OpenHands 等 agent 共享与迁移同一份长期记忆。机制上通过 schema 学习、离线 dreaming 整合与交互反馈实现记忆自演化，可把经验记忆蒸馏为技能候选并回写执行结果。提供官方云服务与本地自托管两种部署，经 HTTP API、Python SDK/CLI 或 agent 插件访问；本地部署用 uv 管理依赖，需配置 chat/embed/rerank 三类模型路由，依赖 Qdrant、Neo4j、Kafka 等 Docker 组件栈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 agent 可移植记忆：用户画像、项目事实、技能候选作为可复用资产共享
- 记忆自演化：schema 学习、离线 dreaming 整合、交互反馈优化
- 经验记忆可蒸馏为技能候选，技能执行结果回流记忆系统
- 云/本地同一协议，支持 HTTP API、Python SDK/CLI、OpenClaw 与 DeepSeek Harness 插件

## 适用场景

- 让多个 agent 共享同一份用户与任务的长期记忆
- 业务应用通过 SDK 或 HTTP API 存取用户偏好与项目事实
- 从交互经验中自动积累并演化可复用技能

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L35:  Accurately remember user and task context and reuse it across agents; evolve memory through ongoing interactions, 
> L48: - **Portable across agents**: Persist user profiles, preferences, project facts, tool experience, and skill candida
> L57: MindMemOS offers **two deployment modes** (official cloud service, local self-hosting) and **three access methods**

## 星数曲线

```mermaid
xychart-beta
    title "mindscale-noah/MindMemOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 916 --> 919
    line [917, 918]
```

2026-10-18 917 → 2026-10-23 918（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c0f1cfb5b76f` · [字段定义](../../DATASET.md)*
