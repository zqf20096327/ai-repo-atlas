# EricSun0218/OpenGameAgent

⭐ 56 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/EricSun0218/OpenGameAgent) · [官网](https://opengameagent.com) · 个人维护 · 中文 README

**面向 AI 原生游戏角色的 TypeScript Agent 运行时**

MIT 许可的 TypeScript 运行时，为游戏提供消息-或-工具的单一 Agent 循环，游戏自身保留规则、权限与权威状态。能力包括 SQLite 持久化存储、可靠动作交换、可选结构化记忆（BGE-M3/向量加速）、提供者中立的可持久化输出媒体任务、语音识别/合成适配、MCP 工具接入，以及 Unity 6、Godot、Unreal 三种引擎集成。要求 Node.js 24.15.0，从源码构建运行；项目自述处于活跃开发中，建议集成时固定 commit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 Agent 循环架构，游戏保留权威状态与权限
- SQLite 单一权威存储：事件、动作、审批、记忆记录
- Unity 6 / Godot / Unreal Engine 三种引擎集成
- 提供者中立的持久化媒体任务与 OpenAI 兼容语音适配
- MCP 服务器显式接入与有界渐进式披露

## 适用场景

- 在 Unity/Godot/Unreal 游戏中为角色接入 AI Agent 行为
- 构建带持久化记忆与目标/信号/调度系统的活世界 NPC
- 为游戏角色配置语音识别与语音合成管线

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: OpenGameAgent is a TypeScript runtime for AI-native game characters and worlds. It hosts a message-or-tool Agent loo
> L8: This MIT-licensed source preview contains the Pi-backed Agent loop, exact run

## 星数曲线

```mermaid
xychart-beta
    title "EricSun0218/OpenGameAgent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 53 --> 57
    line [54, 55, 56, 56]
```

2026-10-18 54 → 2026-10-25 56（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `75558d9afca8` · [字段定义](../../DATASET.md)*
