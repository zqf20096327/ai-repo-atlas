# Qredence/agentic-fleet

⭐ 111 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/Qredence/agentic-fleet) · [官网](https://agenticfleet.com) · 组织维护

**基于 DSPy 与 Microsoft Agent Framework 的多智能体编排运行时**

Python 编写的生产导向多智能体编排系统：任务经五阶段流水线（分析→路由→执行→进度→质量）分派给 9 个以上专业智能体，支持 Auto/Delegated/Sequential/Parallel/Handoff/Discussion 六种执行模式。DSPy 提供结构化推理与类型化签名，模型调用需 OpenAI API Key（可选 Azure OpenAI），存储可选 Azure Cosmos DB 或本地 SQLite。提供 Typer CLI、Python API 与 React Web 界面（SSE/WebSocket 流式），含 OpenTelemetry 追踪、Azure AI 评测、HITL 暂停与检查点恢复。安装通过 git clone + uv（make install），前端需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五阶段流水线与 6 种执行模式、9+ 专业智能体路由
- DSPy 类型化签名与离线编译，Pydantic 校验输出
- Tavily 搜索、代码执行、浏览器自动化、MCP 工具集成
- OpenTelemetry/Jaeger 追踪、HITL 与检查点恢复

## 适用场景

- 用自然语言任务驱动多个专业智能体协作完成研究与写作
- 作为多智能体工作流引擎嵌入自己的 Python 应用
- 通过 Web 界面实时查看智能体编排与执行过程

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12:  Self-optimizing multi-agent orchestration powered by DSPy + Microsoft Agent Framework.
> L16: **AgenticFleet** is a production-ready multi-agent orchestration runtime that routes tasks to specialized agents th
> L120: AgenticFleet is a production-oriented multi-agent orchestration system that **automatically routes tasks to specia

## 星数曲线

```mermaid
xychart-beta
    title "Qredence/agentic-fleet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 110 --> 112
    line [111, 111]
```

2026-10-18 111 → 2026-10-23 111（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `568da9f52a09` · [字段定义](../../DATASET.md)*
