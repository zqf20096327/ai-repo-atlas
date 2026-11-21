# Replyze/ai-customer-support-agent

⭐ 19 · Python · MIT · 推送 2026-11-13 · [GitHub](https://github.com/Replyze/ai-customer-support-agent) · [官网](https://replyze.chat/?utm_source=github&utm_medium=referral&utm_campaign=ai-customer-support-agent) · 组织维护

**基于 Markdown 文档带引用作答并可转人工的客服 AI agent**

用 Python 编写的自托管 AI 客服 agent 参考实现：仅从用户提供的 Markdown 帮助文档检索作答并引用所依据的小节，通过官方 anthropic SDK 调用 Claude，检索用无依赖的 BM25 实现（无向量数据库）。每轮返回符合 JSON schema 的结构化决策（answer/ask/handoff），规则层在模型调用前捕获退款、纠纷、法律、账户安全等必转人工情形，守卫层校验引用与数字/链接/邮箱，无出处的回答不会被发送。附 37 个评测用例与 CLI、Python API、HTTP 端点三种使用方式，支持无 API key 的离线 stand-in 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅从 Markdown 文档作答，每条回答附小节级引用
- 规则+模型+守卫三层转人工机制（退款/纠纷/法律/重复失败等）
- BM25 检索零依赖实现，支持无 key 离线模式
- 内置 37 个评测用例，可设通过率阈值用于 CI 门禁

## 适用场景

- 在自己的帮助文档上搭建带引用的可审计客服问答
- 需要明确转人工规则的客服自动化场景
- 学习可读性优先的 agent 参考实现并做适配

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L9: A small, readable Python reference implementation of an AI customer support agent. It answers only from a folder of 
> L67: 1. **Rules** (`rules.py`) catch the cases that always go to a person, with regular expressions, before any model ca

## 星数曲线

```mermaid
xychart-beta
    title "Replyze/ai-customer-support-agent 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-21"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-11-18 19 → 2026-11-21 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `6b10cf34ae98` · [字段定义](../../DATASET.md)*
