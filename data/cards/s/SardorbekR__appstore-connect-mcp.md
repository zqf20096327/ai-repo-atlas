# SardorbekR/appstore-connect-mcp

⭐ 22 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/SardorbekR/appstore-connect-mcp) · 个人维护

**让 Claude/Cursor 等 MCP 客户端直接管理 App Store Connect 的服务器**

面向 Apple App Store Connect API 的 Model Context Protocol 服务器，供 Claude Desktop、Cursor、VS Code Continue 等 MCP 客户端调用。提供 1,303 个 API 操作的通用访问（经 Apple OpenAPI 规格校验），覆盖版本提交、TestFlight、截图上传、评论回复、定价与 PPP、订阅与内购、分析报表等功能。通过 npx 或 npm 全局安装运行，需配置 .p8 密钥等 Apple API 凭据，使用 ES256 JWT 认证，支持只读模式与按工具组裁剪暴露面。

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

- asc_api_request 可调用全部 1,303 个 App Store Connect API 操作
- 覆盖 TestFlight、截图、定价 PPP、订阅、内购、分析报表等工具集
- ES256 JWT 认证与自动 token 刷新，日志中凭证脱敏
- 只读模式（ASC_READ_ONLY）与按工具组（ASC_TOOLSETS）裁剪暴露面

## 适用场景

- 在 Claude 或 Cursor 中直接编辑 App Store 版本信息并提交审核
- 通过对话管理 TestFlight 测试组与测试员
- 用 AI 助手设置分地区定价、管理订阅与内购
- 让客户端拉取应用分析与销售报表

## 场景标签

 · 领域:移动应用发布/开发者工具

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server for Apple's App Store Connect API. Manage your iOS, macOS, tvOS, and visionOS 
> L40: 2. Add the server to your MCP client with `npx -y asc-mcp@latest` and your credentials (see MCP Client Configuratio

## 星数曲线

```mermaid
xychart-beta
    title "SardorbekR/appstore-connect-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b763aad2e73a` · [字段定义](../../DATASET.md)*
