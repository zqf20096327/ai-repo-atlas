# zoharbabin/web-researcher-mcp

⭐ 70 · Go · MIT · 推送 2026-10-25 · [GitHub](https://github.com/zoharbabin/web-researcher-mcp) · [官网](https://zoharbabin.com/web-researcher-mcp/) · 个人维护

**给 AI 助手提供带真实引用的网络研究能力的 MCP 服务器**

用 Go 编写并以预编译二进制分发的 MCP 服务器（含 PyPI wheel、Homebrew、安装脚本与 Docker），为 Claude、Cursor、VS Code、LM Studio 等支持工具调用的 AI 助手提供 37 个研究工具：网页/学术/专利/SEC/法院/临床试验等多源搜索、全文抓取（网页/PDF/Word/YouTube）、引用核验与书目审计（APA/MLA/BibTeX 等格式）。核心机制是“search lenses”——可限定 AI 只检索指定可信站点；默认零配置路径用 DuckDuckGo 搜索（无需 API key），部分工具需配置对应 key。查询在本地运行并留有可复现的检索日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 37 个研究工具：网页/学术/专利/SEC/法院/临床等多源搜索与全文抓取
- search lenses 可将检索限定在指定可信站点
- 引用核验、书目整体审计与 Wayback 存档工具
- 默认 DuckDuckGo 路径无需 API key，附带一键式 prompt 模板

## 适用场景

- 让 Claude/Cursor 等 AI 助手检索并引用真实可核验的来源
- 限定 AI 只从医学期刊、法院数据库等可信站点取材
- 提交前批量审计参考文献中的失效或不可核验引用

## 场景标签

`科研工具` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L21:  web-researcher-mcp MCP server
> L104: Works with Claude, Claude Desktop, Cursor, and any AI assistant that supports tool use.
> L127: ## What your AI can do with this

## 星数曲线

```mermaid
xychart-beta
    title "zoharbabin/web-researcher-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-25 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3f6d351cb1cd` · [字段定义](../../DATASET.md)*
