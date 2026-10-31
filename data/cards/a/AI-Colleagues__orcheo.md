# AI-Colleagues/orcheo

⭐ 15 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/AI-Colleagues/orcheo) · [官网](https://orcheo.readthedocs.io/) · 组织维护

**面向 AI 编码 agent 的工作流编排全栈平台**

工作流编排平台，定位服务于 vibe coding：AI 编码 agent（Claude Code、Codex CLI、Cursor 等）可通过安装 Agent Skill 后代为完成环境搭建、工作流创建与部署。工作流以 Python 代码编写，基于 LangGraph，CLI 优先运行，UI（Studio）可选。安装依赖 Docker，提供 curl/PowerShell 脚本、SDK（uv）、PyPI 包与 GHCR 镜像多种途径。项目自声明处于 Beta，迭代中可能出现破坏性变更；对话式搜索示例需 OpenAI/DeepSeek 等 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 编码 agent 通过 Agent Skill 代为安装、建工作流并部署
- 工作流为 Python 代码，基于 LangGraph，无专有 DSL
- CLI 优先可无头运行，Studio UI 可选
- 提供对话式搜索示例（从基础 RAG 到生产级搜索）

## 适用场景

- 让 Claude Code/Cursor 等 agent 搭建和部署自动化工作流
- 用 Python 编排 RSS 监控、定时任务等自动化流程
- 构建和演示对话式搜索/RAG 应用

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Orcheo is a workflow orchestration platform designed for vibe coding — AI coding agents like Claude Code can start 
> L24: - **Python-native**: Workflows are Python code powered by LangGraph — no proprietary DSL to learn.
> L31: > Prerequisite: Docker Desktop/Engine must be installed to run the stack (`orcheo install --start-stack`).

## 星数曲线

```mermaid
xychart-beta
    title "AI-Colleagues/orcheo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ac1c34fb623e` · [字段定义](../../DATASET.md)*
