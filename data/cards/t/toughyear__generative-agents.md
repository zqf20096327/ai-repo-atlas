# toughyear/generative-agents

⭐ 84 · TypeScript · MIT · 推送 2026-05-31 · [GitHub](https://github.com/toughyear/generative-agents) · [官网](https://multimode.run/) · 组织维护

**基于 LLM 的生成式 Agent 框架（TypeScript）**

提供生成式智能体（Generative Agents）架构的 TypeScript 实现框架：核心库 generative-agents 含 Agent 与 AgentEngine，AgentEngine 管理网络请求与世界状态，Agent 支持接收观察流并自动反思更新内部状态。面向在沙盒环境做社会行为模拟、游戏动态 NPC、自主技能习得 agent 的开发者。当前仅有 TypeScript 实现与一个 React + Phaser 2D 示例，自述为实验性；LLM 调用依赖 OpenAI API（README 提及该 API 可能不稳定），示例代码中内置了作者的 OpenAI key，要求使用者自建 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent/AgentEngine 架构，管理网络请求与世界状态
- Agent 可接收观察流并自动反思、更新内部状态
- 附 React + Phaser 2D 顶视角像素游戏示例

## 适用场景

- 在沙盒环境中模拟复杂社会行为
- 为游戏创建动态 NPC
- 构建与环境交互中习得技能的自主 Agent（如 Minecraft 场景）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Simple Framework for working with Generative Agents powered by LLMs.
> L30: We have started with a TypeScript implementation of the agent architecture and plan to add more languages in the fu

## 星数曲线

```mermaid
xychart-beta
    title "toughyear/generative-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-28 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f61001533561` · [字段定义](../../DATASET.md)*
