# Xander-Xai/Customer-Service-AI-Agent

⭐ — · [GitHub]() · 个人维护 · 中文 README

**企业客服多智能体 Agent 参考实现：双路径执行+人工审批治理**

独立维护的 LangGraph 多智能体客服工程参考实现，采用四层状态机（缓存→意图路由→专家 Agent 协作→响应后处理）。同步快路径经 /api/chat 实时回答，长任务落库入队由 Celery worker 从 Postgres checkpoint 续跑；高风险工具调用执行前摘出等待人工审批，工具副作用以 ledger 去重。默认 LLM 为 siliconflow/Qwen3-8B，检索为 Qdrant+BM25 融合。README 明确声明生产验收未完成、正式 RAG 指标 NOT_VERIFIED。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同步 /api/chat 快路径与异步 /api/runs 耐久路径共享同一图与 checkpoint
- HIGH 风险工具调用执行前 interrupt() 等待人工审批，TTL 过期按拒绝处理
- 三层幂等（run/thread/tool ledger）+ 崩溃后从 checkpoint 续跑
- 评测流水线自我认证失败机制，未验证指标标记 NOT_VERIFIED

## 适用场景

- 作为企业客服 Agent 的工程架构参考来搭建自己的服务
- 为带副作用操作（退款/改单）的 Agent 设计人工审批流程
- 学习分布式 Agent 的崩溃恢复与幂等去重实现

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **LangGraph-based Customer Service AI Agent** — multi-agent orchestration, hybrid RAG,
> L107: > 一句话：**一个同步快路径 + 异步耐久路径并存的企业客服 Agent 服务。**
> L63: 企业智能客服的难点不在"能不能调通 LLM"，而在下面这六件事。任何一件没做对，

## 星数曲线

```mermaid
xychart-beta
    title "Xander-Xai/Customer-Service-AI-Agent 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a468f5a7d123` · [字段定义](../../DATASET.md)*
