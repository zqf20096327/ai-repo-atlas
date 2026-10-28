# damientilman/mailchimp-mcp-server

⭐ 24 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/damientilman/mailchimp-mcp-server) · [官网](https://www.tilman.marketing) · 个人维护

**面向 Mailchimp Marketing API 的 MCP 服务器：227 个工具供 AI 客户端调用**

通过 Model Context Protocol 向任意 MCP 兼容客户端（Claude Desktop、Cursor、Cline 等）暴露 227 个 Mailchimp 工具，覆盖邮件营销活动的读与写、受众与成员管理、细分与标签、自动化流程、报表分析、电商（店铺/订单/促销）、落地页、调查、文件管理等。基于 requests 直接调用 Marketing API 而非官方 Python 客户端。安全机制包括按工具的 read/write/destructive 风险分级元数据、只读模式、干跑模式、结构化 JSON 审计日志与参数校验；支持多账户密钥与工具子集加载以压缩 token 占用。需 Python 3.10+ 与 Mailchimp API key，提供 uvx/pip/Docker 三种安装运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 227 个工具覆盖 Mailchimp 营销与电商 API 的读写全表面
- 每工具 read/write/destructive 风险分级，经 MCP 注解与 describe_tools 暴露
- 只读/干跑/审计三种运行时安全模式与参数契约校验
- 多账户支持与 MAILCHIMP_TOOLS 子集加载（约 63k token 可压缩至约 29k）

## 适用场景

- 在 Claude Desktop 或 Cursor 等客户端中用自然语言查询营销报表与受众数据
- 让 AI 助手代为创建、排期与发送邮件营销活动（可开干跑预览）
- 同一服务端管理多个 Mailchimp 账户并分别设置只读/可写策略
- 配合外部 MCP 网关按风险分级执行调用策略与审计

## 场景标签

 · 领域:营销自动化/AI 工具接入

## 证据(README 行号)

> L11: The most complete Model Context Protocol (MCP) server for the Mailchimp Marketing API: **227 tools** to query and m
> L29: Add it to your MCP client (Claude Desktop, Cursor, Cline, …):
> L159: The server is designed for defense-in-depth alongside an external MCP gateway: it owns the *semantics* (which tool

## 星数曲线

```mermaid
xychart-beta
    title "damientilman/mailchimp-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `23465f10d0e1` · [字段定义](../../DATASET.md)*
