# temporal-community/ai-agents-workshop-python

⭐ 36 · Python · 推送 2026-06-05 · [GitHub](https://github.com/temporal-community/ai-agents-workshop-python) · 组织维护

**渐进式教程：用 OpenAI Agents SDK 与 Temporal 构建 AI agent**

由 Temporal 社区维护的 Python 工作坊，包含 6 组渐进式示例：手写 agentic loop、OpenAI Agents SDK 与 Temporal 集成插件、MCP 工具服务器、human-in-the-loop 信号交互、多 agent 编排（child workflow 与 Nexus）、以及跨框架（Strands）与跨语言（Java/Spring AI）的异构编排。每个示例独立（各自的 pyproject、task queue、worker），运行需 Temporal dev server、Python 3.10+、uv 与 OPENAI_API_KEY；demo3-6 需 F1 MCP server，demo6b 另需 JDK 21+。

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

- 6 组渐进式示例，每组新增一种 Temporal 原语（signal、child workflow、Nexus 等）
- temporalio.contrib.openai_agents 插件使 LLM/工具调用自动成为 activity
- MCP 工具经 StatelessMCPServerProvider 作为 Temporal activity 派发
- 跨框架与跨语言（Java/Spring AI）异构多 agent 编排示例

## 适用场景

- 学习如何用 Temporal 持久化执行机制构建可靠 AI agent
- 参考 human-in-the-loop 与多 agent 编排的实现模式
- 对比不同框架（OpenAI Agents SDK/Strands/Spring AI）与 Temporal 集成方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A series of progressive demos that build an AI agent in Python using the OpenAI Agents SDK and Temporal for durable 
> L5: Every demo is self-contained: its own `pyproject.toml`, its own task queue, its own worker. You can work through the

## 星数曲线

```mermaid
xychart-beta
    title "temporal-community/ai-agents-workshop-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e76f078726bc` · [字段定义](../../DATASET.md)*
