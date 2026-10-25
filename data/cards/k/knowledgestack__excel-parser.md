# knowledgestack/excel-parser

⭐ 75 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/knowledgestack/excel-parser) · [官网](https://knowledgestack.github.io/excel-parser/) · 组织维护

**将 Excel(.xlsx) 解析为可引用、带公式与依赖图 JSON 的 Python 库，供 LLM/RAG 使用**

开源 Python 库（MIT，Python 3.10+），将 .xlsx 工作簿解析为带类型的单元格图：值、公式 AST、合并区域、7 类图表、条件格式，并生成含 token 计数与来源 URI（file.xlsx#Sheet!A1:F18）的 RAG 就绪分块；提供公式上下游依赖图遍历与 xxhash64 确定性内容哈希。面向构建 RAG 管道与 AI agent（LangChain、LangGraph、CrewAI、OpenAI Agents SDK、MCP 客户端）的开发者。运行依赖 openpyxl、pydantic、lxml、xxhash、tiktoken，可加装 FastAPI 服务。README 含与 Docling 的 SpreadsheetBench 基准对比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输出带 source_uri 与 token 计数的引用就绪分块
- 公式 AST 与上下游依赖图（含环检测）
- 提取 7 类图表、条件格式、数据验证与合并区域
- 默认安全：不执行宏、阻断外链、ZIP-bomb 防护

## 适用场景

- 把财务模型工作簿接入 RAG 管道并按单元格引用回答
- 通过 MCP 客户端让 agent 检索 Excel 内容
- 审计工作簿版本间的变更（内容哈希去重/比对）

## 场景标签

`文档解析` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L11:  <code>excel-parser</code> — the open-source Python library that parses Excel (.xlsx) files into citation-ready JSO
> L43: `excel-parser` turns an Excel workbook into a token-counted, source-addressable
> L141:  🧰 Framework-agnostic LangChain · LangGraph · CrewAI · MCP

## 星数曲线

```mermaid
xychart-beta
    title "knowledgestack/excel-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-25 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0fbca5cb7f20` · [字段定义](../../DATASET.md)*
