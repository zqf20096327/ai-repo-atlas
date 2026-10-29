# rretsiem/opencode-hive

⭐ 42 · Python · MIT · 推送 2026-07-30 · [GitHub](https://github.com/rretsiem/opencode-hive) · [官网](https://opencode.ai) · 个人维护

**OpenCode 的多 agent 架构模板：按成本路由模型并维护项目 wiki**

一套 OpenCode 配置模板：编排器将任务按领域分派给专职 specialist 子代理并行执行，按 SUB/MID/PREMIUM 成本层级为路由、分析、代码生成等角色分配不同模型，模型用占位符表示、不绑定特定提供商。内置 python-pro/go-pro 等 7 个全局子代理与前端/后端/数据库/DevOps 示例专家，7 个代码导航与检查工具（Python 3.10+，部分需 Ruff/pytest），以及符合 Open Knowledge Format v0.2 的代理维护项目 wiki。供已安装 OpenCode 并配置至少一个 LLM 提供商的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排器按任务领域并行分派给专职 specialist 子代理
- SUB/MID/PREMIUM 三层成本感知模型路由，占位符不绑定提供商
- 7 个代码导航/检查工具（skeleton/impact/seek/ghost/check 等）
- 符合 OKF v0.2 的代理维护项目 wiki（bootstrap/ingest/query/lint）

## 适用场景

- 在 OpenCode 中搭建多 agent 协作的开发工作流
- 按成本分层路由模型，避免高价模型处理轻量任务
- 让 AI 自动维护可溯源的项目知识库 wiki

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: A multi-agent architecture for OpenCode with cost-aware model routing, parallel specialist execution, and an agent-m
> L34: **Prerequisites**: OpenCode installed, at least one LLM provider configured.

## 星数曲线

```mermaid
xychart-beta
    title "rretsiem/opencode-hive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6921fd07325f` · [字段定义](../../DATASET.md)*
