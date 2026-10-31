# aytzey/paper-pilot

⭐ 14 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/aytzey/paper-pilot) · [官网](https://github.com/aytzey/paper-pilot) · 个人维护

**本地 MCP 服务器：让 AI agent 检索、下载并整本阅读论文**

面向 Codex、Claude 等 MCP 客户端的本地学术检索服务器：接入 Semantic Scholar、OpenAlex、arXiv、Crossref、Europe PMC、DOAJ 六个学术数据源，通过 Unpaywall 解析缺失 PDF，可选 Zotero 同步。提供 read_pdf_text 分页读取、render_pdf_pages 页面图像渲染、read_pdf_document 原始 PDF 传输等工具，并保留 DOI、页码等证据链。自身不含 LLM、不需要 API key 或向量数据库；无文本层的扫描 PDF 不做 OCR。附带无 AI 客户端的 CLI demo 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个学术数据库检索 + Unpaywall/OpenAlex PDF 解析链
- 分页连续读取全文、页面图像渲染与原始 PDF 传输三种读取路径
- 保留来源、DOI、PDF 页码与提取警告的证据链
- 无需账户或 API key，自带不含 LLM 的 CLI demo

## 适用场景

- 让现有 AI agent 跨学科调研某个决策问题并整本阅读论文
- 对已有 PDF 做完整阅读、图表检查与假设梳理
- 获取带页码引用的文献证据对比

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Search six academic databases, read methods and results page by page, inspect figures, and get back to the decision 
> L73: Search covers **Semantic Scholar, OpenAlex, arXiv, Crossref, Europe PMC, and DOAJ**. A working PDF is used directly

## 星数曲线

```mermaid
xychart-beta
    title "aytzey/paper-pilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `047540ae2880` · [字段定义](../../DATASET.md)*
