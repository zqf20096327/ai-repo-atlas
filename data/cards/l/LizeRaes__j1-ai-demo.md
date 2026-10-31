# LizeRaes/j1-ai-demo

⭐ 25 · Java · MIT · 推送 2026-08-11 · [GitHub](https://github.com/LizeRaes/j1-ai-demo) · 个人维护

**面向开发者演示的企业 AI 客服分诊系统（医疗预约场景）**

由多个 Java 微服务组成的演示平台：患者提交支持请求后流入集中客服系统，经 LLM 分诊服务分类与路由（置信度低于 0.4 转人工），并由领域训练的 ML 模型（Java/DeepNetts）生成紧急度评分，紧急度 ≥0.8 升级至值班人员；另含历史工单向量检索、带 RBAC 的公司文档 RAG，以及自动准备 bug 修复 PR 的编码助手。各服务独立部署，提供 start-all.sh 一键启动。演示系统，无真实认证，部分集成为模拟。

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

- LLM 分诊 + 置信度阈值（<0.4 转人工）的人工接管控制模式
- Java/DeepNetts 训练的领域 ML 紧急度评分服务（含 MCP 变体）
- 历史工单向量检索与 RBAC 控制的公司文档 RAG 引用
- 自动准备 bug 修复 PR 的异步编码助手

## 适用场景

- 参考如何在业务工作流中加入 agent 与 ML 能力并保留人工控制
- 搭建和演练企业级 AI 客服分诊演示
- 学习多微服务（Quarkus/Helidon）+ LangChain4j 的架构组织

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L15: 3. Helpdesk calls the **AI triage** service (:8081) to classify and route the ticket with an AI confidence score.
> L18:  - **Urgency service** (:8086) generates a priority score from a domain-trained machine learning model (built in Ja
> L131: |ai-triage|Quarkus + LangChain4j|GPT-4o-mini / —|

## 星数曲线

```mermaid
xychart-beta
    title "LizeRaes/j1-ai-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3c1a79e6f642` · [字段定义](../../DATASET.md)*
