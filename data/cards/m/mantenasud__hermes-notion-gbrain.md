# mantenasud/hermes-notion-gbrain

⭐ 10 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/mantenasud/hermes-notion-gbrain) · 个人维护

**通过 WhatsApp/Slack 自然语言管理 Notion 任务并写入 GBrain**

为 Hermes agent 提供的一组技能脚本：将 WhatsApp/Slack 的自然语言消息解析为任务操作（创建、标记完成、列出、改期、归档），写入 Notion 任务数据库并按项目归类；另含每周 cron 脚本，调用 OpenAI gpt-4o-mini 将一周内更新的任务蒸馏为项目级摘要页写入 GBrain 知识库。依赖已运行的 Hermes、GBrain 与 Notion 集成，通过复制脚本并手动配置 token、数据库 ID、项目映射完成安装。

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

- 自然语言消息驱动 Notion 任务的增删改查与项目归属推断
- 每周 cron 用 gpt-4o-mini 蒸馏任务为 GBrain 项目上下文页
- OpenAI key 直接读取 GBrain 配置，无需单独设置
- 提供 system_prompt 片段与故障排查指引

## 适用场景

- 在 WhatsApp 里用一句话记录和跟进工作任务
- 让 AI agent 维护 Notion 任务库并自动汇总项目进展
- 为个人 agent 沉淀每周工作上下文

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L3: Natural language task management via WhatsApp and Slack, backed by Notion,
> L19: Every Sunday, a cron job pulls all tasks updated that week, distils them into
> L38: - `gbrain_enrichment.py` — weekly cron that distils Notion tasks into GBrain knowledge pages

## 星数曲线

```mermaid
xychart-beta
    title "mantenasud/hermes-notion-gbrain 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `12e43df15fec` · [字段定义](../../DATASET.md)*
