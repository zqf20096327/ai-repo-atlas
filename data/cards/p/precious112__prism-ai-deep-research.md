# precious112/prism-ai-deep-research

⭐ 19 · TypeScript · MIT · 推送 2026-02-19 · [GitHub](https://github.com/precious112/prism-ai-deep-research) · [官网](https://prism-ai.glyde.world/) · 个人维护

**开源深度研究智能体：多 Agent 协作生成带引用的研究报告**

面向学生、开发者与学习者的开源深度研究应用，自我定位为 Perplexity Pro 与 OpenAI Deep Research 的替代品。采用 Plan-and-Execute 架构：PlanningAgent 先将复杂问题拆解为目录结构，再并行生成多个 Researcher Agent 搜索、爬取并阅读网页，最后聚合为带直接来源链接的引用报告，并可生成 React 图表组件做可视化。技术栈为 Python+LangGraph/LangChain 核心、Node.js/Express API、Next.js 前端、Go WebSocket + Redis 实时层，通过 Docker Compose 部署，运行需要 OpenAI 与 Serper API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PlanningAgent 生成研究路线图后再执行的多 Agent Plan-and-Execute 架构
- Python asyncio 并行运行 5+ 研究 Agent
- LangGraph 状态机：Agent 可自我纠正、回环并重试搜索
- 每条结论附带来源直链，并可生成自定义 React 图表组件

## 适用场景

- 对任意主题生成结构化、带引用的深度研究报告
- 学术场景下综合文献综述与查找引用
- 指向 GitHub 仓库以理解其架构与关键组件

## 场景标签

`科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Prism AI solves this by orchestrating a team of autonomous agents.** Whether you're a student, a developer, or a 
> L39: * **🔄 LangGraph State Machine**: Agents aren't just chains; they are state machines that can self-correct, loop bac

## 星数曲线

```mermaid
xychart-beta
    title "precious112/prism-ai-deep-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8f4230b77403` · [字段定义](../../DATASET.md)*
