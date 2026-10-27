# Vishisht16/Humane-Proxy

⭐ 27 · Python · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/Vishisht16/Humane-Proxy) · 个人维护

**拦截自残与犯罪意图提示的 LLM 安全中间件**

部署在用户与任意 LLM 之间的 Python 安全中间件：消息经过 3 级级联检测（关键词启发式、语义嵌入、推理 LLM 如 OpenAI Moderation/LlamaGuard），命中自残意图时阻断并返回含 10+ 国家危机热线的关怀回复，犯罪意图则阻断或标记，均通过 Slack/Discord/PagerDuty 等通知运营者；默认不存储原始消息，仅存 SHA-256 哈希。可作为 Python 库、独立服务或 MCP server 供 Claude Desktop、Cursor 等 agent 使用，附会话级风险轨迹与按会话限流的告警。明确不处理越狱与提示注入。

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

- 3 级级联检测管线：启发式 <1ms、嵌入、推理 LLM
- 自残命中时返回多国危机热线关怀回复并告警运营者
- 可作为 Python 库或 MCP server 集成到 agent
- 默认不存原始消息，仅存 SHA-256 哈希，支持删除会话

## 适用场景

- 在客服或陪伴类 LLM 应用上线前拦截自残意图并触发人工介入
- 为 Claude Desktop/Cursor 等 agent 挂载消息安全检查工具
- 满足 GDPR/HIPAA 场景下的审计与被遗忘权要求

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: HumaneProxy sits between your users and any LLM. When someone expresses self-harm ideation or criminal intent, it in
> L18: User message → HumaneProxy → (safe?) → Upstream LLM → Response
> L62: ## How it works

## 星数曲线

```mermaid
xychart-beta
    title "Vishisht16/Humane-Proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 26 --> 29
    line [28, 27, 27]
```

2026-10-18 28 → 2026-10-27 27（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a9f42c30eab7` · [字段定义](../../DATASET.md)*
