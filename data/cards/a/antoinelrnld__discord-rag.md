# antoinelrnld/discord-rag

⭐ 28 · Python · MIT · 推送 2026-02-05 · [GitHub](https://github.com/antoinelrnld/discord-rag) · 个人维护

**基于个人 Discord 消息记录构建 RAG 问答应用与机器人**

提供一套 Docker Compose 编排的流水线：从 Discord 频道导出消息存入 MongoDB，用 SemanticChunking 策略切分并生成向量存入 ChromaDB，再启动检索增强生成 API（/invoke 返回基于消息上下文的回答），并附带可在 Discord 服务器内用 /ask 命令对话的机器人。调用 OpenAI API 生成回答，系统提示支持英/法两种语言。项目自述处于早期原型阶段，实时数据摄取尚未实现。面向想在自有服务器部署的个人用户与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 消息导出→MongoDB→语义分块索引→ChromaDB 的完整数据流水线
- 提供 /invoke 与 /health 两个 API 端点，返回检索上下文与生成回答
- Discord 机器人通过 /ask 命令在服务器内直接问答
- Docker Compose 一条命令启动全部服务

## 适用场景

- 用 LLM 回答关于自己 Discord 群历史消息的问题
- 为社区服务器部署了解群聊上下文的问答机器人
- 对过往聊天记录做总结或检索式提问

## 场景标签

`RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This repo aims to provide a simple and fast way to create a RAG (Retrieval-Augmented Generation) application based o
> L70: We are now ready to launch the API that will allow us to interact with the model. The API receives a prompt from th

## 星数曲线

```mermaid
xychart-beta
    title "antoinelrnld/discord-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81719c7f5900` · [字段定义](../../DATASET.md)*
