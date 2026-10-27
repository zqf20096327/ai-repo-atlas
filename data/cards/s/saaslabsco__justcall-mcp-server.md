# saaslabsco/justcall-mcp-server

⭐ 25 · HTML · MIT · 推送 2026-03-12 · [GitHub](https://github.com/saaslabsco/justcall-mcp-server) · [官网](https://justcall.io) · 组织维护

**让 LLM/agent 通过 MCP 直接打电话、发短信的官方服务器**

JustCall 官方的 MCP Server：以函数调用接口向 LLM 与 AI agent 开放 JustCall 电话能力，提供 66 个工具，覆盖通话管理、SMS、WhatsApp、联系人、预约、分析报表、AI 通话/会议分析、AI 语音外呼及销售拨号器等。通过远程端点 mcp.justcall.host 以 Streamable HTTP 连接，支持 OAuth2（PKCE/S256）与 API key Bearer 认证；README 给出 Claude Desktop、Claude Web、ChatGPT 的连接步骤。需 JustCall 账号与 API 凭证，请求受 API key 速率限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 66 个 MCP 工具：通话、SMS、WhatsApp、联系人、预约、分析等
- 支持 AI 语音 agent 外呼与通话/会议 AI 分析检索
- OAuth2（授权码+PKCE，S256）与 Bearer token 认证
- Streamable HTTP 远程连接，可接入任意 MCP 客户端

## 适用场景

- 让 Claude/ChatGPT 等客户端直接发起和管理真实电话与短信
- AI 销售外呼场景中查询/创建拨号器活动与联系人
- 在对话中检索通话转写、摘要与分析数据

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: The JustCall Model Context Protocol (MCP) Server lets Large Language Models (LLMs) and AI agents make real-world voi
> L9: - ⚙️ Seamless integration: Use the MCP standard to connect JustCall’s telephony capabilities with any LLM runtime or

## 星数曲线

```mermaid
xychart-beta
    title "saaslabsco/justcall-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3730ea72f753` · [字段定义](../../DATASET.md)*
