# traveler-leon/smart-customer-service-system

⭐ 102 · Roff · MIT · 推送 2025-11-05 · [GitHub](https://github.com/traveler-leon/smart-customer-service-system) · [官网](https://traveler-leon.github.io/smart-customer-service-system/index.html) · 个人维护 · 中文 README

**面向机场场景的多智能体开源智能客服系统，可迁移至各行业**

基于 LangGraph 构建的多智能体智能客服系统，默认面向机场场景：意图分类器将请求路由到子智能体，提供 RAG 文档问答（RAGFlow 知识库）、Text2SQL 航班查询、业务办理（MCP 接入高德地图/12306 等后端 API）、多轮闲聊、情感识别与多语言支持。附带专家审核平台（批量评分、内容纠正、自动沉淀训练数据）与端到端指标评估平台。模型经 Xinference 部署，RAGFlow 需用户自行下载；运行依赖 Python 3.12+ 与 Redis。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体协作架构：意图分类路由至领域子智能体
- 同时支持 RAG、Text2SQL、后端 API 业务办理与多轮闲聊
- 专家审核平台形成数据闭环：审核通过问答自动入知识库，支持 Embedding 微调语料沉淀
- 指标评估平台覆盖业务与技术、端到端与组件级指标

## 适用场景

- 机场等垂直领域的在线智能客服问答与业务办理
- 需要持续运营迭代、有专家审核流程的客服场景
- 作为可迁移到其他行业的智能客服系统基座进行二次开发

## 场景标签

`多智能体` `文档问答` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L14: 系统采用**多智能体（Multi-Agent）协作架构**，通过意图分类器将用户请求智能路由到不同的子智能体，由各自领域的专家智能体精准地处理用户问题。
> L17: 1. **乘机须知问答**：覆盖安检、边检、海关、订票、值机、行李等全流程。
> L22: 系统支持多轮对话，能够根据上下文理解用户意图，并通过知识库检索和数据库查询为用户提供准确、及时的信息服务。

## 星数曲线

```mermaid
xychart-beta
    title "traveler-leon/smart-customer-service-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-31 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `e10f0b5e87ae` · [字段定义](../../DATASET.md)*
