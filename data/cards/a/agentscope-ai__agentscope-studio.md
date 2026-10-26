# agentscope-ai/agentscope-studio

⭐ 660 · TypeScript · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/agentscope-ai/agentscope-studio) · [官网](https://agentscope-ai.github.io/agentscope-studio/) · 组织维护

**面向 AgentScope 开发者的多智能体应用本地可视化工具**

为使用 AgentScope 框架的开发者提供的本地可视化工具箱：以 Projects/Runs 组织项目，提供聊天式界面实时查看智能体交互、基于 OpenTelemetry 的 LLM 调用与 token 用量追踪可视化、统计视角的智能体评测，以及内置 Copilot（Friday）开发助手。通过 npm 全局安装后运行 as_studio 启动，AgentScope 应用侧设置 studio_url 即可接入；也可源码运行或 Docker 部署。注意：AgentScope 2.0 已内置 Web UI，本工具已停止维护并将归档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenTelemetry 的 LLM 调用、token 用量与 agent 调用追踪可视化
- 聊天式界面实时查看智能体运行过程
- Projects/Runs 项目组织与统计视角的智能体评测
- 内置开发助手 Copilot（Friday），兼作二次开发 playground

## 适用场景

- 开发调试 AgentScope 多智能体应用时实时观察推理与工具调用
- 从统计角度评测智能体表现与 token 消耗
- 本地运行的可视化环境，无需上传数据到外部服务

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L55: AgentScope Studio is a powerful **local visualization toolkit** designed for developers working with AgentScope. It
> L61: - **Tracing**: OpenTelemetry-based trace visualization for LLM calls, token usage, and agent invocations

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/agentscope-studio 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-26"]
    y-axis "stars" 656 --> 661
    line [657, 658, 660, 660]
```

2026-10-18 657 → 2026-10-26 660（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `39896ca7385a` · [字段定义](../../DATASET.md)*
