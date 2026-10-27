# yu-iskw/cursor-experiments

⭐ 27 · Shell · 推送 2026-06-03 · [GitHub](https://github.com/yu-iskw/cursor-experiments) · 个人维护

**Cursor IDE 多 Agent 编排演示项目：旅行规划协作示例**

在 Cursor IDE 内演示专用 AI Agent 协作的示例仓库：定义 @trip-planner 主编排 Agent，委派 @flight-researcher 与 @hotel-researcher 子 Agent，配合 Agent Skills 执行 shell 脚本检索数据，最终生成旅行报告与任务日志（含 Mermaid 执行路径图）。航班与酒店搜索由返回随机结果的 Bash 脚本模拟，用于展示数据流。Agent 定义存放于 .cursor/agents/（YAML frontmatter Markdown），技能存放于 .cursor/skills/。使用方式为在 Cursor 中打开仓库并通过 Chat 面板调用 /trip-planner。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主编排 Agent 向专用子 Agent 透明委派子任务
- Agent Skills 通过执行 shell 脚本执行特定动作
- 生成旅行报告与任务日志，任务日志中含 Mermaid 执行路径图
- 航班/酒店搜索由返回随机结果的模拟脚本实现

## 适用场景

- 学习 Cursor 中多 Agent 层级编排的配置方式
- 参考 Agent 定义（.cursor/agents/）与 Agent Skills（.cursor/skills/）的写法
- 作为自有项目多 Agent 架构的起步模板

## 场景标签

 · 领域:AI 开发工具/Agent 编排

## 证据(README 行号)

> L3: This project demonstrates how specialized AI agents can collaborate to solve complex, multi-step tasks within the Cu
> L7: The primary goal is to showcase the **orchestration capability** of Cursor's agentic framework. By defining a high-l
> L67: 3. **Simulation Scripts**: For this demo, flight and hotel searches are simulated using Bash scripts (`research_fli

## 星数曲线

```mermaid
xychart-beta
    title "yu-iskw/cursor-experiments 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5ced76ce9c16` · [字段定义](../../DATASET.md)*
