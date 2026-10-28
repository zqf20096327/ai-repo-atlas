# Caellwyn/long-memory-character-chat

⭐ 24 · Python · MIT · 推送 2025-12-05 · [GitHub](https://github.com/Caellwyn/long-memory-character-chat) · 个人维护

**带中长程记忆机制的角色扮演对话应用**

面向角色扮演对话爱好者的 LLM 聊天应用，核心是三层记忆机制：逐字滚动聊天窗口（短期）、由 agent 自行更新并快照存入向量库的摘要草稿板（中期）、基于对话摘要与语义检索的向量库长期记忆（检索结果按时间戳排序回注提示词）。另含两个机制：以模型首次回复作为风格示例随每个提示注入以维持语言风格，以及运行中动态修改角色描述、地点与用户名以支持角色演化。README 未给出安装与运行命令，也未说明模型后端接入方式，属于作者自述的实验性项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 滚动聊天窗口 + 摘要草稿板 + 向量库的三层记忆架构
- 长期记忆按时间戳存储与检索，冲突时指示模型优先近期信息
- 以首条回复作为风格示例注入每次提示以维持角色语言风格
- 支持运行中动态修改角色描述、地点与用户名

## 适用场景

- 长篇角色扮演对话中保持设定、地点与既往事件的记忆
- 让角色性格与目标随剧情推进而演化
- 通过更换用户名在同一对话中模拟多角色互动

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Role-playing Chatbot for Long Conversations and Adventures
> L2:  A character chat with integrated medium and long-term memory
> L20: The Agent is provided with a multi-tiered "memory", or dynamically changing system prompt, which includes levels of

## 星数曲线

```mermaid
xychart-beta
    title "Caellwyn/long-memory-character-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `67880bad32cd` · [字段定义](../../DATASET.md)*
