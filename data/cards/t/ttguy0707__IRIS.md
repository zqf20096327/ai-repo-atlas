# ttguy0707/IRIS

⭐ 69 · Python · 推送 2026-03-09 · [GitHub](https://github.com/ttguy0707/IRIS) · 个人维护 · 中文 README

**智能体工作流驱动的自动深度调研与报告生成系统**

基于 LangGraph 状态机的自动化调研系统：意图识别、路径规划、动态检索（本地文档 RAG / 混合全网搜索）、深度撰写、自我审查与局部修订构成闭环。内置 Grader LLM 评估检索文档相关性，触发熔断或降级至全网搜索；AsyncSqliteSaver 实现会话级持久化与跨轮修改指令。后端为 Python 3.10+ / FastAPI 全异步架构，使用 OpenAI API（GPT-4o/GPT-4o-mini）与 Tavily Search，前端 Vue 3 + Tailwind CSS，SSE 流式推送。面向需要深度学术调研报告的用户，从源码部署前后端。

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

- LangGraph 多节点状态机：Router/Planner/Researcher/Writer/Reviewer/Refiner 协同
- Grader LLM 相关性评估与熔断/智能降级机制
- SQLite Checkpoint 会话级持久化，支持跨轮断点续写与局部微调
- FastAPI 全异步后端 + SSE 流式传输，Vue 3 前端渲染数学公式

## 适用场景

- 让 AI 自动完成从检索到成稿的深度调研报告
- 基于自己上传的文档做问答与报告撰写（含无关文档熔断提示）
- 对已生成报告下达修改指令进行局部扩写或调整

## 场景标签

`Agent 框架` `RAG` `科研工具` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **IRIS** 是一个基于 **Agentic Workflow（智能体工作流）** 的自动化深度调研与报告生成系统。它摒弃了传统单向 RAG（检索增强生成）的线性问答模式，通过构建多节点状态机（State Machine），
> L16: * 🧠 **Agentic 工作流引擎 (Powered by LangGraph)**
> L52: * **核心 LLM**: OpenAI API (GPT-4o, GPT-4o-mini)

## 星数曲线

```mermaid
xychart-beta
    title "ttguy0707/IRIS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-26 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ec28a6355267` · [字段定义](../../DATASET.md)*
