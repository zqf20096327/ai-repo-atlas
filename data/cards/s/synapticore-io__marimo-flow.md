# synapticore-io/marimo-flow

⭐ 15 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/synapticore-io/marimo-flow) · 组织维护

**面向物理信息 ML 的多智能体科学计算平台，编排 PINA 工作流**

以 pydantic-ai/pydantic-graph 构建的反应式多智能体团队，端到端编排 PINA 物理信息神经网络工作流：用自然语言描述 PDE，智能体组合 Problem、设计网络、接线求解器并训练验证；全程通过 MLflow 记录追踪，并写入 DuckDB 16 表溯源库。提供 marimo 聊天 UI、CLI 及 A2A/AG-UI ASGI 服务器三种交互通道；LLM 供应商无关，默认指向 Ollama Cloud。也保留经典 marimo_flow.core API 供手动驱动 PINA；Docker 支持 CPU/CUDA/Intel XPU 三种镜像。限制：组合式 PDE 依赖 sympy 可表达范围。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 节点 pydantic-graph 状态机编排多智能体 PINA 工作流
- MLflow 追踪 + DuckDB 16 表溯源库记录每次运行与交接
- 组合优先的 PDE 构建（EquationSpec/SubdomainSpec/ConditionSpec，无硬编码 PDE 工厂）
- marimo 聊天 UI、CLI、A2A 与 AG-UI 服务器三种交互通道

## 适用场景

- 用自然语言描述 PDE 并让智能体团队完成建模、训练与验证
- 科学计算实验全程记录在 MLflow 并可查 DuckDB 溯源
- 在 CPU/CUDA/Intel XPU 的 Docker 环境中运行物理信息神经网络实验

## 场景标签

`多智能体` `MLOps` · 领域:Agent 开发

## 证据(README 行号)

> L19: **An agentic scientific-computing platform for physics-informed ML.**
> L20: A reactive multi-agent team orchestrates PINA / PINN workflows
> L35: Natural language goes in; a `pydantic-ai` multi-agent team turns it into

## 星数曲线

```mermaid
xychart-beta
    title "synapticore-io/marimo-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0dd671e67f53` · [字段定义](../../DATASET.md)*
