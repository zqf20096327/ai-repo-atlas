# DevanshSrajput/Dataa_Analyst_Agent

⭐ 23 · Python · MIT · 推送 2026-06-06 · [GitHub](https://github.com/DevanshSrajput/Dataa_Analyst_Agent) · [官网](https://document-agent.streamlit.app/) · 个人维护

**Streamlit 文档分析与对话应用：上传文档即可摘要、分析与问答**

Python + Streamlit 构建的文档分析 Web 应用，面向终端用户：支持 PDF、DOCX、TXT、CSV、Excel 与图片（OCR）上传，提供摘要、统计、图表可视化与基于 BM25 检索的对话问答。LLM 调用通过 OpenCode Zen 的 OpenAI 兼容接口，默认模型 minimax-m3-free，共 10 个可选模型；会话状态以 SQLite 持久化。本地需 pip 安装依赖并配置 API key，也支持一键部署到 Streamlit Cloud。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式文档读取（PDF/DOCX/CSV/Excel/图片 OCR）
- 通过 OpenCode Zen 调用 10 个可选模型，默认 minimax-m3-free
- BM25 检索 + token 级流式输出的文档问答
- SQLite 会话持久化，容器重启后可恢复状态
- 内置 73 项测试套件（不触网）

## 适用场景

- 上传 PDF 或 Excel 后直接对话提问获取要点
- 对 CSV/Excel 数据生成统计摘要与自动图表
- 用 OCR 读取图片文字并纳入问答上下文

## 场景标签

`文档问答` `数据分析` `OCR` · 领域:效率与自动化

## 证据(README 行号)

> L15: - **Read** your PDFs, DOCX, TXT, CSV, Excel (XLSX/XLS), and images (JPG, JPEG, PNG, TIFF, BMP — OCR, because why no
> L16: - **Summarize** them via **OpenCode Zen** — OpenAI-compatible chat completions, with `minimax-m3-free` as the defau
> L85: - **Conversational Q&A:** Ask anything about your documents

## 星数曲线

```mermaid
xychart-beta
    title "DevanshSrajput/Dataa_Analyst_Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b1a439b4175b` · [字段定义](../../DATASET.md)*
