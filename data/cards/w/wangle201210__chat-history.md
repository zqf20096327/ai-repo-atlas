# wangle201210/chat-history

⭐ 20 · Go · Apache-2.0 · 推送 2025-11-12 · [GitHub](https://github.com/wangle201210/chat-history) · 个人维护 · 中文 README

**为 Eino 框架补齐聊天历史记录存储，支持多轮对话管理**

Go 语言库，为字节开源的 Eino 大模型应用框架提供聊天历史记录管理能力：通过 NewEinoHistory 以 MySQL DSN 初始化，在 Eino 原有构建 messages 与返回消息的代码位置插入少量代码，即可持久化与读取对话历史，从而支持多轮对话及对话管理。以 go get 方式安装，参照 example 目录接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 Eino 框架提供其未内置的聊天历史记录功能
- 通过 MySQL DSN 初始化 EinoHistory
- 在现有 messages 构建与返回处少量插入代码即可接入

## 适用场景

- 我在用 Eino 做大模型应用，需要补上多轮对话的历史记录
- 基于 MySQL 持久化管理对话记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: 目前eino提供了快捷接入大模型的方法但是聊天历史记录的功能没有提供，导致没法进行对轮对话，及对话管理
> L13: var eh = eino.NewEinoHistory("root:123456@tcp(127.0.0.1:3306)/chat_history")

## 星数曲线

```mermaid
xychart-beta
    title "wangle201210/chat-history 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `95179780b5e5` · [字段定义](../../DATASET.md)*
