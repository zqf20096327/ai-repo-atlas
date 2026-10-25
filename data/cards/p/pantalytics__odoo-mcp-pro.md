# pantalytics/odoo-mcp-pro

⭐ 88 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/pantalytics/odoo-mcp-pro) · [官网](https://www.pantalytics.com/apps/odoo-mcp-server) · 组织维护

**把 Odoo ERP 接入 AI 助手的 MCP 连接器（托管/自托管）**

基于 Model Context Protocol 的 Odoo 连接器：向 Claude、ChatGPT、Cursor 等 MCP 兼容 AI 工具暴露 record_search/get/aggregate/export/create/update/delete 等工具，让用户用自然语言查询和操作 Odoo 业务数据。兼容 Odoo 14-20，自动选择 JSON/2 或 XML-RPC；无状态代理、API 密钥 AES-128 加密。提供 pantalytics.com 托管版（含 OAuth 2.1、多租户）与 pip 安装的自托管版（单租户、环境变量配置、无 OAuth）。双许可：Elastic 2.0 + MPL-2.0，多租户等属商业包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 暴露 12 类 MCP 工具覆盖搜索/聚合/导入导出/增删改
- 兼容 Odoo 14-20，自动选择 JSON/2 或 XML-RPC 协议
- 托管版提供 OAuth 2.1、多租户与加密 API 密钥；自托管版单租户、API key 认证
- 无状态代理设计，权限沿用 Odoo 用户 ACL 与记录规则

## 适用场景

- 用自然语言查询 Odoo 发票、销售单、CRM 等业务数据
- 通过 AI 助手批量创建或更新 Odoo 记录
- 让 Claude/ChatGPT/Cursor 直接读取公司 ERP 数据完成日常操作

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L88: odoo-mcp-pro is an Odoo connector that implements MCP (Model Context Protocol) -- an open standard that lets AI ass
> L24: odoo-mcp-pro is an AI connector for Odoo that uses MCP (Model Context Protocol) -- an open standard that lets AI as

## 星数曲线

```mermaid
xychart-beta
    title "pantalytics/odoo-mcp-pro 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 86 --> 89
    line [87, 88, 88]
```

2026-10-18 87 → 2026-10-25 88（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `42e8846c1954` · [字段定义](../../DATASET.md)*
