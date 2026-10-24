# tomaspavlin/rohlik-mcp

⭐ 121 · TypeScript · MIT · 推送 2026-03-17 · [GitHub](https://github.com/tomaspavlin/rohlik-mcp) · 个人维护

**让 LLM 在 Rohlik 集团平台购买生鲜杂货的 MCP 服务器**

基于 Model Context Protocol 的服务器，使 AI 助手（如 Claude Desktop）能够通过逆向工程的 Rohlik API 与捷克的 Rohlik.cz、德国 Knuspr.de、奥地利 Gurkerl.at、匈牙利 Kifli.hu、罗马尼亚 Sezamo.ro 交互。提供约 18 个工具：商品搜索、购物车增删查、基于订单历史的餐食建议与常购分析、折扣浏览、订单与配送时段查询等。通过 ROHLIK_BASE_URL 环境变量切换区域，以 npm/npx 方式在 Claude Desktop 配置中接入。作者声明仅供学习与个人用途。

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

- 覆盖 5 个国家站点的 Rohlik Group 生鲜平台（另 2 个站点规划中）
- 约 18 个工具：搜索、购物车、订单历史、配送时段、折扣浏览
- 基于订单历史生成个性化餐食建议与常购商品分析
- 附带 API 校验工具与单元测试（测试 11 个 API 端点）

## 适用场景

- 在 Claude Desktop 中用自然语言完成生鲜下单与购物车管理
- 让 AI 根据我的订单历史推荐餐食或常购商品
- 查询折扣商品与最便宜的配送时段

## 场景标签

 · 领域:电商/生活服务

## 证据(README 行号)

> L8: This is a Model Context Protocol (MCP) server that enables AI assistants to interact with the Rohlik Group's online 
> L52: Add the MCP to Claude Desktop configuration:

## 星数曲线

```mermaid
xychart-beta
    title "tomaspavlin/rohlik-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-24 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6d8270cc9b7f` · [字段定义](../../DATASET.md)*
