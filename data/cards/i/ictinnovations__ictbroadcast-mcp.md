# ictinnovations/ictbroadcast-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ictinnovations/ictbroadcast-mcp) · [官网](https://ictbroadcast.com) · 组织维护

**ICTBroadcast 的 MCP 服务器：让 AI 助手监控语音/SMS/传真外呼活动**

为 ICTBroadcast 语音、短信、传真广播与呼叫中心平台提供的 Model Context Protocol 服务器。AI 助手可通过它列出外呼活动、查询运行状态、读取汇总与单次呼叫结果；默认只读，仅在设置 ICTBROADCAST_MCP_ALLOW_WRITE=true 时才注册启动/停止活动工具。通过 ICTBroadcast 的 form-encoded REST API 连接，凭账号用户名与密码认证，无需单独令牌。需 Node.js 18 或更高版本，支持 npx 直接运行或全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读工具集：列出活动、查询状态、读取汇总与单呼结果
- 写操作（启动/停止外呼）默认不注册，需显式开启
- 通过 REST API 以账号密码认证，无需单独令牌
- npx 免安装运行或 npm 全局安装

## 适用场景

- 让 AI 助手实时监控我的外呼活动状态与呼叫结果
- 在确认成本风险后，通过对话启动或停止外呼活动
- 在 Claude Desktop 等 MCP 客户端中接入 ICTBroadcast

## 场景标签

 · 领域:通信/呼叫中心自动化

## 证据(README 行号)

> L3: A Model Context Protocol server for
> L7: It lets an AI assistant monitor outbound campaigns — list them, check status, read

## 星数曲线

```mermaid
xychart-beta
    title "ictinnovations/ictbroadcast-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8152798db331` · [字段定义](../../DATASET.md)*
