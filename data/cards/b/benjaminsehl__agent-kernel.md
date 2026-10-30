# benjaminsehl/agent-kernel

⭐ 32 · 推送 2026-04-15 · [GitHub](https://github.com/benjaminsehl/agent-kernel) · 个人维护

**给 agent 提供持久记忆的 markdown 工作区模板**

一组 markdown 文件构成的公开参考模板，用于让无跨会话记忆的 agent 变为有状态：AGENTS.md 定义操作规则与会话协议，IDENTITY.md 描述 agent 身份，KNOWLEDGE.md 作为知识索引。记忆分为两类——knowledge/ 存放可变的状态事实，notes/ 存放追加式的叙事记录；另设 raw/ 收集原始材料、outputs/ 保存可复用产物。包含 DREAM.md 反思协议，按 Orient/Signal/Consolidate/Prune 四阶段决定哪些信号值得沉淀。工作区由 agent 维护，人类可浏览但无需手动维护。

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

- AGENTS.md/IDENTITY.md/KNOWLEDGE.md 三个核心文件构成 agent 状态
- 状态（knowledge/）与叙事（notes/，追加式）两类记忆分离
- raw→knowledge→outputs 的原始材料到编译知识再到产物结构
- DREAM.md 四阶段反思协议（Orient/Signal/Consolidate/Prune）

## 适用场景

- 让跨会话无记忆的 agent 通过文件读写保持状态
- 为 agent 项目搭一个可检查、可自由改编的记忆模板
- 按反思协议整理哪些短期信号值得固化为长期知识

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A small markdown workspace that helps an agent accumulate durable context over time.
> L5: This repository is a public reference template for people who want simple, inspectable files instead of a heavy memo
> L26: The agent has no built-in memory between sessions. The repo is how it becomes stateful — read to remember, write so

## 星数曲线

```mermaid
xychart-beta
    title "benjaminsehl/agent-kernel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e653522234e5` · [字段定义](../../DATASET.md)*
