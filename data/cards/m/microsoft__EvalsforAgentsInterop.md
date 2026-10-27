# microsoft/EvalsforAgentsInterop

⭐ 40 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/microsoft/EvalsforAgentsInterop) · 组织维护

**微软的 AI agent 评测平台：测试与评估企业智能体**

由三个组件组成的 agent 评测平台：FastAPI 后端（测试数据集管理、agent 注册与评测、MCP 服务器、Cosmos DB 持久化）、示例 agent（连接 MCP 服务器、使用 Azure OpenAI、演示日历与邮件能力）和 React 前端（创建数据集、注册 agent、运行评测、查看指标）。自有 agent 需暴露符合规范的无鉴权 HTTP POST 端点接入。依赖 Azure Cosmos DB 与 Azure OpenAI，用 Bicep 模板部署，支持 Docker Compose 或本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三组件架构：FastAPI 后端 + 示例 agent + React 前端
- 通过 MCP 服务器执行工具调用并记录评测
- 接入自有 agent 只需实现规范的 HTTP POST 端点
- Azure Bicep 模板一键部署 Cosmos DB 与 Azure Foundry 资源

## 适用场景

- 企业内评测 LLM 生产力 agent 的多维度表现
- 基于日历、邮件等场景数据集运行自动化测试
- 以示例 agent 为参考实现开发并接入自有 agent

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: - Agent registration and evaluation
> L27: - Running evaluations
> L194: To integrate your own agent with the evaluation platform, your agent must expose an unauthenticated HTTP POST endp

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/EvalsforAgentsInterop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9bd517123764` · [字段定义](../../DATASET.md)*
