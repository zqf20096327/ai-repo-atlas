# cram2/pycram

⭐ 50 · Python · GPL-3.0 · 推送 2025-12-01 · [GitHub](https://github.com/cram2/pycram) · [官网](https://pycram.readthedocs.io/en/latest/index.html) · 组织维护

**Python 认知机器人任务规划框架：以意图描述生成可执行机器人计划**

PyCRAM（Cognitive Robot Abstract Machine）是面向机器人的高层任务规划与执行框架：用 designator 表达"做什么"的意图，运行时再落地为具体动作；支持晚绑定、顺序/并行/重试等控制流组合计划、前置/后置条件校验、ORM 持久化执行轨迹，并集成世界模型与运动构建块（TCP、夹爪、抓取搬运）。同一高层逻辑可复用于不同机器人平台，提供仿真优先工作流与浏览器内虚拟研究大楼演示。主要给机器人学研究者与开发者使用；完整功能需配合 ROS 安装以加载 URDF 与 RViz2 可视化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- designator 意图式任务描述，运行时晚绑定落地
- 顺序/并行/重试/监控等控制流的可组合计划树
- ORM 持久化计划、动作与空间数据以支持复现分析
- 平台无关：意图与具体机器人本体分离，跨平台复用

## 适用场景

- 在仿真中快速迭代机器人抓取搬运等操作任务
- 编写跨机器人平台复用的高层任务计划
- 记录并分析机器人执行轨迹用于基准与失败分析

## 场景标签

 · 领域:机器人/认知架构

## 证据(README 行号)

> L3: - Intent-based task specification: express “what” to do using designators; the framework decides the concrete “how” 
> L5: - Composable plans: build behaviors as trees of plan nodes with clear control-flow constructs (sequential, parallel,

## 星数曲线

```mermaid
xychart-beta
    title "cram2/pycram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-31 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c44a52691079` · [字段定义](../../DATASET.md)*
