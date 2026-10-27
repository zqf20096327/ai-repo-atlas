# mickyarun/bodhiorchard

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/mickyarun/bodhiorchard) · [官网](https://bodhiorchard.ai/) · 个人维护

**自托管 Jira/Scrum 替代品：十二个 AI agent 驱动软件开发全流程**

面向软件开发团队的自托管项目管理平台，以 Agent-Driven Development 取代 Scrum 流程：Slack 消息经 Triage Agent 转为需求，十二个专职 agent 负责起草规格、技术方案、测试计划、回顾与周期预测（AI-PERT + 蒙特卡洛模拟输出 P50/P70/P85 交付日期），每个阶段设人工审批关卡。推理可选 Claude Code、GitHub Copilot、Codex 或 Ollama 本地运行；附带 HR 假期/员工记录模块与 Slack 审批。技术栈为 FastAPI + Vue 3 + PostgreSQL/pgvector，支持 Docker 与 npx 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十二个专职 agent 覆盖 intake→spec→开发→测试→部署→回顾全生命周期
- AI-PERT + 10,000 次蒙特卡洛模拟输出分阶段置信区间交付日期
- tree-sitter 多仓库代码图谱索引与 blast-radius 查询
- HR/People 工作区含假期审批、员工记录 AES-256-GCM 加密

## 适用场景

- 软件团队用 agent 起草规格、测试计划并预测交付日期，替代 Scrum 仪式
- 私有部署项目管理工具，数据保留在本机并可选 Ollama 完全本地推理
- HR 与销售在同一平台管理假期、考勤与员工记录

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L19: **Bodhiorchard** replaces sprint, scrum, and Jira ceremony with **Agent-Driven Development (ADD)** — twelve special
> L128: Twelve agents, one flow, zero ceremony — the Agent-Driven Development lifecycle
> L146: |Agent|What it does|

## 星数曲线

```mermaid
xychart-beta
    title "mickyarun/bodhiorchard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5130ae09a4a3` · [字段定义](../../DATASET.md)*
