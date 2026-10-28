# aashari/mcp-server-atlassian-confluence

⭐ 62 · TypeScript · 推送 2026-02-22 · [GitHub](https://github.com/aashari/mcp-server-atlassian-confluence) · 个人维护

**让 AI 助手通过 MCP 访问 Confluence 知识库的服务器**

Node.js/TypeScript 实现的 MCP server，把 Atlassian Confluence 的 REST API（空间/页面/评论/博客/CQL 搜索）以 5 个通用工具（conf_get/post/put/patch/delete）暴露给 Claude Desktop、Cursor 等 AI 助手，另提供镜像同参数的 CLI。凭据通过环境变量、.env 或 ~/.mcp/configs.json 配置，需 Atlassian API Token。默认输出 TOON 格式（自称较 JSON 少 30-60% token），支持 JMESPath 过滤；超约 4 万字符的响应自动截断并将全文存至 /tmp/mcp/。可运行 STDIO 或 HTTP（SSE）两种传输模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个通用工具覆盖 Confluence API 的读写删改
- 默认 TOON 输出格式与 JMESPath 过滤以降低 token 消耗
- 超过约 4 万字符的响应自动截断并保存完整原文到临时文件
- 提供与 MCP 工具同参数的 CLI 及 MCP Inspector 调试方式

## 适用场景

- 在 Claude Desktop / Cursor 中用自然语言查询团队 Confluence 文档
- 通过 AI 助手创建或更新 Confluence 页面与评论
- 在终端直接调用 CLI 访问 Confluence API

## 场景标签

 · 领域:AI 连接器/企业知识库集成

## 证据(README 行号)

> L3: Transform how you access and interact with your team's knowledge by connecting Claude, Cursor AI, and other AI assis
> L101: This MCP server provides 5 generic tools that can access any Confluence API endpoint:

## 星数曲线

```mermaid
xychart-beta
    title "aashari/mcp-server-atlassian-confluence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9e3c062fa640` · [字段定义](../../DATASET.md)*
