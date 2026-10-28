# Quazi-07/Research-Grant-Finder-Agent

⭐ 29 · Python · 推送 2026-07-08 · [GitHub](https://github.com/Quazi-07/Research-Grant-Finder-Agent) · 个人维护

**面向科研人员的 NIH 基金机会智能检索与排序工具**

以多 agent 工作流组织的基金发现原型：从 NIH Guide、Grants.gov 采集公开资助机会，归一化去重后由 ML Relevance Agent 依据计算关键词、标题中心性、文本相似度、截止日期等信号打 0-100 相关性分并分为 HIGH/MEDIUM/WATCHLIST 三级；可从 NIH RePORTER 拉取已资助项目上下文，支持研究者反馈记录。以 Streamlit 仪表盘交互，SQLite 持久化，可导出 Excel 与 Markdown 摘要。定位为功能性研究原型，当前评分引擎不依赖 LLM 做自主科学推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 个专职 agent 组成的基金发现工作流（摄取/解析/相关性/上下文/摘要/反馈）
- 多信号可解释相关性评分（0-100，三级分类），保留匹配理由
- NIH RePORTER 已资助项目上下文检索
- Streamlit 交互仪表盘：筛选、截止日期监控、Excel 导出

## 适用场景

- AI/数据科学/生物信息团队从 NIH 与 Grants.gov 中筛选相关资助机会
- 追踪即将截止的高相关性基金公告
- 查看某个机会被优先推荐的具体匹配理由

## 场景标签

`科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L24: Instead of treating funding discovery as a simple keyword search problem, this AI tool organizes the process as an 
> L63: The system separates major grant intelligence tasks into specialized AI agents.
> L305: The current intelligence engine uses explainable computational scoring and text similarity.

## 星数曲线

```mermaid
xychart-beta
    title "Quazi-07/Research-Grant-Finder-Agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-28 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4741e8c874d7` · [字段定义](../../DATASET.md)*
