# lmcc-dev/mult-fetch-mcp-server

⭐ 15 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/lmcc-dev/mult-fetch-mcp-server) · 组织维护 · 中文 README

**供 AI 助手抓取网页内容的 MCP 服务器：多格式/分块/代理**

基于官方 MCP SDK 实现的 Stdio 传输服务器，向 Claude Desktop、Cursor 等 MCP 客户端提供 fetch 工具：默认 HTTP 抓取并用 Readability 提取正文，输出 Markdown/HTML/JSON/纯文本/原始文本五种格式，超长内容按 maxChars/maxBytes 分块并用 cursor 续取。可选安装 Puppeteer 以无头浏览器渲染页面，支持代理参数、环境变量与系统代理检测。每个请求（含重定向）均做回环/私网/云元数据地址检查以防 SSRF。界面中英双语，可经 MCP_LANG 或系统语言切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 fetch 工具支持 5 种输出格式，超长内容自动分块并支持 cursor 续取
- 可选无头浏览器模式（Puppeteer + stealth 插件）渲染需 JS 的页面
- 请求前 SSRF 地址检查（回环/私网/云元数据等），浏览器模式同样生效
- 代理支持三种途径：请求参数、环境变量、系统代理检测

## 适用场景

- 让 Claude/Cursor 等 AI 助手在对话中抓取并阅读网页
- 分块获取超长网页内容供模型处理
- 在代理网络环境下让 AI 助手访问外部网页

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L21: This project implements an MCP-compliant client and server for communication between AI assistants and external too
> L107: - Implementation based on the official MCP SDK

## 星数曲线

```mermaid
xychart-beta
    title "lmcc-dev/mult-fetch-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0247af6d0518` · [字段定义](../../DATASET.md)*
