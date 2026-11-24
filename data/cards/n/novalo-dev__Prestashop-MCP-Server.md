# novalo-dev/Prestashop-MCP-Server

⭐ 3 · PHP · AFL-3.0 · 推送 2026-11-22 · [GitHub](https://github.com/novalo-dev/Prestashop-MCP-Server) · [官网](https://github.com/novalo-dev/Prestashop-MCP-Server/wiki) · 组织维护

**把 PrestaShop 店铺变成 MCP 服务器的免费模块**

面向 PrestaShop 8.0–9.x 的免费开源模块，将店铺转为远程 MCP 服务器，使 Claude、ChatGPT、Mistral、Cursor 等支持 OAuth 的助手可通过 MCP 调用订单、目录、库存、客户、统计、SEO 等工具；内置后台聊天支持自选模型 key 或经 O'So AI Relay 使用本地模型。权限机制：助手继承连接员工的后台权限，写入操作标记并需用户批准，连接经 OAuth 2.1 与邮件验证码，提供 compact 模式以六个搜索/运行工具替代完整工具列表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AFL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MCP 协议接入多类助手（网页端、CLI、代码编辑器、自动化平台）
- 按员工权限控制助手能力，写入操作需批准并记录拒绝日志
- 内置后台聊天，支持多模型 key 或 Ollama/LM Studio 本地运行
- compact 模式以 6 个工具（搜索+读写运行器）压缩工具列表

## 适用场景

- 让 AI 助手查询和更新订单状态、检查库存
- 让 AI 审计并修改商品页 SEO 元信息
- 多店环境下按员工权限安全地授权助手操作
- 在后台聊天中用多个角色化 agent 分工处理不同业务

## 场景标签

 · 领域:电商/AI 工具接入

## 证据(README 行号)

> L108: Your shop becomes a remote MCP server: an assistant you already use connects
> L21: **Talk to your PrestaShop shop from Claude, ChatGPT or the assistant built into your back office.**

## 星数曲线

```mermaid
xychart-beta
    title "novalo-dev/Prestashop-MCP-Server 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `d4d30b2cdcd6` · [字段定义](../../DATASET.md)*
