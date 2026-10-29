# allcolor/PawFlow-Agents

⭐ 26 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/allcolor/PawFlow-Agents) · [官网](https://pawflow.allcolor.org/) · 个人维护

**自托管 AI agent 运行时：在自有基础设施上运行持久化 agent 与工作流**

位于聊天 agent、本地工具与生产工作流之间的运行时层：服务端持久化保存会话、上下文、记忆、文件与流程，Relay 组件在目标机器旁执行文件系统、shell、浏览器、桌面与媒体工具。支持多 provider agent（OpenAI、Anthropic、OpenAI 兼容 API、原生 Codex/Claude Code/Gemini CLI 引擎、ACP/AG-UI 外部 agent）、委托视觉（文本模型配合独立视觉模型）、NiFi 风格确定性 Flow、技能学习循环与签名 .pfp 包生态。提供 Docker 安装器与源码运行两条路径，README 标注为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Relay 架构：文件/shell/浏览器/桌面/媒体工具在目标机器旁执行
- 多 provider agent：混用 API、原生 CLI 引擎与 ACP/AG-UI 外部 agent
- 委托视觉：文本推理模型搭配独立视觉模型描述屏幕并给出坐标
- NiFi 风格确定性 DAG Flow，带调度、检查点与审批

## 适用场景

- 在自有机器上运行可审计的 agentic coding 会话
- 把重复性工作固化为可调度、可检查点恢复的确定性工作流
- 为没有干净 API 的场景做浏览器与桌面自动化
- 通过 MCP/A2A/AG-UI 端点把 agent 暴露给外部客户端

## 场景标签

`GUI 自动化` `工作流自动化` `编码 Agent` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7:  Self-hosted agent runtime for real infrastructure.
> L29: PawFlow is the runtime layer between chat agents, local tools, and production workflows. The server keeps conversat
> L49: - **Multi-provider agents**: mix direct OpenAI Chat Completions or Responses,

## 星数曲线

```mermaid
xychart-beta
    title "allcolor/PawFlow-Agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `209aa64157fc` · [字段定义](../../DATASET.md)*
