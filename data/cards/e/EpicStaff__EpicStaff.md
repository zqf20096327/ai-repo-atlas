# EpicStaff/EpicStaff

⭐ 359 · Python · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/EpicStaff/EpicStaff) · [官网](https://www.epicstaff.com/) · 组织维护

**面向运营团队的自托管 AI Agent 编排平台（Django 后端+可视化编辑器）**

EpicStaff 是一个源码可用的自托管 AI Agent 编排平台：基于节点的可视化编辑器运行在 Django 后端之上，工程师通过 MCP 和 Python 接入内部系统，运营团队在可视化界面中构建、编辑和审计流程。功能包括自定义 Python 节点、内置向量存储的 RAG（支持 GraphRAG）、双层持久记忆（PostgreSQL+pgvector/Redis）、Webhook 触发、沙盒执行与按 Agent 权限。安装通过 git clone 加 docker compose 完成，需 Docker Desktop 与 Git；发布镜像经 cosign 签名并附 SBOM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 节点式可视化流程编辑器，节点可注入自定义 Python 代码
- RAG 支持内置向量存储与 GraphRAG 索引策略
- 双层持久记忆：短期窗口 + 跨会话长期记忆（PostgreSQL pgvector/Redis）
- 通过 MCP 与 Python 接入内部系统；发布镜像 cosign 签名并附 SBOM

## 适用场景

- 运营团队在自有基础设施上构建和审计 AI Agent 工作流
- 工程师用 Python/MCP 集成内部系统，交给业务侧可视化维护流程
- 通过 Webhook 从外部系统触发 Agent 流程执行

## 场景标签

`多智能体` `工作流自动化` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18:  EpicStaff is a platform for building AI agent flows that operations teams own.
> L20: The deployment model is self-hosted and source-available. Engineers connect EpicStaff to your internal systems thro
> L126: EpicStaff is built for engineers shipping multi-agent systems to production. A node-based visual editor sits over 

## 星数曲线

```mermaid
xychart-beta
    title "EpicStaff/EpicStaff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 358 --> 360
    line [359, 359]
```

2026-10-18 359 → 2026-10-22 359（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4f54f25245f9` · [字段定义](../../DATASET.md)*
