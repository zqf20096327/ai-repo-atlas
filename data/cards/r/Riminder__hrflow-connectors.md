# Riminder/hrflow-connectors

⭐ 42 · Python · Apache-2.0 · 推送 2026-04-14 · [GitHub](https://github.com/Riminder/hrflow-connectors) · [官网](https://www.hrflow.ai) · 组织维护

**HR 数据连接器库：在 HrFlow.ai 与 ATS/招聘平台间同步人才数据**

HrFlow.ai 公司维护的开源 Python 连接器仓库：提供低代码方式创建连接器，在外部系统（ATS/CRM/HCM/招聘板）与 HrFlow.ai 的 Board/Source 之间拉取或推送职位与人才档案数据，支持条件同步（logics）、自定义格式化（format）及解析/更新等仓库选项。开源连接器 20 余个，另有需 API Key 的 Premium 连接器清单。使用前需创建 Workspace 并获取 API Key，通过 pip 安装，配套开发文档与 API（解析、嵌入、搜索、打分等）。

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

- 低代码连接器框架，抽象化概念便于快速创建新连接器
- 支持外部系统与 HrFlow.ai 间职位/档案的双向同步
- logics 条件过滤与 format 自定义格式化
- 开源连接器 20+，覆盖 Greenhouse、Bullhorn、SmartRecruiters 等

## 适用场景

- 把 ATS 中的职位和候选人档案同步到 HrFlow.ai 做统一处理
- 按自定义条件过滤同步特定数据流
- 开发者贡献新连接器扩展框架

## 场景标签

 · 领域:HR Tech/数据集成

## 证据(README 行号)

> L23: **HrFlow-Connectors** is an open-source project created by HrFlow.ai to democratize Talent Data integration within 
> L213: With HrFlow-Connectors, you can **synchronize** and **process** multiple **HR data streams** in just a few lines o
> L217: - Pull jobs : `External Job flow` :arrow_right: ***`HrFlow.ai Board`***

## 星数曲线

```mermaid
xychart-beta
    title "Riminder/hrflow-connectors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6b1e7c13b8c1` · [字段定义](../../DATASET.md)*
