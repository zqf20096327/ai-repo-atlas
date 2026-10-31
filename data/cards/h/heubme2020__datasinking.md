# heubme2020/datasinking

⭐ 22 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/heubme2020/datasinking) · [官网](https://datasink.ing) · 组织维护 · 中文 README

**为 LLM/RAG 提供多市场财报全文 Markdown 的 API 与 MCP 服务**

覆盖美、英、中、日、韩、台六地交易所的年报/半年报/季报全文，从官方披露平台（SEC EDGAR、巨潮、DART、EDINET、MOPS 等）抓取并转换为带 YAML frontmatter 的结构化 Markdown，每个数字可溯源到披露块。以 REST API（FMP 风格 symbol 与 apikey）提供，可按章节（如 MD&A、风险）拉取以节省 token；另发布 MCP server（6 个工具），支持托管 URL 或本地运行（Node 18+ / Python 3.8+），并配 curl/Python/R 客户端与示例、研究笔记。免费 key 有速率与文档数配额，整所下载需付费 key。声明提供报告文本而非投资建议，MIT 许可。

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

- 六地市场财报全文转结构化 Markdown，YAML frontmatter 保留标题与表格
- 章节级拉取（MD&A/风险）节省 token，数字可溯源到披露块
- MCP server 6 工具，可托管一键接入或本地 Node/Python 运行
- REST API 配 curl / Python / R 客户端，附 RAG 切块摄取示例

## 适用场景

- 为 RAG 知识库摄取多市场财报全文或指定章节
- 通过 MCP 让 Claude/Cursor 等 agent 直接查询财报数据
- 量化或研究场景批量下载某交易所全部公司的报告
- 不写代码，直接让 LLM 用自然语言查询财报数据

## 场景标签

`金融量化` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: **Full-text financial reports across the US and Asia, as clean Markdown.**
> L18: Ship DataSinking to any AI agent (Claude / Cursor / Codex / Devin Desktop / n8n) as an
> L144: Don't want to write code? Point any LLM at datasink.ing,

## 星数曲线

```mermaid
xychart-beta
    title "heubme2020/datasinking 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2f12434d88e1` · [字段定义](../../DATASET.md)*
