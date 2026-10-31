# gia-uh/argo

⭐ 24 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/gia-uh/argo) · [官网](https://uhgia.org/argo/) · 组织维护

**构建多智能体系统的轻量 Python 框架**

ARGO 是一个用于构建 LLM 多智能体系统的代码优先 Python 框架，提供 Agent、Skill、Tool、Context、Crew 等抽象，支持用 Python 代码或 YAML 声明式文件定义智能体工作流，可经 CLI 运行，或以 FastAPI 服务形式对外提供接口。多智能体协作通过带类型的消息板实现，智能体间松耦合，可替换为 Redis 等异步分布式消息板。还包含通过交互式反馈自动生成示例的训练模式（开发中）。框架自定位为概念验证，声明尚未达到生产可用状态。

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

- 代码优先与 YAML 声明式两种使用模式，附 CLI 运行方式
- 基于类型化消息板的多智能体协作（Crew/MessageBoard）
- argo serve 命令可为智能体生成 FastAPI 服务
- 训练模式通过用户反馈交互式生成改进示例（开发中）

## 适用场景

- 用 Python 代码灵活构建定制的智能体工作流
- 通过 YAML 声明式配置快速定义并运行智能体
- 搭建松耦合的多智能体协作系统处理可拆分任务

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **ARGO** - *Agent-based Reasoning, Governance, and Orchestration* - is a Python framework for building powerful, col
> L15: **ARGO** is a code-first framework, meaning you create agentic workflows by writing Python code. This approach offe
> L79: Building on top of the Agent abstraction, **ARGO** proposes a multi-agent architecture based on a typed message boa

## 星数曲线

```mermaid
xychart-beta
    title "gia-uh/argo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `753fda2cb5b8` · [字段定义](../../DATASET.md)*
