# Rayyan9477/linkedin_mcp

⭐ 28 · Python · 推送 2026-03-15 · [GitHub](https://github.com/Rayyan9477/linkedin_mcp) · 个人维护

**让 AI 助手操作 LinkedIn 的 MCP 服务器：求职搜索与文档生成**

基于官方 MCP Python SDK（FastMCP）构建的 LinkedIn MCP 服务器，向 Claude Desktop / Claude Code 等 AI 助手暴露 13 个工具：带过滤条件的职位搜索、个人资料与公司页获取、AI 简历与求职信生成（3+2 套模板，HTML/Markdown/PDF 输出）、本地求职申请状态跟踪（六种状态流转）。需配置 LinkedIn 账号凭据，AI 功能依赖可选的 Anthropic API key，无 key 时核心 LinkedIn 功能仍可用。异步架构、服务层缓存，含 Jinja2 沙箱与 SSRF 防护等安全设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个 MCP 工具覆盖职位搜索、资料获取、简历/求职信生成、申请跟踪
- 简历 3 套模板、求职信 2 套模板，输出 HTML/Markdown/PDF
- AI 功能可选：无 Anthropic key 时核心 LinkedIn 功能仍可用
- 安全设计：Jinja2 沙箱、SSRF 防护、路径遍历防护、凭据脱敏

## 适用场景

- 让 AI 助手按关键词、地点、远程等条件搜索 LinkedIn 职位
- 从我的 LinkedIn 资料生成针对特定职位的简历和求职信
- 跟踪我的求职申请进度（applied/interviewing/offered 等）
- 分析我的 LinkedIn 主页并获得优化建议

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: An MCP server that gives AI assistants full access to LinkedIn — search jobs, view profiles and companies, generate 
> L53: **With Claude Desktop** — add to your `claude_desktop_config.json`:
> L123: - **Official MCP SDK** — Uses `FastMCP` with `@mcp.tool()` decorators, not a custom protocol implementation

## 星数曲线

```mermaid
xychart-beta
    title "Rayyan9477/linkedin_mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b7a9ebf6f7bd` · [字段定义](../../DATASET.md)*
