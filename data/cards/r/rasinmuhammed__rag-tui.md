# rasinmuhammed/rag-tui

⭐ 21 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/rasinmuhammed/rag-tui) · 个人维护

**终端里的 RAG 管道调试工具：切块可视化、诊断与评测**

面向 RAG 开发者的终端 UI（TUI）与 CLI 工具：粘贴或加载文档后，用滑块实时调整切块大小与重叠、在七种切块策略间切换并查看重叠高亮；提供无需标注查询集的 corpus 结构诊断（hub/orphan/duplicate/fracture/boilerplate 五项检查，输出 0-100 评分可作 CI 门禁）、批量 IR 指标评测（hit rate/MRR/nDCG 等，可选本地 LLM 评判）、参数扫描优化，并可导出 LangChain/LlamaIndex 配置。嵌入支持 Ollama/OpenAI/Gemini/Groq 或内置词法嵌入（无模型、离线可用）；另提供 MCP server 与 Python API。基础安装仅需 pip，无模型下载与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需标注查询集的 corpus 结构诊断，五项检查输出可作 CI 门禁的评分
- 滑块实时重渲染的切块可视化，7 种策略 + 自定义 Python 切块器（AST 沙箱）
- 嵌入提供多后端并自动选择，内置词法嵌入支持离线零依赖运行
- MCP server 提供 6 个工具供 Claude Code/Cursor 等 agent 调用

## 适用场景

- 调试检索返回错误切块的问题，直观对比不同切块配置
- 在 CI 中用评分门禁拦截知识库质量回退
- 扫描上百种切块配置组合并按 IR 指标排序选优
- 让 agent 在同一会话中直接调整切块管道

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L33: `rag-tui doctor` does not ask for queries. It embeds your chunks once and then studies the shape of the space they 
> L139: Paste a list of queries and get the full IR suite back as colour-coded bars: hit rate, MRR, nDCG@k, recall@k and p
> L153: Presets for common jobs (QA, summarisation, code search, long documents), the custom chunker and cleaner editors, 

## 星数曲线

```mermaid
xychart-beta
    title "rasinmuhammed/rag-tui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f0c93382ddbe` · [字段定义](../../DATASET.md)*
