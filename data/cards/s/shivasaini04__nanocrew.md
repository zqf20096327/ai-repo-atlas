# shivasaini04/nanocrew

⭐ 4 · TypeScript · MIT · 推送 2026-11-13 · [GitHub](https://github.com/shivasaini04/nanocrew) · [官网](https://github.com/shivasaini04/nanocrew#readme) · 个人维护

**自托管的多智能体运行平台：Docker 沙箱隔离、带审批**

自托管的开源平台，运行一组 AI agent：每个 agent 有独立身份、长期记忆、工具与调度，在专属 Docker 容器内执行（shell、文件、无头浏览器、Python REPL），agent 之间可移交任务与互借工具。敏感操作进入人工审批收件箱，支持 cron、webhook 与聊天触发。模型通过 LiteLLM 网关接入多家供应商并配额降级，内置 70+ 工具、约 200 个技能与 MCP 支持。当前为 v0.1 早期版本，README 提示可能有不兼容变更；编排器通过 Docker socket 控制 Docker 宿主机，需注意部署安全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每个 agent 运行在独立 Docker 容器沙箱内，不触及宿主机
- agent 间任务移交、互借工具与协作关系图谱
- LiteLLM 网关接入多家模型供应商，支持配额降级与每日消费上限
- 70+ 内置工具、约 200 个 markdown 技能、MCP 外部工具支持

## 适用场景

- 自托管一套可调度的多 agent 团队处理日常任务
- 对发邮件等敏感操作保留人工审批环节
- 用自己的 API key 统一接入多家模型并控制开销

## 场景标签

`多智能体` `Agent 记忆` `模型网关` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: An open-source platform for running a crew of AI agents. Each agent has its own identity, memory, tools and
> L32: - **Bring your own models.** A LiteLLM gateway sits in front of Anthropic, OpenAI-compatible providers, DeepSeek,
> L41:  Dashboard (React) ──► Orchestrator (Node/TypeScript, SQLite) ──► LiteLLM gateway ──► model providers

## 星数曲线

```mermaid
xychart-beta
    title "shivasaini04/nanocrew 星数(近 3 点)"
    x-axis ["2026-11-01", "2026-11-08", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-01 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `1c547b2e1ad7` · [字段定义](../../DATASET.md)*
