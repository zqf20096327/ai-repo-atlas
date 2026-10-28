# Bbar0n234/learnflow-ai

⭐ 35 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/Bbar0n234/learnflow-ai) · 个人维护

**面向教师与演讲者的自托管 AI 教学材料生成工作台**

面向教师、技术演讲者与课程作者的自托管平台：以项目为单位组织工作，AI agent 在长期记忆（知识域）支撑下将作者的专长素材转化为讲义、摘要、手册与幻灯片。基于 LangGraph ReAct 循环实现单一通用 agent，配合可插拔的方法论技能包、子代理、MCP 网络搜索与 prompt-injection 分层防护；对话状态存于 PostgreSQL checkpoint，支持任意 OpenAI 兼容端点（含 on-prem vLLM）与 Langfuse 追踪。栈为 FastAPI + React，Docker Compose 部署，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 项目即上下文域：知识域长期记忆累积决策、术语与素材，会话可续接
- 单一 LangGraph ReAct agent，行为经配置扩展，附子代理与工具调用
- 支持任意 OpenAI 兼容端点（含 on-prem vLLM），Langfuse 追踪与请求级成本统计
- 技能包方法论（如讲座构建、GOST 报告格式），库开放贡献

## 适用场景

- 把我的课程素材整理成讲义、摘要和幻灯片
- 跨会话持续维护一门课程的术语与决策记忆
- 在自己的服务器上用自选模型生成教学材料

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L18: LearnFlow AI построен вокруг другой идеи: **проект как сфера контекста**. Вы создаёте проект — курс, доклад, серию 
> L40: - **Свой контур** — self-hosted развёртывание, любой OpenAI-совместимый endpoint (от облачных провайдеров до on-pre

## 星数曲线

```mermaid
xychart-beta
    title "Bbar0n234/learnflow-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3237d3a2daa8` · [字段定义](../../DATASET.md)*
