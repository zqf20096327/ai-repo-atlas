# langchain-ai/ambient-agent-101

⭐ 35 · Jupyter Notebook · 推送 2026-10-24 · [GitHub](https://github.com/langchain-ai/ambient-agent-101) · 组织维护

**通过构建环境邮件助手学习 LangGraph 基础的教程仓库**

LangChain 官方的教学仓库，是 LangChain Academy 内容的浓缩版，面向在 LangChain 工程师带领下参加培训的开发者。通过一个 notebook 分 4 节构建接入 Gmail API 的 ambient 邮件助手：ReAct agent 基础、human-in-the-loop、记忆（基于 LangGraph Store 持久化），以及可选的评测节（Pytest + LangSmith evaluate API，含 LLM-as-a-judge）。默认使用 OpenAI，可在 utils.py 中切换 Anthropic/Bedrock/AzureOpenAI 等。提供 editable 安装方式与自动化测试套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 节 notebook：ReAct agent → human-in-the-loop → memory → evaluation
- 邮件助手接入 Gmail API 并可部署到 LangGraph Platform
- 使用 LangSmith evaluate API 做评测（LLM-as-a-judge、工具调用与分流判定）
- 附自动化测试套件，结果记录到 LangSmith

## 适用场景

- 系统学习 LangGraph 的 agent、HITL 与记忆机制
- 参考邮件助手实现来构建自己的 ambient agent
- 了解基于 LangSmith 的 agent 评测方法

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: In this session, you will learn about the fundamentals of LangGraph through one of our notebooks. It builds up to an
> L6: This is a condensed version of LangChain Academy, and is intended to be run in a session with a LangChain engineer. 

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/ambient-agent-101 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a6b384e93c1` · [字段定义](../../DATASET.md)*
