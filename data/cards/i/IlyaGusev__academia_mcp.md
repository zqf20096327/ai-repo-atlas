# IlyaGusev/academia_mcp

⭐ 94 · Python · Apache-2.0 · 推送 2026-01-25 · [GitHub](https://github.com/IlyaGusev/academia_mcp) · [官网](https://smithery.ai/server/@IlyaGusev/academia_mcp) · 个人维护

**科研论文与数据集检索分析的 MCP 服务器**

面向 MCP 客户端（如 Claude Desktop）的学术研究工具服务器：提供 arXiv 搜索与下载、ACL Anthology 检索、Hugging Face 数据集搜索、Semantic Scholar 引文查询、Exa/Brave/Tavily 网页搜索、网页抓取、LaTeX 编译与 PDF 阅读等工具；可选 LLM 驱动的文档问答与研究提案工具，需设置 OPENROUTER_API_KEY 启用。支持 stdio/sse/streamable-http 三种传输与可选 Bearer token 认证。Python 3.12+，可 pip 安装或 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- arXiv/ACL Anthology/HF 数据集/Semantic Scholar 引文检索工具
- Exa/Brave/Tavily 统一网页搜索封装
- LaTeX 模板、编译与 PDF 文本提取工具
- 可选 LLM 文档问答与研究提案生成（经 OpenRouter）

## 适用场景

- 让 Claude 等 MCP 客户端检索和下载学术论文
- 构建自动文献综述与引文分析工作流
- 通过对话对论文 PDF 做问答

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9: MCP server with tools to search, fetch, analyze, and report on scientific papers and datasets.
> L105: ### Available tools (one-liners)
> L119: - `document_qa`: Answer questions over provided document chunks (requires LLM).

## 星数曲线

```mermaid
xychart-beta
    title "IlyaGusev/academia_mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 92 --> 95
    line [93, 94, 94]
```

2026-10-18 93 → 2026-10-30 94（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2720ed9676cf` · [字段定义](../../DATASET.md)*
