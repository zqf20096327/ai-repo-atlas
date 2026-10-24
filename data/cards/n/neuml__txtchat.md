# neuml/txtchat

⭐ 339 · Python · Apache-2.0 · 推送 2026-02-13 · [GitHub](https://github.com/neuml/txtchat) · 个人维护

**构建接入聊天平台的本地 AI 对话助手框架**

基于 Python 3.10+ 和 txtai 构建的本地聊天助手框架：以 persona（聊天代理+工作流）形式定义助手，接入 Rocket.Chat、Mattermost 等消息平台，对消息返回 AI 驱动的回复。内置 Agent（联网）、Wikitalk（Wikipedia RAG 问答带引用）、Summary（URL 摘要）、Mr. French（翻译）等工作流，可用 LLM 或专用小模型；用户可自定义 txtai 工作流（YAML）连接自有数据（如 Hacker News 索引）。通过 pip/PyPI 安装，新增平台只需实现 Chat 子类。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- persona = 聊天代理 + 工作流，平台无关可复用
- 内置 Wikitalk（Wikipedia RAG，回答附引用来源）
- 支持 LLM 与专用小模型混合工作流（摘要/翻译无需 LLM）
- 通过 txtai YAML 工作流接入自有数据构建问答索引

## 适用场景

- 在 Rocket.Chat/Mattermost 内部署本地 AI 问答机器人
- 基于 Wikipedia 或自有数据做带引用来源的 RAG 问答
- 为消息平台定制摘要、翻译等专用助手

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L9: txtchat adds a set of intelligent agents that are available to integrate with messaging platforms. These agents or p
> L41: A persona is a combination of a chat agent and workflow that determines the type of responses. Each agent is tied t

## 星数曲线

```mermaid
xychart-beta
    title "neuml/txtchat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 338 --> 340
    line [339, 339]
```

2026-10-18 339 → 2026-10-24 339（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8fa1607942f0` · [字段定义](../../DATASET.md)*
