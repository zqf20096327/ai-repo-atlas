# ntg2208/production-ai-customer-support

⭐ 23 · Python · MIT · 推送 2025-12-06 · [GitHub](https://github.com/ntg2208/production-ai-customer-support) · [官网](https://twentytwotensors.co.uk) · 个人维护

**面向终端用户的量产级多智能体 AI 客服系统（含教程）**

基于 Google ADK 的多智能体客服应用：Master Agent 分析意图并路由到 Policy Agent（RAG 检索公司政策）与 Ticket Agent（查询/预订/改签），支持位置检测、状态管理、PII 脱敏与提示注入防御等安全护栏，以及用 Gemini 做的 6 维 LLM-as-a-Judge 自动评测。演示场景为虚构的 UKConnect 铁路客服，含 15 个测试场景与配套教程系列。安装方式为 git clone 源码 + pip 安装依赖 + 配置 GOOGLE_API_KEY，需 Google AI API key。

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

- Master/Policy/Ticket 三智能体编排，支持串行与并行路由
- ADK callbacks 实现的 PII 脱敏、提示注入防御与内容审核护栏
- 6 维 LLM-as-a-Judge 评测（准确率/有用性/任务完成等加权打分）
- 15 个测试场景、Docker 与云端部署文档、8 集配套教程

## 适用场景

- 搭建交通/酒店/医疗等行业的 AI 客服系统
- 学习企业级多智能体架构与安全护栏的实现
- 用 LLM-as-a-Judge 评测流程自动评估客服回答质量

## 场景标签

`多智能体` `聊天机器人` `模型评测` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L61: - **Master Agent**: Primary orchestrator that analyzes customer queries, maintains context, and intelligently route
> L62: - **Policy Agent**: RAG-powered specialist for company policies, refund rules, terms & conditions, and fare regulat

## 星数曲线

```mermaid
xychart-beta
    title "ntg2208/production-ai-customer-support 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `a9c1fecca825` · [字段定义](../../DATASET.md)*
