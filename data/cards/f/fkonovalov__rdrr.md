# fkonovalov/rdrr

⭐ 194 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/fkonovalov/rdrr) · [官网](https://rdrr.app) · 个人维护

**把网页转为干净 Markdown 供 AI agent 阅读的 CLI/库/MCP 服务器**

网页内容提取工具，面向为 agent 供给上下文的开发者：读取文档、Hacker News、YouTube、GitHub issues、Stack Overflow、Reddit、X 等来源，去除导航与广告，输出保留代码块、表格与对话结构的 Markdown，附元数据与 token 预算控制。以 CLI、TypeScript 库和 MCP 服务器三种形式提供，本地运行无需 API key 或 headless 浏览器，另有托管服务（每月 1000 次免费请求）。限制：不执行 JavaScript、不绕过登录/付费墙、不支持 PDF、单次输入限 20 MiB。

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

- 覆盖文档/HN/YouTube/GitHub/StackOverflow/Reddit/X 等的专用提取器
- CLI、TypeScript 库、MCP 服务器三种形式，本地运行无需 API key
- fetch/parallel_fetch/check/extract_html 四个 MCP 工具，长结果分页续读
- Markdown/JSON/JSONL/XML 四种输出格式与 --budget token 预算控制

## 适用场景

- 让 Claude Code / Cursor 等 agent 通过 MCP 读取网页内容
- 为 LLM 上下文准备去噪后的 Markdown，控制 token 预算
- 在 TypeScript 项目中解析网页并获取结构化元数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: **Web content to clean Markdown for AI agents.**
> L11: Read documentation, Hacker News threads, YouTube videos, GitHub issues, and more with one command. Available as a *
> L84: ## Use with AI agents

## 星数曲线

```mermaid
xychart-beta
    title "fkonovalov/rdrr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 193 --> 195
    line [194, 194]
```

2026-10-18 194 → 2026-10-28 194（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d1be0deb69af` · [字段定义](../../DATASET.md)*
