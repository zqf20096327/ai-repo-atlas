# langchain-ai/memory-agent-js

⭐ 53 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/langchain-ai/memory-agent-js) · 组织维护

**LangGraph.js 记忆型 ReAct Agent 示例：跨会话保存用户偏好**

由 LangChain 团队维护的 JavaScript 示例仓库：实现一个 ReAct 风格 agent，带 save-memories 工具，所有记忆按可配置的 userId 作用域存储，使 bot 能跨会话线程记住用户偏好。部署到 LangGraph Cloud 后可通过任意 API 调用；默认模型为 anthropic/claude-3-5-sonnet-20240620，也可切换 OpenAI 等兼容模型。README 说明如何自定义记忆结构、追加工具、换模型与提示词，并附带若干评测用例建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct agent + store_memory 工具实现记忆持久化
- 记忆按 userId 作用域，跨对话线程生效
- 默认模型 anthropic/claude-3-5-sonnet-20240620，支持配置切换
- 提供记忆结构、工具、模型、提示词四个自定义入口

## 适用场景

- 学习 LangGraph.js 中带记忆存储的 agent 实现方式
- 以该模板为基础搭建能记住用户偏好的对话 bot
- 参考其评测文件为记忆管理功能建立评估集

## 场景标签

`Agent 记忆` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L7: This repo provides a simple example of a ReAct-style agent with a tool to save memories, implemented in JavaScript. 
> L67: This chat bot reads from your memory graph's `Store` to easily list extracted memories. If it calls a tool, LangGra

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/memory-agent-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-27 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8f886d3686cc` · [字段定义](../../DATASET.md)*
