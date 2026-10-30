# jerry1993-tech/Cornucopia-Multi-Agent

⭐ 15 · Python · 推送 2026-06-06 · [GitHub](https://github.com/jerry1993-tech/Cornucopia-Multi-Agent) · 个人维护 · 中文 README

**多智能体协作框架：6 种协作模式与 8 种工具编排 agent 任务**

基于 Python 的多智能体协作编排框架，面向构建 agent 应用的开发者。提供 6 种协作模式（顺序、并行、辩论共识、专家团队、批评审查、层级协作）、6 种通信拓扑与 4 条执行路径（简单执行、LLM 协作、深度聚类、动态工作流），内置 8 种工具（搜索、数据分析、代码执行、报告生成等）经统一注册表调度，采用 OpenAI function-calling 兼容 schema。LLM 默认接 DashScope 的 qwen3.6-27b，提供 FastAPI 服务端、WebSocket 实时流与 Streamlit Web UI，从源码以 venv 方式安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种协作模式与 6 种通信拓扑，统一 BaseCollaboration 接口
- 8 种专业工具经注册表调度，OpenAI function-calling 兼容 schema
- DeepPlanner 任务分解 + AgentCluster 工具调用循环的深度聚类路径
- FastAPI + WebSocket 实时流与 Streamlit 可视化界面

## 适用场景

- 搭建市场研究、报告生成等多 agent 流水线
- 需要辩论共识或批评审查机制提升输出质量的任务
- 通过 Web UI 可视化编排和监控 agent 协作

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Cornucopia is a production-grade multi-agent collaboration framework that supports:
> L153: Cornucopia provides **8 professional tools**, managed and dispatched through a unified registry (`cornucopia/tools

## 星数曲线

```mermaid
xychart-beta
    title "jerry1993-tech/Cornucopia-Multi-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9badbf439e25` · [字段定义](../../DATASET.md)*
