# RailtownAI/railtracks

⭐ 234 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/RailtownAI/railtracks) · [官网](https://docs.railtracks.org/) · 组织维护

**纯 Python 智能体框架：开发者自组装智能体工具调用回路**

Railtracks 是一个 Python agent 框架，用于构建智能体与 harness。所有组件为普通 Python 对象：工具调用回路、函数工具面、子智能体与 MCP 服务器接入、上下文管理、权限与预算控制、可回放运行记录，通过标准 Python 控制流表达执行顺序与分支循环，无 YAML/DSL。内置本地可视化器观察运行与评估，支持 decision_node 分类路由，兼容标准调试器与 IDE 补全。面向开发者，通过 pip 安装，经统一接口接入多家模型提供商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Loop/Tool surface/Context/Controls/Record 五部件按需组装
- 任何 Python 函数自动转换为工具，支持 MCP 协议接入
- 本地运行的可视化器实时检查智能体运行与评估
- decision_node 单次调用返回校准概率，用于分类/路由/评分

## 适用场景

- 构建带人工审批与审计记录的高风险工具操作智能体
- 搭建代码编辑类 harness，文件写入前停下等待批准
- 为检索研究型智能体配置记忆与结构化输出报告

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L26: Railtracks is a Python **agent framework** for building your own **agents and/or harness**. Every piece is an ordin
> L138: Railtracks integrates with major model providers through a unified interface:

## 星数曲线

```mermaid
xychart-beta
    title "RailtownAI/railtracks 星数(近 8 点)"
    x-axis ["2026-10-23", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-20", "2026-11-21", "2026-11-25"]
    y-axis "stars" 232 --> 237
    line [234, 235, 236, 234, 235, 233, 234, 234]
```

2026-10-23 234 → 2026-11-25 234（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `ebddc2ae493a` · [字段定义](../../DATASET.md)*
