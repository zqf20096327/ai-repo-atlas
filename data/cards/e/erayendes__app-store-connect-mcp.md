# erayendes/app-store-connect-mcp

⭐ 53 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/erayendes/app-store-connect-mcp) · [官网](https://npmjs.com/package/@erayendes/asc-mcp) · 个人维护

**为 AI 客户端提供 App Store Connect 全量 API 的本地 MCP 服务器**

基于 Apple OpenAPI 规范生成的 MCP 服务器，覆盖 App Store Connect API 与 App Store Server API（StoreKit 2），提供 13 个 profile、33 个子 profile、共 928 个工具（剔除 123 个已废弃操作，888 个生成工具加 40 个手写工具），用户可按需选择 profile。本地运行：从 macOS Keychain 读取 App Store Connect 密钥并签发短期令牌直连 Apple。对改价、删除、发布等不可逆操作默认要求确认。可通过 npx 一条命令完成安装向导，需 Node.js 20.19+。作者以个人身份在业余时间维护，MIT 许可。

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

- 从 Apple OpenAPI 规范生成 928 个工具，覆盖 13 个 profile（TestFlight、订阅、定价、评论、Xcode Cloud 等）
- 本地运行，密钥存于 Keychain，签发短期令牌直连 Apple
- 高风险变更（定价、删除、发布、外部测试）默认确认后才执行
- npx 一条命令安装向导，含密钥配置与 profile 选择

## 适用场景

- 让 Claude/Codex/Cursor 等 AI 客户端直接操作我的 App Store Connect 账户
- 用对话方式汇总商店评论、查询各国订阅价格
- 通过 AI 完成版本送审、TestFlight 分组等日常操作

## 场景标签

 · 领域:iOS/macOS 开发者工具

## 证据(README 行号)

> L33: One MCP server for the **App Store Connect API** and the **App Store Server API (StoreKit 2)**, built from Apple's 
> L45: ### Runs on your machine

## 星数曲线

```mermaid
xychart-beta
    title "erayendes/app-store-connect-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `94facbafe33a` · [字段定义](../../DATASET.md)*
