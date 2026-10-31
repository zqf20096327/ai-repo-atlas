# iOSDevSK/mcp-for-woocommerce

⭐ 15 · PHP · GPL-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/iOSDevSK/mcp-for-woocommerce) · [官网](https://mcpforwoocommerce.com) · 个人维护

**WooCommerce 商店的 MCP 服务器插件：向 AI 客户端只读暴露商品数据**

基于 Automattic 官方 WordPress MCP 实现的社区 WordPress 插件，将 WooCommerce 商店转为 MCP 数据源：通过 Streamable HTTP（JSON-RPC 2.0）与 STDIO 式（WordPress REST）两种传输暴露商品、分类、标签、属性、评论、配送、税率及 WordPress 内容。全部工具为只读（registry 拒绝非 read 类型），不涉及订单、客户或用户数据，无需登录认证（1.3.0 已移除 JWT/OAuth）。提供 40 余个只读工具、后台开关 UI 与 STDIO 本地代理脚本，兼容 Claude、VS Code、MCP Inspector 等客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全部工具只读，注册表仅接受 read 类型，不暴露订单/客户/用户数据
- Streamable HTTP（JSON-RPC 2.0）与 STDIO 式双传输端点
- 商品与变体均含 permalink 字段，支持自然语言多条件商品搜索
- 后台提供 MCP 主开关与逐工具开关的 React 管理 UI

## 适用场景

- 把 WooCommerce 商店商品目录接入 Claude/VS Code 等 MCP 客户端
- 在网站上部署基于目录数据的 AI 购物助手，回答附商品链接
- 让 AI 客户端以只读方式查询商品、评论、配送与税率信息

## 场景标签

 · 领域:电商/AI 接口

## 证据(README 行号)

> L5: **Connect your WooCommerce store to AI assistants like Claude and VS Code.** This WordPress plugin enables AI client
> L33: - Streamable HTTP transport (JSON-RPC 2.0) — recommended
> L215: A server implementation of the Model Context Protocol that exposes WooCommerce and WordPress data to MCP clients (

## 星数曲线

```mermaid
xychart-beta
    title "iOSDevSK/mcp-for-woocommerce 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2ddacf02c96b` · [字段定义](../../DATASET.md)*
