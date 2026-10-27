# redhat-community-ai-tools/UnifAI

⭐ 45 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/redhat-community-ai-tools/UnifAI) · 组织维护

**构建与运行多 Agent 工作流的企业知识平台**

面向企业知识检索场景的多 Agent 编排平台：将 Slack、Jira、PDF/Markdown 等数据源摄入 Qdrant 向量库（元数据存 MongoDB），再通过可组合的多 Agent 流水线查询。工作流以 YAML blueprint 或拖拽式 Web UI 定义，节点、LLM、工具、检索器均来自可插拔目录；本地用 LangGraph 执行，分布式用 Temporal，通过环境变量切换。支持 A2A 与 MCP 协议、NDJSON 实时流式输出、Keycloak 认证及 Helm/Kubernetes 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML blueprint 与拖拽 UI 两种方式定义 Agent 有向图
- LangGraph 本地执行与 Temporal 分布式执行可切换
- 内置 RAG 管道：PDF/Markdown/Slack 摄入、切块、嵌入、语义检索
- 支持 A2A 与 MCP 协议接入外部 Agent 与工具

## 适用场景

- 把散落在 Slack、Jira、文档中的企业知识统一检索与问答
- 可视化编排跨数据源的条件路由多 Agent 工作流
- 在 Kubernetes/OpenShift 上部署并横向扩展 Agent 执行

## 场景标签

`多智能体` `Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L27: The heart of UnifAI is its **Multi-Agent System (MAS)**: a production-grade orchestration engine for defining, exec
> L61: |**Local**|LangGraph|Development, single-process execution|

## 星数曲线

```mermaid
xychart-beta
    title "redhat-community-ai-tools/UnifAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9d54c67e18e0` · [字段定义](../../DATASET.md)*
