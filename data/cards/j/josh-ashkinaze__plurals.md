# josh-ashkinaze/plurals

⭐ 43 · Python · 推送 2026-09-11 · [GitHub](https://github.com/josh-ashkinaze/plurals) · [官网](https://josh-ashkinaze.github.io/plurals/) · 组织维护

**模拟社会群体的多智能体 LLM 实验框架，面向计算社会科学研究**

Python 库，用于构建由 LLM Agent 组成的模拟社会群体（ensemble）：Agent 携带系统指令与任务，置于链、图、辩论、集成、循环等信息共享结构中，可由 Moderator 汇总回应。人格指令可来自美国 ANES 选举调查数据，支持全国代表性焦点小组模拟；提供 Best-of-N（可验证奖励/LLM-as-judge）、Interview 人生故事人格生成、Loop 收敛循环等功能。面向学术界用户，配套 CHI 2025 论文与教程文档，需设置 OpenAI/Anthropic API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent + 结构（Chain/Graph/Ensemble/Loop/Debate）+ Moderator 的三组件架构
- 接入 ANES 政府调查数据生成全国代表性人格焦点小组
- Best-of-N 并行生成，支持可验证奖励与 LLM-as-judge
- Interview 类通过模拟访谈生成结构化 JSON 人生故事人格

## 适用场景

- 运行全国代表性模拟焦点小组做受众研究
- 实验不同信息共享结构对 LLM 审议质量的影响
- writer/critic 循环迭代优化文本至满足停止条件
- 多视角 Agent 协作生成与打磨说服性信息或创意方案

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L37: Plurals is an end-to-end generator of simulated social ensembles. (1) **Agents** complete tasks within (2) **Struct
> L39: The building block is Agents, which are large language models (LLMs) that have system instructions and tasks. Syste
> L150: Plurals is run by a small and energetic team of academics doing the best they can [1]. To report bugs or feature r

## 星数曲线

```mermaid
xychart-beta
    title "josh-ashkinaze/plurals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c9b671171191` · [字段定义](../../DATASET.md)*
