# agentscope-ai-java/agentscope-java

⭐ 94 · Java · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/agentscope-ai-java/agentscope-java) · [官网](https://java.agentscope.io/) · 组织维护 · 中文 README

**构建分布式、生产级、长时运行 AI agent 的 Java 框架**

AgentScope Java 2.0 是面向企业的 agent 构建框架，提供 HarnessAgent 抽象：事件流（31 种类型事件）、三态权限系统（allow/approve/deny）、AOP 风格中间件、多 agent 编排（agent_spawn/agent_send）与分布式会话管理（Redis/MySQL/PostgreSQL/OSS/COS 状态持久化、跨副本恢复）。工具可运行于本地、Docker、Kubernetes 或 E2B 云沙箱。模型提供商以扩展模块形式接入（DashScope/OpenAI/Anthropic/Gemini/Ollama），环境变量自动读取 API key。要求 JDK 17+，Maven Central 发布，另提供 AgentScope Service 控制平面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HarnessAgent 提供 31 种类型事件的统一事件流与 HITL 权限门控
- 分布式会话与内存管理，支持跨副本会话恢复与零停机滚动部署
- 工具沙箱执行：本地子进程 / Docker / Kubernetes / E2B 云沙箱
- 成功模式自动保存为 Markdown 技能并按需加载

## 适用场景

- 用 Java 构建可在生产环境运行的分布式多 agent 系统
- 对敏感工具调用引入人工审批的人机协作流程
- 长时运行任务的分层记忆与上下文自动压缩

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L48: AgentScope Java 2.0 is a production-ready framework for building distributed, enterprise-grade agents, providing es
> L50: - **Event System** → A unified event stream with 31 typed events for real-time frontend rendering and human-in-the-

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai-java/agentscope-java 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-23 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `379edfa7d4e5` · [字段定义](../../DATASET.md)*
