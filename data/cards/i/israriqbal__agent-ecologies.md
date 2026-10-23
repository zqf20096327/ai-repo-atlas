# israriqbal/agent-ecologies

⭐ 122 · HTML · 推送 2026-10-22 · [GitHub](https://github.com/israriqbal/agent-ecologies) · 个人维护

**多智能体操作系统：让 LLM 驱动的 NPC 自主生活在像素世界中**

Agent-Worlds 是一个基于 FastAPI 与 Model Context Protocol (MCP) 的多智能体运行时：每个 NPC 由独立 LLM 实例驱动，在持久化 2D 像素世界中自主完成作息、习得技能、形成关系。核心组件包括世界内核、Agent Brain（可按角色分配 DeepSeek/OpenAI/Claude 等不同后端）、双层记忆库、JSON 定义的技能引擎与关系图。面向游戏开发者与 AI 研究者，提供实时仪表盘观察与干预；运行需 Python 3.10+、至少一个 LLM API key，小型世界（10-20 agents）最低 4GB RAM。

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

- 每个 NPC 独立运行 LLM 实例，可按角色混搭不同模型后端
- MCP 协议标准化上下文通信，模型可热切换
- 技能系统含 5 族技能与 5 级熟练度成长
- 持久化世界与双层记忆（短期 50-100 条交互、长期压缩摘要）

## 适用场景

- 构建 NPC 有自主日程与记忆的 RPG 城镇
- 在受控数字环境中研究群体涌现行为与信息传播
- 让自主角色互动生成涌现式叙事
- 搭建学生与 AI 角色互动的教学模拟

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Imagine a pixel-art world where artificial intelligence agents don't just respond—they *live*. They wake up, wander 
> L48: **MCP Broker**: The Model Context Protocol implementation that standardizes how agents send and receive context. Th

## 星数曲线

```mermaid
xychart-beta
    title "israriqbal/agent-ecologies 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 120 --> 123
    line [121, 122, 122]
```

2026-10-18 121 → 2026-10-23 122（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c3e30c57765f` · [字段定义](../../DATASET.md)*
