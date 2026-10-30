# PlumoAI/plumoai

⭐ 78 · Python · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/PlumoAI/plumoai) · [官网](https://plumoai.com) · 组织维护

**自托管自主 AI 员工平台：创建并运行承担业务职责的 AI 雇员**

面向个人、初创到企业的自托管平台，用于创建和运行‘AI 员工’：可创建数量不限的 AI 员工，运行于自有基础设施，分配职责，通过 MCP 服务器或专用 Agent 连接邮件、CRM、数据库等外部系统，并内置项目管理系统。工作流构建区分无 LLM 的确定性节点与推理型 AI Agent。以 Docker Compose 多容器栈交付（UI/API/AI 服务/MySQL/MongoDB/Milvus，Traefik 路由），另有按用量计费的 PlumoAI 云托管选项。README 自述处于 Public Beta，部署为单节点参考架构、无高可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 创建不限数量的 AI 员工并运行在自有基础设施上
- AI Agent 生态：通过 MCP 服务器连接邮件/CRM/数据库等外部系统
- n8n 风格的确定性无 LLM 工作流节点与 AI Agent 分离
- Docker Compose 多容器部署，含备份/恢复/监控（Prometheus/Grafana）脚本

## 适用场景

- 企业自托管部署 AI 员工承担外联、调度等业务职责
- 通过 MCP 将外部工具接入 AI 员工并统一管理
- 在自有服务器上免费运行不限数量的 AI 员工与项目管理

## 场景标签

`工作流自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L15: PlumoAI is the **world's first platform designed to run Autonomous AI Employees**.
> L61: PlumoAI supports an extensible ecosystem of **AI Agents**.
> L63: AI Agents connect external systems to the platform using MCP servers or any specific agent.

## 星数曲线

```mermaid
xychart-beta
    title "PlumoAI/plumoai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-30 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1f189f6cc091` · [字段定义](../../DATASET.md)*
