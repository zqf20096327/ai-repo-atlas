# nekyialabs/resonant-archive

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/nekyialabs/resonant-archive) · 组织维护

**本地优先的 AI 对话历史语义归档与检索工具（CLI+MCP）**

面向每天使用 Claude Code 的用户，由两部分组成：chronicle 模组通过 hooks 干预上下文压缩，让 AI 以自定义口吻写压缩摘要、保留近期原文并镜像每条消息到磁盘；archive 部分将 Claude Code 会话、ChatGPT/claude.ai 导出、Markdown 笔记导入本地 Postgres，结合全文、本地嵌入向量和精确锚点做 rank-fused 混合检索。提供只读 MCP 服务器供 Claude Code/Claude Desktop 调用。限制：仅 Linux/macOS，归档需要 Postgres 15+ 与 pgvector，hooks 属早期访问特性，原始 ChatGPT/claude.ai 导出需先经 Nexus 转换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- chronicle 模组：自定义口吻压缩、近期对话逐字保留、/squish 手动触发与 75%/90% 上下文计量
- 混合检索：全文+本地嵌入向量+精确锚点 rank-fused，无 API key 全程本机运行
- 只读 stdio MCP 服务器（search/around/overview/associate/stats 等 6 个工具）
- 导入器插件化，支持 chronicle 镜像、Claude Code 转录、Nexus Markdown、笔记文件夹

## 适用场景

- 把 Claude Code、ChatGPT 等历史对话汇成可语义检索的本地档案
- 压缩后通过 recall 找回被摘要掉的原句与标识符
- 让 Claude Code/Desktop 通过 MCP 检索我的全部对话历史

## 场景标签

`语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L47: Your AI reaches it through MCP (`search`, `around`, `overview`, `associate`, `stats`). The chronicle mod reaches it
> L123: `resonant-archive mcp` is a read-only stdio MCP server. It does not need a daemon running; if the embed server (`r

## 星数曲线

```mermaid
xychart-beta
    title "nekyialabs/resonant-archive 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28", "2026-10-31"]
    y-axis "stars" 10 --> 15
    line [11, 12, 14, 14]
```

2026-10-18 11 → 2026-10-31 14（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b029616fbd7a` · [字段定义](../../DATASET.md)*
