# apple-aiml-research/ml-symphony

⭐ 65 · Svelte · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/apple-aiml-research/ml-symphony) · [官网](https://apple.github.io/ml-symphony/) · 组织维护

**组合交互式机器学习界面的组件框架（CHI 2022 论文代码）**

苹果 AI/ML 研究团队发布的框架，用于组合面向任务的、数据驱动的交互式机器学习界面组件，可跨计算笔记本与 Web 仪表板等平台使用。仓库含三部分：框架主体 symphony_ui、共享代码库 symphony_lib，以及作为组件提供的 widgets；通过 pip 安装框架后可按需安装单个组件或全部组件，可配合 DNIKit 生成分析数据并运行预计算示例。本代码为 CHI 2022 论文的配套实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨计算笔记本与 Web 仪表板组合 ML 交互组件
- 框架 + 共享库 + 可插拔 widgets 三层结构
- pip 安装，支持单个组件或全部组件安装
- 可配合 DNIKit 生成分析数据（如 Familiarity/Duplicates 组件）

## 适用场景

- 在计算笔记本中构建交互式 ML 数据分析界面
- 为机器学习工作流组装可复用的可视化组件
- 复现 CHI 2022 论文中的界面示例

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Symphony is a framework for composing interactive machine learning interfaces with task-specific, data-driven compon
> L16: - `symphony_ui`: The main Symphony project, containing the framework.

## 星数曲线

```mermaid
xychart-beta
    title "apple-aiml-research/ml-symphony 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-27 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `97601c460b2d` · [字段定义](../../DATASET.md)*
