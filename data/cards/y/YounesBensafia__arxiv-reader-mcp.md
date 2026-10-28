# YounesBensafia/arxiv-reader-mcp

⭐ 25 · Python · MIT · 推送 2026-06-07 · [GitHub](https://github.com/YounesBensafia/arxiv-reader-mcp) · 个人维护

**让 MCP 客户端直接检索 arXiv 论文并提取 PDF 全文的服务器**

基于 Python/uv 的 MCP 服务器，向 Claude Code 等 MCP 兼容客户端暴露 5 个工具：按关键词/作者/类别/日期检索论文、快速查询、获取单篇元数据、拉取某类别最新论文、下载并提取指定 arXiv ID 的 PDF 全文。通过 STDIO 传输接入，可用 MCP Inspector 测试；README 附常用 arXiv 类别码表与对话示例。需自备 MCP 兼容客户端使用。

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

- 5 个工具：检索、快速查询、元数据获取、最新论文、PDF 全文提取
- 支持关键词/作者/类别/日期组合检索
- STDIO 传输，可接入 Claude.ai 与 MCP Inspector

## 适用场景

- 在编辑器/助手中直接查找和总结 arXiv 论文
- 获取某类别最新论文列表
- 提取论文 PDF 全文供助手解读方法论

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: MCP server for searching and retrieving papers from arXiv, including full-text PDF extraction.
> L87: > Don't have an MCP-compatible client? Try Claude Code or the MCP Inspector with `uv run arxiv-mcp-server`.

## 星数曲线

```mermaid
xychart-beta
    title "YounesBensafia/arxiv-reader-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b8f5e9bd3696` · [字段定义](../../DATASET.md)*
