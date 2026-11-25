# Nitin-Shukla-eng/Multi-Agents

⭐ 10 · Python · 推送 2026-08-14 · [GitHub](https://github.com/Nitin-Shukla-eng/Multi-Agents) · [官网](https://multi-agents-jwsbzmdgrtx4i3fetouffz.streamlit.app/) · 个人维护

**为学习者提供的多 Agent 联网调研报告生成流水线**

ResearchMind 是一个小型多 Agent 系统，将主题调研拆为四步顺序执行：Search Agent 用 Tavily 搜索来源、Reader Agent 抓取最相关页面文本、Writer Chain 生成含引言/要点/结论/来源的结构化报告、Critic Chain 打分并给出改进建议。四个组件共用 gpt-4o-mini（temperature 0）。提供 Streamlit Web UI 与 CLI 两种运行方式，也提供在线演示；README 明示每次只抓取一个 URL、抓取内容截断至 3000 字符、无重试机制等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Search→Reader→Writer→Critic 四组件顺序协作流水线
- 提供 Streamlit Web UI 与命令行两种运行方式
- 在线演示版密钥由用户在侧栏输入，不存储不记录
- 报告可下载为 Markdown，搜索/抓取原始输出可展开查看

## 适用场景

- 输入一个主题，自动生成带来源的结构化调研报告
- 学习 LangChain tool-calling agent 与 LLM chain 的组合方式
- 查看每一步的中间输出以理解多 Agent 流程

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L9: ResearchMind is a small multi-agent system that automates the process of researching a topic end-to-end: it searches
> L19: |3|**Writer Chain**|Prompt → LLM chain|Drafts a structured report (Introduction, Key Findings, Conclusion, Sources)
> L20: |4|**Critic Chain**|Prompt → LLM chain|Reviews the report and returns a score out of 10, strengths, areas to improv

## 星数曲线

```mermaid
xychart-beta
    title "Nitin-Shukla-eng/Multi-Agents 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `7d67eee409ad` · [字段定义](../../DATASET.md)*
