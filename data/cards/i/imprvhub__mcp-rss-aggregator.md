# imprvhub/mcp-rss-aggregator

⭐ 27 · TypeScript · MPL-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/imprvhub/mcp-rss-aggregator) · 个人维护

**让 Claude Desktop 聚合阅读 RSS 订阅的 MCP 服务器**

面向 Claude Desktop 用户的 Model Context Protocol 服务器：读取本地 OPML 或 JSON 格式的订阅源配置，按分类组织 RSS 订阅，向 Claude 提供 rss_list、rss_latest、rss_feed 三个工具，用于列出订阅源、跨源获取最新文章或按单源过滤获取。文章内容在本地读取和格式化，不外发。安装方式为 Smithery CLI 或 git clone 后 npm 构建运行，需 Node.js 20 以上；可作为 Claude Desktop 子进程自动启动。0.3.0 起订阅路径改由 RSS_FEEDS_PATH 环境变量指定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 rss_list/rss_latest/rss_feed 三个参数化工具
- 支持 OPML 导入与 JSON 自定义订阅配置，按分类组织
- 文章在本地读取与格式化，内容不离开本机
- 支持 Smithery CLI 安装与 Claude Desktop 子进程自动启动

## 适用场景

- 在 Claude Desktop 中用自然语言浏览我的 RSS 订阅最新文章
- 导入现有 RSS 阅读器的 OPML 订阅继续在 Claude 中阅读
- 让 Claude 汇总、比较多个新闻源对同一事件的报道

## 场景标签

 · 领域:AI 客户端工具/信息聚合

## 证据(README 行号)

> L9:  An integration that allows Claude Desktop to fetch and read content from your favorite RSS feeds using the Model Co
> L169: 2. Ask Claude for your feeds in plain language; it will pick the right tool

## 星数曲线

```mermaid
xychart-beta
    title "imprvhub/mcp-rss-aggregator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2a637d25509b` · [字段定义](../../DATASET.md)*
