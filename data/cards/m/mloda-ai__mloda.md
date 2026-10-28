# mloda-ai/mloda

⭐ 97 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/mloda-ai/mloda) · [官网](https://mloda.ai) · 组织维护

**面向 AI 代理的声明式数据访问与插件化数据管道框架**

mloda 是一个 Python 框架，通过声明式 API 让 AI 代理、ML 管道和数据分析描述所需数据（WHAT），由框架解析依赖、链接插件并交付结果（HOW）。核心机制包括三类插件（FeatureGroup 定义转换、ComputeFramework 提供执行后端如 Pandas/Polars/Spark、Extender 提供日志/校验/血缘钩子），并内置结果到数据源的 lineage 追溯。支持 LLM 工具函数、上下文窗口组装和 RAG 特征链式声明等 AI 用例。限制：RAG 与上下文示例需自实现 FeatureGroup；不适用于实时流（<5ms）或单库简单查询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 API：用户/代理只描述需求，框架解析依赖并组装管道
- 三类插件体系：FeatureGroup / ComputeFramework / Extender
- 单管道内混用多种计算后端（Pandas/Polars/Spark）
- 内置 lineage 将任意结果追溯回数据源

## 适用场景

- 让 AI 代理以 LLM 工具函数形式获取多源数据
- 以声明式链式语法构建 RAG 管道（校验→检索→脱敏）
- 在 notebook 与生产集群间复用同一套插件

## 场景标签

`数据分析` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L9: > **Declarative data access for AI agents. Describe what you need - mloda delivers it.**
> L41: |Give AI agents data access|Declarative API - agents describe WHAT, not HOW|
> L99: Give LLMs deterministic data access - they declare what, mloda handles how:

## 星数曲线

```mermaid
xychart-beta
    title "mloda-ai/mloda 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 95 --> 97
    line [96, 96]
```

2026-10-18 96 → 2026-10-28 96（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7d4e2d6fd50a` · [字段定义](../../DATASET.md)*
