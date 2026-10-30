# vincenzo-afk/NOVA-exe

⭐ 23 · TypeScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/vincenzo-afk/NOVA-exe) · 个人维护

**本地优先的桌面 AI agent 平台：带权限审批的自动化执行**

基于 TypeScript/Electron/React/SQLite 的 pnpm monorepo，提供桌面 AI agent 运行时：规划器、执行器、验证器、任务调度与工具注册，配 SQLite+Prisma 的分层记忆持久化、固定本体知识图谱、文件系统/剪贴板/通知/浏览器元数据/键鼠活动等 Windows 观察器（权限默认关闭），以及 workspace-code 受限脚本 CLI。LLM 侧提供 Groq OpenAI 兼容适配器，凭据经 vault 引用解析。默认测试无需 API key；仍处 0.1.0 活跃开发阶段，Windows 实机验证在无主机连接时推迟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Planner/executor/verifier 与任务调度、工具注册的 agent 运行时
- SQLite+Prisma 的工作区级记忆持久化与知识图谱浏览器
- 剪贴板/通知/浏览器元数据/键鼠等默认关闭的权限化观察器
- Groq OpenAI 兼容 provider 适配器（vault 引用凭据）

## 适用场景

- 在桌面本地运行带权限审批的自动化 agent 任务
- 跨设备分布式任务调度与同步
- 通过 Task Monitor 查看/重试/取消任务并审计执行

## 场景标签

`Agent 框架` `GUI 自动化` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A local-first desktop AI agent platform built for permissioned automation, durable memory, and auditable execution
> L17: Nova is a local-first desktop agent platform. Its runtime coordinates planning, permission checks, tool execution, 
> L25: - Planner, executor, verifier, task-manager, priority/concurrency task scheduler, tool-registry, deterministic mode

## 星数曲线

```mermaid
xychart-beta
    title "vincenzo-afk/NOVA-exe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `31ceb3a51771` · [字段定义](../../DATASET.md)*
