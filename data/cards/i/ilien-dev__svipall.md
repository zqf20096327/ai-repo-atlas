# ilien-dev/svipall

⭐ 20 · Rust · AGPL-3.0 · 推送 2026-10-08 · [GitHub](https://github.com/ilien-dev/svipall) · [官网](https://svipall.ilien.dev) · 个人维护

**本地优先的 Rust 网页抓取 MCP 服务器与 CLI，供 AI agent 阅读 Web**

以 Rust 编写的 MCP server + CLI + REST 服务，在用户本机运行：抓取并渲染网页转为 Markdown、在配置限额内整站爬取（llms.txt/CSV 输出、近重复标注、可恢复）、无 API key 的多引擎搜索（DuckDuckGo/Bing/Brave）、从列表页自动推导 schema 输出结构化行、读取 PDF/Office 文件、页面监控与登录会话保持。可尝试本地应对 15 类验证码组件与 12 类墙，无法解决的转入人工面板并如实报告。面向 Claude Code/Cursor 用户与 agent 开发者，无遥测、无第三方付费服务。部分站点仍会拦截，分类为启发式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页转 Markdown、schema:auto 从未知列表页提取类型化行
- 无 API key 的聚合搜索与限额内可恢复整站爬取
- 本地验证码尝试（15 组件族/11 答案形态）与人工面板兜底
- svipall serve 暴露 20 条本地 REST 路由，输出单一 JSON 对象可管道给 jq

## 适用场景

- 让 Claude Code/Cursor 等 agent 以本地方式读取网页与整站文档
- 构建 RAG 语料：站点爬取为 Markdown 并获得质量与近重复标注
- 无 API key 前提下抓取列表/表格数据并导出 CSV
- 监控页面区域变化并在被拦截时得到明确判定

## 场景标签

`网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L1: Svipall, a local-first web scraping and browsing MCP server for AI agents
> L6:  An MCP server and CLI, in Rust, that extracts web pages into Markdown,
> L51: Rust · MCP + CLI + REST · no Node, no Python, no API key · local storage and processing

## 星数曲线

```mermaid
xychart-beta
    title "ilien-dev/svipall 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `79743d8da0f9` · [字段定义](../../DATASET.md)*
