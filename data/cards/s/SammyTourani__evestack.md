# SammyTourani/evestack

⭐ 16 · JavaScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/SammyTourani/evestack) · [官网](https://evestack.vercel.app) · 个人维护

**本地自托管的 AI agent 运行栈：会话、沙箱、审批与仪表盘**

基于 Vercel 开源 agent 框架 eve 构建的自托管运行栈，以 npm 脚手架一条命令生成项目：Docker 运行的 Postgres 持久会话（含 pgvector 语义记忆）、Docker 代码沙箱、人工审批门控、持久 cron 调度，以及可驱动 agent 的 Web 仪表盘。通过 OpenTelemetry 提供每会话 trace、按 turn 计费与延迟监控，经 Composio 接入 1,000+ 工具集成，支持 Ollama 本地模型。要求 Node 24 与 Docker，Windows 未测试（建议 WSL2）。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Postgres 持久会话 + pgvector 语义记忆，无需独立向量服务
- 审批门控：风险工具调用暂停等待人工确认并留审计日志
- OpenTelemetry trace、p50-p99 延迟与按 turn 成本统计
- EVESTACK_PROVIDER=ollama 可整栈零成本本地运行

## 适用场景

- 在自己机器/VPS 上运行并观测 AI agent，数据不出内网
- 为 agent 的危险操作加入人工审批环节
- 把真实会话（尤其出错会话）转为 eval 用例

## 场景标签

`Agent 框架` `LLM 可观测性` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L88: Under the hood, evestack runs on eve, Vercel's open-source agent
> L89: framework. evestack is **not a fork** — it ships as an eve registry, so it adds to eve rather than
> L144: Node 24, Docker, and a model API key (or Ollama).

## 星数曲线

```mermaid
xychart-beta
    title "SammyTourani/evestack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3dd1dd2ebc0b` · [字段定义](../../DATASET.md)*
