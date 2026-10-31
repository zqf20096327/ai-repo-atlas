# Proact0/act-operator

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Proact0/act-operator) · [官网](https://www.proact0.org/) · 组织维护 · 中文 README

**为 AI 编码代理生成并管理 LangGraph 项目脚手架的开发工具**

面向用 AI 编码代理（如 Claude Code）开发 LangGraph 1.0+ 应用的 Python CLI 工具。通过 act new 命令生成含 CI、基类、测试结构的 monorepo 项目骨架，并提供三层机制：脚手架、可执行 SSOT（50+ LangGraph 参考 pattern 的 Agent Skills、draw.io 架构图 Kit）、以及跨会话维护的 CLAUDE.md 规范反馈环。Skills 目录默认适配 Claude Code 命名，需为 Cursor 等工具改名后使用。要求 Python 3.11+，通过 uvx 运行。

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

- act new 生成含 CI/基类/测试结构的 LangGraph 项目骨架
- 50+ LangGraph pattern 的 Agent Skills 供代理运行时读取
- architecting-act 生成 CLAUDE.md 作为跨会话持续规范
- drawkit.xml 提供 draw.io 预定义架构组件

## 适用场景

- 团队用 AI 编码代理搭建 LangGraph agent 项目并保持代码风格一致
- 让新会话的代理接续上一次的架构设计继续开发
- 为 LangGraph 项目生成架构图与持久规范文档

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L21: **A production-grade harness for controlling LangGraph 1.0+ project structure with AI agents.** Designed for real p
> L61: |**Executable SSOT**|Knowledge encoded as living files that agents and humans read at runtime|Act Template (project
> L129: Skills encode LangGraph knowledge as files that agents read directly. Instead of you telling the agent what patter

## 星数曲线

```mermaid
xychart-beta
    title "Proact0/act-operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `78cd81b94f70` · [字段定义](../../DATASET.md)*
