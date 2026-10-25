# fingentic/revolut-mcp

⭐ 34 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/fingentic/revolut-mcp) · [官网](https://fingentic.github.io/revolut-mcp/) · 组织维护

**连接 AI 助手与 Revolut Business API 的 MCP 服务器**

Model Context Protocol 服务器，桥接 Claude、Cursor 等 AI 助手与 Revolut Business API。助手可通过自然语言查询账户与余额、浏览交易、管理交易对手、查汇率、转账等，提供按八个作用域组织的 21 个工具。仅支持 Revolut Business 账户，不支持个人账户、RevolutX/crypto 或 Merchant API；默认沙箱环境，需设置生产证书才能连接真实账户。安装途径为 npm、源码或 Docker，采用 MIT 许可。

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

- 21 个工具按八个作用域组织
- 覆盖账户、交易、交易对手、汇率与转账操作
- 默认沙箱环境，可通过证书切换到生产环境
- 提供 npm / 源码 / Docker 三种安装途径

## 适用场景

- 让 Claude 等 AI 助手自然语言查询公司账户余额与交易
- 通过对话管理 Revolut Business 的交易对手
- 查询实时汇率并发起转账

## 场景标签

 · 领域:金融科技/Agent 工具服务

## 证据(README 行号)

> L12: Revolut MCP is a Model Context Protocol server that bridges AI
> L13: assistants (Claude, Cursor, etc.) and the **Revolut Business API**. Through natural-language requests

## 星数曲线

```mermaid
xychart-beta
    title "fingentic/revolut-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e26acac70555` · [字段定义](../../DATASET.md)*
