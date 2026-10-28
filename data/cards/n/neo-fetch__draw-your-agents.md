# neo-fetch/draw-your-agents

⭐ 27 · TypeScript · AGPL-3.0 · 推送 2026-07-28 · [GitHub](https://github.com/neo-fetch/draw-your-agents) · [官网](https://neo-fetch.github.io/draw-your-agents/) · 个人维护

**浏览器内可视化 AI agent 工作流编辑器，编译生成可运行的 Python 项目**

运行于浏览器（无需服务器与账号）的拖拽式图形编辑器：在 React Flow 画布上编排 agent、router、loop 等 8 类节点，经统一 JSON Graph IR 校验后编译为可独立运行的 Google ADK（默认）或 LangGraph Python 项目（.zip）。支持变量芯片系统、嵌套 pydantic 模型、critic/reviser 循环节点与 draw.io 导入（进行中）。本项目是编译器而非运行时，生成代码由用户自行部署执行。个人与非营利免费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Graph IR 编译到 Google ADK 或 LangGraph 两个目标，一键导出 .zip 项目
- 变量芯片系统：拖入 schema 字段生成 prompt 变量，支持跨祖先节点的 session-state 读取
- critic/reviser 循环节点编译为有界循环，外层图保持无环 DAG
- 纯浏览器运行，无服务器无账号，Tier 1 测试可零安装冷检出跑

## 适用场景

- 画 agent 工作流图并拿到可自托管的 LangGraph/ADK 源码
- 不想被可视化平台锁定，导出后在自己基础设施上运行
- 在浏览器里做 agent 图原型并实时预览生成的 Python 代码

## 场景标签

`Agent 框架` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L5: A visual builder that compiles drag-and-drop agent graphs into runnable Python projects for **two targets from one c
> L41: - **Two targets from one IR** — A single `compile(ir, { target })` emits a **Google ADK** project (default) or a **

## 星数曲线

```mermaid
xychart-beta
    title "neo-fetch/draw-your-agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-28 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `26d77aa24ff7` · [字段定义](../../DATASET.md)*
