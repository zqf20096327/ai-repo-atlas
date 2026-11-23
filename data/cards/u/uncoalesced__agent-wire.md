# uncoalesced/agent-wire

⭐ 4 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/uncoalesced/agent-wire) · [官网](https://uncoalesced.com/agent-wire) · 个人维护

**让 AI agent 在本机读取网页与 31 个站点并写出引用简报的 MCP 服务器**

一个本地运行的 MCP 服务器，让 AI agent 以紧凑 Markdown 读取网页和 Reddit、X、GitHub、YouTube、Hacker News、arXiv 等 31 个平台频道，并可写出近 30 天的带引用简报。通过四阶段抓取瀑布应对封禁（站点 API、浏览器级 TLS 指纹、镜像/Wayback、本地无头浏览器），按 BM25 与投票权重压缩页面至 token 预算；登录凭据存本地加密保险库，回传内容做隐私擦除；wire_cite 逐一核验引用链接是否有效。通过 uvx 安装，支持 Claude Code/Desktop、Codex、ChatGPT、Gemini、Cursor 等多种客户端，常见场景无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 MCP 服务器读取网页与 31 个平台频道，输出紧凑 Markdown
- 四阶段抓取瀑布（站点 API→TLS 指纹→镜像/Wayback→无头浏览器）
- 本地加密保险库管理登录，隐私擦除并剥离隐藏提示文本
- wire_cite 打开引用链接核验死链与引文缺失，未溯源声明标记 [[UNSOURCED]]

## 适用场景

- 让 agent 查询 Reddit/X 今天在讨论什么话题
- 为某主题生成近 30 天的带引用调研简报
- 将网页与仓库趋势数据作为 Markdown 喂给 agent 绘图或分析
- 在 Claude Code/Codex/Gemini 等客户端中接入实时网络读取工具

## 场景标签

`网页抓取` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L23: agent-wire is an MCP server that lets an AI agent read the live web and 31 platform channels from your own machine 
> L48: agent-wire is one warm async Python process on your machine. Routing, bot walls, logins, privacy scrubbing and comp

## 星数曲线

```mermaid
xychart-beta
    title "uncoalesced/agent-wire 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-11-10", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-29 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0f62cfcc846b` · [字段定义](../../DATASET.md)*
