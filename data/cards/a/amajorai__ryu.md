# amajorai/ryu

⭐ 42 · HTML · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/amajorai/ryu) · [官网](https://ryuhq.com) · 组织维护

**自托管 agent 运行时与编排基础设施，可接入现成 agent**

开源 core 的 agentic 基础设施：仓库含 Core、Gateway、CLI、Desktop、Island 与自托管文件，支持接入 Claude Code、Codex、OpenClaw 等现有 agent 或 harness，BYO 模型与 provider。提供插件/技能/集成目录、多 agent 协调、持久化工作流、审批与审计、沙箱执行、后台调度，可将 agent 发布为 app 或通过 CLI/渠道交付。可本地或自有服务器运行，无需 Ryu 账户。许可混合：Core/SDK Apache-2.0，Gateway AGPL-3.0，Desktop 等 source-available 商业许可；项目声明 pre-1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 接入现有 agent/harness（Claude Code、Codex、OpenClaw 等）而非从零构建
- 含 Core、Gateway、CLI、Desktop 与自托管文件，可自有基础设施运行
- 多 agent 协调、持久化工作流、审批/审计、沙箱执行、插件与 MCP 支持
- 以对照表形式与 DeepSeek Harness、LangChain、Grok Bot 等产品比较产品能力面

## 适用场景

- 在自有服务器上运行和编排多个现成 coding agent
- 通过插件扩展 agent 能力并把 agent 打包成应用
- 对 agent 运行做监控、审批与访问控制

## 场景标签

`Agent 框架` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L25: Build with SDKs, Core, Gateway, apps, plugins, and APIs. Run Ryu locally, on your own server, or in
> L28: This repository contains Core, Gateway, CLI, Desktop, Island, shared runtime packages, and

## 星数曲线

```mermaid
xychart-beta
    title "amajorai/ryu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-25 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8c44adebe3be` · [字段定义](../../DATASET.md)*
