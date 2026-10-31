# NUGURI-7/CoCoWork

⭐ 15 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/NUGURI-7/CoCoWork) · [官网](https://cocowork.nuguri.org) · 个人维护 · 中文 README

**多 Agent 协作平台：supervisor 调度、Agentic RAG 与沙箱产出物**

基于 FastAPI + React + LangGraph 的多 Agent 协作平台：supervisor 拆解任务并分派成员，成员失败经 fallback 回报不中断回复；@ 直连成员可绕过调度层对话。每个知识库封装为独立 retriever tool 交由模型自行决定检索时机，底层支持向量（pgvector）、全文（jieba+TF-IDF）与混合检索（RRF 融合），可经 rerank 精排。挂载 Skill 的 Agent 在一次性 Docker 容器内执行脚本，产出物落对象存储并跨会话聚合复用。另含 HITL 人工确认、跨会话记忆、上下文工程与多会话并发。自部署需 Python≥3.12、Node.js、PostgreSQL(pgvector)、Redis，Docker 为沙箱可选依赖。

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

- supervisor 调度多 Agent 协作，@ 直连成员绕过调度层
- Agentic RAG：知识库封装为独立工具，支持向量/全文/混合三种检索与 rerank
- Skill 沙箱：一次性 Docker 容器执行，产出物落对象存储并跨会话聚合
- HITL 人工确认、跨会话记忆与按视角重写的历史机制

## 适用场景

- 搭建多 Agent 协作工作空间，让 supervisor 拆解并分派任务
- 将多个知识库以工具形式挂载给 Agent 按需检索
- 在沙箱中运行 Skill 脚本并复用文件产出物

## 场景标签

`多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L5: **多 Agent 协作平台**
> L27: supervisor 接收指令后拆解任务并分派至成员，成员独立执行并回报结果，由 supervisor 汇总。执行过程完整可见：工具调用、中间产出与失败重试实时展开于对话流。

## 星数曲线

```mermaid
xychart-beta
    title "NUGURI-7/CoCoWork 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d623c917aa77` · [字段定义](../../DATASET.md)*
