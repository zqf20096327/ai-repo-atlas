# n1byn1kt/apitap

⭐ 130 · TypeScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/n1byn1kt/apitap) · [官网](https://www.apitap.io) · 个人维护

**把任意网站转为 API 供 AI agent 调用的 CLI/MCP/npm 库**

面向 AI agent 开发者与 MCP 客户端用户：通过 CDP 捕获网站真实流量、自动探测框架 OpenAPI 或从 APIs.guru 目录导入，生成签名可移植的 skill 文件（端点 JSON 映射），再用 fetch() 直接重放请求，无需浏览器与 DOM。凭据存加密存储、重放时注入，不入 skill 文件；每个端点带置信度与可重放性分级。提供 12 个工具的 MCP 服务器、文本模式浏览（peek/read，内置 7 种站点解码器）与 --max-bytes 响应大小上限。需 Node.js 20+，capture/browse 需可选安装 Playwright Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种 API 知识获取路径：CDP 捕获/自动发现/导入 APIs.guru 2,500+ OpenAPI 规范
- skill 文件 HMAC 签名，凭据加密存储并在重放时注入
- 12 个工具的 MCP 服务器，支持 Claude Desktop/Cursor/Windsurf/VS Code Copilot
- 文本模式 peek/read 内置 7 种站点解码器，83 个测试域名平均节省 74% token

## 适用场景

- 让 AI agent 不开浏览器直接调用网站内部 API
- 从已运行的 Chrome 会话捕获带登录态的 API 流量
- 快速导入公开 API 规范建立本地端点知识库
- 以低 token 成本让 agent 读取 Reddit/Wikipedia 等站点内容

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: **The CLI, MCP server, and npm library that turns any website into an API — no docs, no SDK, no browser.**
> L259: ApiTap includes an MCP server with 12 tools for Claude Desktop, Cursor, Windsurf, and other MCP-compatible clients

## 星数曲线

```mermaid
xychart-beta
    title "n1byn1kt/apitap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-26 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `81ed2f035e1c` · [字段定义](../../DATASET.md)*
