# kandada/fastclaw

⭐ 169 · Python · GPL-3.0 · 推送 2026-10-08 · [GitHub](https://github.com/kandada/fastclaw) · [官网](https://fastclaw-ai.com/) · 个人维护

**Python 轻量级 AI Agent 框架：多渠道、工具调用与定时任务**

基于事件驱动编排的 Python AI Agent 框架：用有向图编排 agent 行为节点，支持条件分支、工具调用（Shell 命令、技能、自定义集成）、cron 定时任务、多会话管理与流式输出；LLM 接入支持 OpenAI 与 Anthropic 网关（含 extended thinking 与 reasoning 字段统一提取），集成渠道包括飞书与 iMessage。提供 WebUI（localhost:8765）配置 agent 与技能热加载，可经 pip 安装或源码运行。GPL-3.0 许可，属于 FastMind 生态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 有向图编排 agent 节点，支持条件分支
- 工具调用、技能热加载与 skill_creator 元技能
- OpenAI/Anthropic 网关，兼容 DeepSeek/MiniMax/Moonshot 等端点
- cron 定时任务可投递结果到飞书，内置 fastbrowser 真实浏览器自动化技能

## 适用场景

- 搭建带工具调用与定时任务的个人 AI 助手
- 通过飞书/iMessage 等渠道与 agent 交互
- 用 Python 生态库（numpy/pandas 等）扩展 agent 能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A lightweight but powerful AI Agent framework in Python.
> L68: FastClaw is built on the core concept of **event-driven agent orchestration**. Key design principles:

## 星数曲线

```mermaid
xychart-beta
    title "kandada/fastclaw 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-25"]
    y-axis "stars" 168 --> 170
    line [169, 169]
```

2026-10-22 169 → 2026-10-25 169（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dd0bc5ca2908` · [字段定义](../../DATASET.md)*
