# nirholas/extract-llms-docs

⭐ 35 · TypeScript · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/nirholas/extract-llms-docs) · [官网](https://llm.energy) · 个人维护

**从网站提取 llms.txt/install.md 文档供 AI agent 使用**

基于 Next.js/TypeScript 的 Web 应用与 MCP 服务器：自动探测并抓取网站的 llms.txt、llms-full.txt 与 install.md，按章节拆分为独立 Markdown 文件，导出 Markdown/JSON/YAML/ZIP；提供 REST API 与批量处理，MCP 服务器暴露 extract_docs、validate_url 等 6 个工具供 Claude Desktop、Cursor 等 MCP 客户端调用。另含 AI 驱动的 install.md 生成器（分析 GitHub 仓库或文档 URL，经 Claude 合成，需 ANTHROPIC_API_KEY）与 llms.txt 生成向导。提供托管版或 git clone 本地运行（端口 3001）。许可为专有（Proprietary）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动探测并按章节拆分 llms.txt / install.md 文档
- MCP 服务器提供 6 个工具，接入 Claude Desktop、Cursor 等客户端
- REST API：extract/validate/batch/download/generate-install
- AI 生成 install.md：从 GitHub 仓库或文档 URL 分析并合成（需 ANTHROPIC_API_KEY）

## 适用场景

- 把网站文档转成 AI 编码助手可读的结构化 Markdown
- 通过 MCP 让 agent 检索和验证站点的 llms.txt 文档
- 为现有 GitHub 项目生成 LLM 可执行的 install.md 安装说明

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L22: llm.energy is a web application and MCP server that fetches, parses, and organizes documentation from websites impl
> L37: |🔌 **MCP Server**|Integrate with Claude Desktop, Cursor, and more|
> L163: The MCP server exposes the following tools for AI agents:

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/extract-llms-docs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-26 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c87a4b22ea4b` · [字段定义](../../DATASET.md)*
