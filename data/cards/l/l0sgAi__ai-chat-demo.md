# l0sgAi/ai-chat-demo

⭐ 14 · Java · MIT · 推送 2026-09-16 · [GitHub](https://github.com/l0sgAi/ai-chat-demo) · 个人维护 · 中文 README

**SpringBoot + SpringAI 的 LLM 聊天机器人全栈项目**

基于 SpringAI + SpringBoot3 的多用户 AI 聊天机器人项目，前后端分离。功能含 MySQL 持久化、sa-token 登录注册（Redis 存 token）、会话与问答对、对话记忆与上下文、虚拟线程异步对话、以 ElasticSearch 8.15.5 作向量存储的 RAG，以及 MCP 工具调用（需拉取 mcp-server 分支）。仅支持 OpenAI 标准 API。配置中心、全局搜索、RabbitMQ 优化为待实现项。运行需 Node.js、Java 21+、Redis、MySQL8、ES，管理员账户需手动改数据库 role 字段创建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多用户聊天会话与问答对，支持对话记忆与上下文
- ElasticSearch 向量存储实现 RAG
- 虚拟线程异步对话，遵循 OpenAI 标准 API
- 支持 MCP 工具调用（mcp-server 分支）

## 适用场景

- 部署一个自托管的 LLM 聊天服务
- 作为 SpringAI + RAG 的学习/参考项目
- 通过管理后台配置多个模型供多用户使用

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L5: ### An AI large language model chatbot project
> L21: **Built with `SpringAI` + `SpringBoot` + `MySQL` + `Redis` + `ES`. Main features:**

## 星数曲线

```mermaid
xychart-beta
    title "l0sgAi/ai-chat-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3dcf2b199f77` · [字段定义](../../DATASET.md)*
