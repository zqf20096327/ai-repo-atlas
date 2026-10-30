# NextStat/chatgpt2md

⭐ 20 · Rust · MIT · 推送 2026-03-01 · [GitHub](https://github.com/NextStat/chatgpt2md) · 个人维护

**把 ChatGPT 导出记录转成 Markdown 并供 Claude 检索的 CLI 工具**

Rust 编写的单二进制 CLI 工具：读取 ChatGPT 数据导出包（ZIP 或 JSON），将每段对话转换为带 YAML frontmatter 的 Markdown 文件并按年/月目录组织，同时基于 Tantivy 构建全文索引。内置 MCP 服务器（stdio 传输），提供 search_conversations、get_conversation、list_conversations 三个工具，使 Claude Desktop 与 Claude Code 可直接检索并读取历史对话；一条 install 命令可自动完成接入配置。支持 macOS/Windows，可从源码编译（需 Rust 1.85+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatGPT 导出（ZIP/JSON）转 Markdown，按年/月组织并生成 Tantivy 全文索引
- 内置 MCP 服务器提供 3 个检索/读取工具（stdio 传输）
- 一条命令自动配置 Claude Desktop 与 Claude Code 接入
- 单二进制，无运行时依赖

## 适用场景

- 把 ChatGPT 历史对话迁移到本地 Markdown 笔记库（Obsidian 等）
- 在 Claude 中直接搜索和读取自己的 ChatGPT 历史对话
- 对过往对话做全文检索与按时间浏览

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: A fast CLI tool that converts your ChatGPT export into organized Markdown files, builds a search index, and provides
> L10: - MCP server with 3 tools for Claude integration

## 星数曲线

```mermaid
xychart-beta
    title "NextStat/chatgpt2md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0bdf87ad5013` · [字段定义](../../DATASET.md)*
