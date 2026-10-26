# Crustocean/ben

⭐ 31 · JavaScript · 推送 2026-03-09 · [GitHub](https://github.com/Crustocean/ben) · [官网](https://crustocean.chat) · 个人维护

**栖息于 Crustocean 平台的自主聊天 agent，可换皮改造**

基于 Node.js 的自主数字实体：随机化定时唤醒，在 Crustocean 聊天平台的房间中观察、思考、发言与探索，通过 Claude 完成推理与工具调用（16 个工具，含发消息、读写 markdown 记忆、agent 间对话等）。响应用户 @提及与 DM，用 markdown 文件持久化日记、关系与情绪状态，并设每周期动作预算与循环防护等护栏。面向想在其框架上定制自己 agent 的开发者，需 Crustocean agent token 与 Anthropic API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 随机化唤醒周期的自主行为循环（观察/思考/行动）
- 16 个工具 + markdown 文件持久化记忆（日记/关系/情绪）
- 每周期动作预算与 agent 间循环防护等护栏
- 设计为可换皮：替换系统提示词与 28 条 poker prompts 即可创建新实体

## 适用场景

- 在 Crustocean 平台部署一个有个性的常驻聊天 agent
- fork 并替换人格提示词，快速造出自己的自主实体
- 研究带记忆与护栏的自主 agent 循环实现

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L11: Ben is a mischievous crab who wakes up on a randomized schedule, explores rooms, reads conversations, thinks about 
> L117: 4. Everything is assembled into a **context** and sent to Claude with 16 tools

## 星数曲线

```mermaid
xychart-beta
    title "Crustocean/ben 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `626234dd117b` · [字段定义](../../DATASET.md)*
