# cqzyys/lang-agent

⭐ 338 · TypeScript · Apache-2.0 · 推送 2026-07-20 · [GitHub](https://github.com/cqzyys/lang-agent) · 个人维护 · 中文 README

**面向开发者的可视化 AI Agent 配置平台，基于 LangGraph**

以 LangGraph 为底层的可有限编程 Agent 配置平台，前后端分离（FastAPI 后端、React/HeroUI 前端），通过画布拖拽节点与边组合 Agent，支持自定义状态变量作用于节点与条件边。内置 LLM/VLM、文档加载、代码执行、命令执行、向量召回等节点及 ReactAgent、SupervisorAgent 预制 Agent，可配置 OpenAI 兼容渠道模型、MCP 工具和 postgres/milvus 向量库。设计理念接近 comfyUI，鼓励开发自定义节点；模型渠道目前仅支持 OpenAI 兼容接口。

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

- 可视化画布拖拽配置 Agent，节点/边/状态变量组合
- 自定义状态变量可作用于节点与条件边的输入输出
- 预制 ReactAgent（MCP 工具调用）与 SupervisorAgent（多 Agent 调度）
- 支持自定义节点开发，无需修改其他代码

## 适用场景

- 通过可视化拖拽搭建业务 AI Agent 流程
- 构建带向量召回的文档问答 Agent
- 用 MCP 工具或命令/代码执行节点扩展 Agent 能力

## 场景标签

`Agent 框架` `多智能体` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L3: 本项目是以LangGraph为底层技术来实现的一个可有限编程的Agent配置平台。
> L138: Agent配置是本项目的核心功能，目的是通过可视化的拖拽和输入来配置各种复杂的AI Agent。

## 星数曲线

```mermaid
xychart-beta
    title "cqzyys/lang-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 337 --> 339
    line [338, 338]
```

2026-10-18 338 → 2026-10-26 338（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6f0fe9b41296` · [字段定义](../../DATASET.md)*
