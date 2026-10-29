# OpenDataBox/OpenCook

⭐ 30 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/OpenDataBox/OpenCook) · [官网](https://code4db.github.io/hi-opencook/) · 组织维护 · 中文 README

**给编码代理加项目级个性化的框架：规则、配方与多层记忆**

面向编码代理（coding agent）的项目个性化层：通过 Recipes（领域实现指南）、Rules（项目约束文件）与 4 层记忆栈（Working→Episodic→Project→Long-Term）包装任意编码代理。内置 Plan→Code→Test 多代理流水线（CodeAgent 编排、PlanAgent 定位改动范围、TestAgent 验证），迭代至补丁编译测试通过，输出文件 diff、轨迹记录与结构化报告。以数据库扩展函数（SQLite/PostgreSQL/DuckDB/ClickHouse）为参考场景，机制声明领域无关。Python 3.10+ 源码安装，需 LLM API key，支持多厂商并兼容 Claude Code/Codex 等 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Recipes + Rules + 4 层记忆的项目级个性化注入
- Plan→Code→Test 自纠错流水线，运行至测试通过
- 每次运行产出 diff、轨迹记录与结构化报告
- 与 Claude Code/Codex/OpenCode 等 agent 协同工作

## 适用场景

- 让编码代理按项目内部约定实现并交付可合并补丁
- 在数据库引擎等复杂 C/C++ 代码库中实现函数
- 跨长会话保持代理对项目约定与决策的记忆

## 场景标签

`编码 Agent` `Agent 记忆` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L34: **OpenCook is the missing layer.** It wraps any coding agent with three project-local primitives:
> L181: OpenCook runs a deterministic **Plan → Code → Test** pipeline through three specialized agents:

## 星数曲线

```mermaid
xychart-beta
    title "OpenDataBox/OpenCook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8ddb253162e1` · [字段定义](../../DATASET.md)*
