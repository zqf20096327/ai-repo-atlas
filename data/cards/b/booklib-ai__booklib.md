# booklib-ai/booklib

⭐ 40 · JavaScript · MIT · 推送 2026-04-10 · [GitHub](https://github.com/booklib-ai/booklib) · [官网](https://booklib-ai.github.io/booklib/) · 组织维护

**面向 AI 编码助手的知识缺口检测与运行时上下文注入工具**

booklib 是一个上下文工程 CLI 工具，面向使用 Claude Code、Cursor、Copilot 等 AI 编码助手的开发团队。它扫描依赖（npm/PyPI/Maven 等 10 个包生态）的发布日期，与模型训练截止时间比对，检出代码库中的训练后 API 缺口，并通过 Context7/GitHub/手动连接自动拉取当前文档；经 MCP 以 PreToolUse/PostToolUse 钩子在编码时注入 3-10 行相关知识。支持团队决策捕获与违规检测、11 种语言的导入检查、BM25+向量混合检索与知识图谱。默认全本地运行（HuggingFace Transformers 嵌入），可选 Ollama/Anthropic/OpenAI 云端模式。要求 Node.js >= 18，npm 全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测 10 个包生态中训练后发布的 API 并自动拉取当前文档
- 经 MCP 向 14 种 AI 编码工具注入运行时上下文（Pre/PostToolUse 钩子）
- 团队决策捕获与代码违规实时检测
- BM25+向量+RRF+重排序的混合检索与知识图谱

## 适用场景

- 发现 AI 编码助手因训练截止而产生的过时 API 用法
- 把团队编码规范与项目文档注入 AI 工具的上下文
- 连接 Notion/GitHub 讨论/本地文档建立团队知识索引

## 场景标签

`RAG` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5:  A context engineering tool for AI coding assistants.
> L121: `booklib init` detects your AI tools and configures MCP automatically.

## 星数曲线

```mermaid
xychart-beta
    title "booklib-ai/booklib 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-27 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bc0cc7b1e0f0` · [字段定义](../../DATASET.md)*
