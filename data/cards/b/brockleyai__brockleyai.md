# brockleyai/brockleyai

⭐ 17 · Go · Apache-2.0 · 推送 2026-06-28 · [GitHub](https://github.com/brockleyai/brockleyai) · 组织维护

**面向生产环境的开源 AI agent 工作流基础设施**

用 Go 编写的自托管 AI agent 基础设施：将 agent 工作流定义为带类型校验的图（JSON 存于 Git），通过 Terraform 资源部署，运行在可水平扩展的无状态 worker 上，提供持久化异步执行、Prometheus 指标、OpenTelemetry 追踪与重试/限流。内含 Superagent 自主节点类型，支持 MCP 工具、沙箱 Python 执行与五层终止机制。面向把 AI 功能做进真实产品的开发团队，提供 Web UI、REST API、CLI、Terraform、MCP server、coding agent 六个对等接口；本地运行依赖 Docker Compose（PostgreSQL/Redis）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作流即代码：agent 图以 JSON Schema 强类型校验，brockley validate 本地跑 13 项检查
- Terraform 资源 brockley_graph 部署，支持 K8s/AWS/GCP/Azure 模块
- Superagent 自主节点：规划、工具调用、沙箱代码执行、五层终止
- 六个对等管理接口（Web UI/REST/CLI/Terraform/MCP/coding agents）

## 适用场景

- 把客服 agent、文档处理流水线等 AI 功能部署到生产环境
- 用 CI 在每个 PR 上校验 agent 工作流定义
- 按队列深度自动扩缩容运行多步自主 agent

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2:  Open-source infrastructure to build, deploy, and scale production AI agents.
> L10: Define agent workflows as typed, validated graphs. Deploy them with Terraform. Run them on horizontally-scaling wor
> L24: - **Built for production.** Single static Go binary. Durable async execution with step-level tracking. Prometheus m

## 星数曲线

```mermaid
xychart-beta
    title "brockleyai/brockleyai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0ecbeafc83ba` · [字段定义](../../DATASET.md)*
