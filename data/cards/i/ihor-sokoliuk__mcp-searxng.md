# ihor-sokoliuk/mcp-searxng

⭐ 1,395 · TypeScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ihor-sokoliuk/mcp-searxng) · [官网](https://www.npmjs.com/package/mcp-searxng) · 个人维护

**让 AI 助手通过自托管 SearXNG 进行隐私网络搜索的 MCP 服务器**

一个 MCP 服务器，接入 SearXNG API，为 Claude、Cursor 等 MCP 客户端提供网络搜索能力。提供四个工具：网页搜索（分页/过滤）、搜索建议、实例能力检查、URL 读取（HTML/结构化文本/有界 PDF 文本）。支持 STDIO 与 Streamable HTTP 两种传输，可选缓存、代理、副本故障转移与 OAuth 保护。要求使用者自备已开启 JSON 输出的 SearXNG 实例；自身不安装 SearXNG，隐私取决于所连实例的部署方式。MIT 许可，通过 npm 与 Docker 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 searxng_web_search、web_url_read 等 4 个 MCP 工具
- 支持 STDIO 与 Streamable HTTP 传输，可选静态 bearer 或 OAuth 鉴权
- 支持副本列表故障转移、HTML fallback、缓存与代理
- npm（npx）与 Docker 两种官方分发方式

## 适用场景

- 为 Claude Desktop、Cursor 等 MCP 客户端添加网页搜索工具
- 通过自托管 SearXNG 控制搜索查询的流向
- 让 AI 助手读取指定 URL 的网页或 PDF 内容

## 场景标签

`AI 助手` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L15: An MCP server that integrates the SearXNG API, giving AI assistants web search capabilities.
> L97: `MCP client → mcp-searxng → SearXNG → search engines`

## 星数曲线

```mermaid
xychart-beta
    title "ihor-sokoliuk/mcp-searxng 星数(近 24 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 1323 --> 1401
    line [1329, 1331, 1334, 1338, 1340, 1342, 1343, 1329, 1351, 1358, 1359, 1358, 1366, 1369, 1372, 1375, 1376, 1379, 1380, 1378, 1381, 1385, 1388, 1395]
```

2026-10-26 1,329 → 2026-11-28 1,395（+66）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `662c889ae600` · [字段定义](../../DATASET.md)*
