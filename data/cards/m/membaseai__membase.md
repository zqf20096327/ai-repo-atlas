# membaseai/membase

⭐ 143 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/membaseai/membase) · [官网](https://membase.com) · 组织维护

**给 AI agent 提供统一记忆层的 SDK、CLI 与 MCP server**

Membase 为 AI agent 提供记忆层：将事实、文档、网页及 Claude/ChatGPT 聊天导出写入同一份记忆，支持按 Memory 分组、检索与提问、删除需 confirm 确认。本仓库是开发者侧组件，包含 Python/TypeScript 客户端、membase 命令行与 MCP server；记忆可存于托管账户、浏览器扩展填充，或通过 unibaseio-membase[local] 本地存储。官方给出 LoCoMo 93.1%、LongMemEval_S 92.6%、DMR 92.2% 的自测结果，并声明 token 用量约为完整历史的 1/3 至 1/11。托管模式需 MEMBASE_API_KEY，本地模式需 OPENAI_API_KEY 且限 Python 3.12/3.13。

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

- Python/TypeScript SDK、membase CLI 与 MCP server 三种接入方式
- 写入需确认、删除需 confirm=True 等访问控制机制
- 本地存储模式（unibaseio-membase[local]），含照片/视频/音频的 media 扩展
- 提供 Claude、ChatGPT、Cursor、Codex、Gemini CLI、Cline 等 MCP 客户端接入说明

## 适用场景

- 让多个 AI 工具共享同一份长期记忆，切换工具不用重复说明背景
- 把 Claude/ChatGPT 聊天记录导入并统一检索
- 通过 MCP server 让 Claude Code/Cursor 等客户端读写记忆
- 为 agent 框架（LangChain、Dify 等）接入记忆能力

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: Membase is the memory layer for AI agents. It keeps one memory for everything you and your agents
> L28: This repository is the developer side: Python and TypeScript clients, the `membase` command line
> L29: and an MCP server. The memory lives in your Membase account, which the

## 星数曲线

```mermaid
xychart-beta
    title "membaseai/membase 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-24"]
    y-axis "stars" 142 --> 144
    line [143, 143]
```

2026-11-22 143 → 2026-11-24 143（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `91d2220b509a` · [字段定义](../../DATASET.md)*
