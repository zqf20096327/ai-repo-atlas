# iamsashank09/llm-wiki-kit

⭐ 61 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/iamsashank09/llm-wiki-kit) · 个人维护

**让 AI agent 维护持久化研究维基的 MCP 服务器**

面向 Claude、Codex、Cursor、Windsurf 等 MCP 兼容 agent 的持久记忆工具：agent 通过 wiki_ingest 摄入 PDF、URL、YouTube、markdown 等来源，自动生成维基页面并以 [[wiki links]] 建立概念交叉引用，跨会话持久保留。提供 SQLite FTS5 全文搜索、wiki_lint 健康检查与交互式 HTML 知识图谱可视化；存储为零锁定的纯 markdown 文件。Python 3.10+，pip 安装，按 pdf/web/youtube 可选依赖分装。基于 Karpathy 的 LLM Wiki 模式。

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

- 多格式摄入：PDF/URL/YouTube/markdown 转为维基页面
- 自动交叉引用与 SQLite FTS5 全文搜索
- 8 个 MCP 工具：ingest/write/read/search/lint/status/log/graph
- 知识以纯 markdown 文件存储，可用 Obsidian/VS Code 查看

## 适用场景

- 跨周累积研究论文并向 agent 提出跨文献的综合问题
- 摄入代码库文档让 agent 回答架构问题
- 维护持续更新的竞争情报或学习笔记维基

## 场景标签

`知识库管理` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L10: Based on Karpathy's LLM Wiki pattern. Works with Claude, Codex, Cursor, Windsurf, and any MCP-compatible agent.
> L153: Your agent gets these MCP tools:

## 星数曲线

```mermaid
xychart-beta
    title "iamsashank09/llm-wiki-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-27 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `880559beec9b` · [字段定义](../../DATASET.md)*
