# tobyandrews1985/basketeer

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/tobyandrews1985/basketeer) · 个人维护

**自动化个人 Tesco 网购账户的 TypeScript SDK（含 MCP/CLI）**

面向个人 Tesco（英国）账户的非官方纯 HTTP TypeScript SDK：直连其 GraphQL 网关，提供目录搜索、商品与营养数据（宏量+微量营养素类型化并可按营养过滤排序）、购物篮、配送时段预订、订单全生命周期操作；checkout 只返回支付 URL 不代付。登录需真实浏览器（Playwright 可选依赖）绕过 Akamai 防护，其余数据面为纯 fetch，限速 1 req/s。附带 CLI、stdio MCP 服务器（供 Claude 等 MCP 客户端调用，含只读/破坏性标注与两步确认）、75 个测试。限制：仅 UK 网关、v0.1 预发布、逆向工程无官方契约，session 明文存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 营养数据类型化为宏量+微量营养素，支持按蛋白/糖等过滤与排序搜索
- 完整订单生命周期：预订/修改/取消/重新下单，checkout 止于支付 URL
- stdio MCP 服务器供 AI agent 购物，破坏性工具带两步确认 token
- 数据面纯 fetch 无第三方依赖，限速 1 req/s，429/403 硬停

## 适用场景

- 用代码或命令行跑完每周采购：搜索、加购、订时段、下单
- 让 Claude 等 MCP 客户端代为操作购物流程（支付留给人工）
- 按营养指标（如蛋白≥10g、糖≤7g）搜索排序商品

## 场景标签

 · 领域:电商自动化/超市购物

## 证据(README 行号)

> L29: - **Agent-ready.** A stdio MCP server lets Claude or any MCP client run the shop. Read-only and destructive tools a
> L137: A stdio MCP server ships as the `basketeer-mcp` bin, exposing tools (`basketeer_search`, `basketeer_search_by_nutr

## 星数曲线

```mermaid
xychart-beta
    title "tobyandrews1985/basketeer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `10ec45dbc3a8` · [字段定义](../../DATASET.md)*
