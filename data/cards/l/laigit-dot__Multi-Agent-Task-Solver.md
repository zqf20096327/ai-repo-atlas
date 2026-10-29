# laigit-dot/Multi-Agent-Task-Solver

⭐ 20 · Python · 推送 2026-05-23 · [GitHub](https://github.com/laigit-dot/Multi-Agent-Task-Solver) · 个人维护

**多智能体协作编排系统：DAG 工作流调度专用 AI agent**

基于 Python/FastAPI 的多智能体编排平台：通过可配置工作流让多个专用 agent 协作，执行引擎提供 DAG 校验（拒绝环）、依赖感知的层级并行调度、带指数退避的重试、按 agent 的超时控制（asyncio.wait_for）与运行中取消。内置 data_fetcher/data_processor/calculator/chart_generator 四类工具型 agent，可通过注册 BaseTool 与子类化扩展。提供 FastAPI 服务与 CLI 两种入口，两者共用同一执行引擎。LLM 集成目前列于路线图，内置 agent 为数据处理工具型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作流 DAG 校验与依赖感知的分层并行调度
- 可配置重试、指数退避与按 agent 超时（asyncio.wait_for）
- 内置 4 类工具型 agent，工具注册表与 agent 基类可扩展
- FastAPI 服务与 CLI 共享同一执行引擎，47 个自动化测试

## 适用场景

- 编排多个专用 agent 按依赖关系并行执行数据处理流水线
- 通过 API 或 CLI 提交、查询、取消工作流执行
- 在此基础上扩展自定义 agent 与工具构建编排服务

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A production-ready orchestration platform that enables specialized AI agents to collaborate through configurable wor
> L27: |`src/core/`|Workflow DAG builder and async execution engine|
> L30: |`src/main.py`|CLI entry point for running servers, workflows, and registry inspection|

## 星数曲线

```mermaid
xychart-beta
    title "laigit-dot/Multi-Agent-Task-Solver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `01a4ff5d6286` · [字段定义](../../DATASET.md)*
