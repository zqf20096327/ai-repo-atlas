# bbossgroups/bboss-elastic-tran

⭐ 27 · Java · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/bbossgroups/bboss-elastic-tran) · [官网](http://www.bbossgroups.com) · 组织维护 · 中文 README

**Java 数据采集同步 ETL 工具与 Elasticsearch ORM 客户端**

bboss 开源的 Java 数据工具：提供数据采集、清洗转换、入库及流批一体化指标统计计算，兼作兼容 ES 1.x-9.x 各版本的 Elasticsearch ORM 客户端，支持 Spring Boot 1.x-3.x。作业用 Java 开发，可独立运行或嵌入 Java 应用，提供作业控制与监控 API（启动/暂停/继续/停止）。另含 jobflow 编排引擎，支持将数据作业、业务任务及多智能体大模型推理任务编排为工作流与有向循环图，含智能体长短期记忆分层管理。通过 Maven 依赖或 gradle 源码构建使用，需 JDK 1.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流批一体化数据处理与多维度时间窗口指标计算
- 100% 兼容 Elasticsearch 1.x-9.x 各版本的 ORM 客户端
- 作业控制 API：启动、暂停、继续、停止与监控
- jobflow 支持多智能体协同与迭代执行的有向循环图编排

## 适用场景

- 数据库到 Elasticsearch 等目标的数据同步 ETL 作业
- 流批一体的实时增量与存量数据指标统计
- 编排数据采集与多智能体大模型推理任务的工作流

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: bboss-datatran由 bboss 开源的数据采集同步ETL工具，提供数据采集、数据清洗转换处理和数据入库以及数据指标统计计算流批一体化处理功能。
> L66: # bboss-jobflowgraph
> L73: - 基于有向循环图的智能体协同、自主规划、迭代执行、结果评估和优化机制；可灵活设置最大循环次数，避免流程陷入无限循环

## 星数曲线

```mermaid
xychart-beta
    title "bbossgroups/bboss-elastic-tran 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `80484da59cd2` · [字段定义](../../DATASET.md)*
