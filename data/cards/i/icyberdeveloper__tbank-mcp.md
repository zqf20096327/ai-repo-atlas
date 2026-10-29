# icyberdeveloper/tbank-mcp

⭐ 38 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/icyberdeveloper/tbank-mcp) · 个人维护 · 中文 README

**非官方 T-Bank 移动银行 MCP 服务器：让 agent 操作银行账户**

面向 Claude Code、Codex、ChatGPT、Cursor 等 MCP 客户端的 T-Bank（前 Tinkoff）银行 API 服务器（stdio），提供 90 个工具：账户/卡片/文档查询、转账与缴费、超市买菜下单、电影演出票、火车机票与酒店搜索、银行消息、投资组合等；每个业务垂直配一个 skill，经 tbank 路由 skill 进入。安全机制：密码/PIN 通过本地 CLI 或环境变量登录、不进入 LLM 上下文；支付需客户端支持 MCP elicitation 按钮确认；内置俄罗斯受信根 CA（SHA-256 固定）。工具文档与回复均为俄语。

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

- 90 个银行工具覆盖查询、转账、买菜、购票、差旅、投资等
- 密码/PIN 经本地 CLI 登录，不进入模型上下文
- 支付需 MCP elicitation 客户端按钮确认，不支持则拒绝执行
- 内置俄罗斯受信根 CA 并按 SHA-256 固定，不从网络学习证书

## 适用场景

- 在 Claude Code 等 MCP 客户端里用俄语查询账户与消费记录
- 让 agent 完成转账、缴费、买电影票、订火车票等操作
- 按食谱自动比价组装超市购物车并结账（需浏览器）

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **T-Bank (Т-Банк) MCP** — mobile banking API server for Claude Code, Codex, ChatGPT, and other MCP-capable agents.
> L134: ## Other agents (Codex, ChatGPT, Hermes, OpenClaw)
> L181: Reading works in any MCP client. **Paying needs a client that renders MCP

## 星数曲线

```mermaid
xychart-beta
    title "icyberdeveloper/tbank-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-29"]
    y-axis "stars" 35 --> 39
    line [36, 37, 38, 38]
```

2026-10-18 36 → 2026-10-29 38（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d7188590fad7` · [字段定义](../../DATASET.md)*
