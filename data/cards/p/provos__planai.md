# provos/planai

⭐ 52 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/provos/planai) · 个人维护

**面向开发者的图结构 LLM 工作流编排框架**

PlanAI 是一个基于图的 Python 任务自动化框架：开发者以 TaskWorker 节点构建工作流，将传统计算（如 API 调用）与 LLMTaskWorker（支持 RAG）混合编排，用 Pydantic 保证输入输出类型安全，并提供类型感知数据路由、任务来源追踪、缓存、结果合并与 LLM 提示自动优化。支持 OpenAI、Ollama 等多种 LLM 提供方。附带可视化编辑器 PlanAIEditor（单独 pip 包）、Web 监控仪表盘及 DeepSearch 深度研究示例（可用 Ollama 本地运行）。框架采用 Apache 2.0 许可，部分示例应用另有许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图架构工作流，混合传统计算与 LLM 任务节点（LLMTaskWorker）
- Pydantic 类型安全与类型感知的数据路由
- 任务来源追踪与 Web 实时监控仪表盘
- 可视化编辑器 PlanAIEditor 与 DeepSearch 示例

## 适用场景

- 编排包含 LLM 调用与传统计算的多步骤自动化流程
- 从教材等内容生成问答数据集
- 在本地用 Ollama 运行深度研究工作流

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: **PlanAI** is an innovative system designed for complex task automation through a sophisticated graph-based architec
> L15: - **Graph-Based Architecture**: Construct dynamic workflows comprising interconnected TaskWorkers for highly custom
> L115: - Integrating with various LLM providers (OpenAI, Ollama, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "provos/planai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9b04fefa553d` · [字段定义](../../DATASET.md)*
