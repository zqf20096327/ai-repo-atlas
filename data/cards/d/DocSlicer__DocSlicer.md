# DocSlicer/DocSlicer

⭐ 36 · Python · AGPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/DocSlicer/DocSlicer) · [官网](https://www.docslicer.ai/docs) · 组织维护

**面向 RAG/agent 管线的确定性文档解析与分块库，附 MCP 服务器**

将 PDF、docx、pptx、HTML 解析为结构化块、表格、图表与可导航标题层级，输出带完整标题面包屑的不重叠分块。全程无 LLM/ML 模型，确定性执行，约 630 KB wheel，无 GPU 要求；HTML 经 Playwright 真浏览器渲染，扫描件可选 Tesseract OCR 回退。提供 Python 库用于经典 RAG 嵌入，另附 MCP 服务器供 Claude/Cursor/VS Code 拉取大纲按节阅读。限制：不支持 .doc/.ppt/.xlsx 旧格式，PDF 超约 50 页会触发进程池，macOS/Windows 需入口守卫。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 LLM/ML 模型、无 GPU 的确定性解析，31 pages/sec
- 分块携带完整标题面包屑，默认零字符重叠
- 表格以单元格结构返回，支持 markdown/melted/jsonl 序列化
- MCP 服务器支持无向量按节读取长文档

## 适用场景

- 为 RAG 管线把合同、财报等业务文档切成带层级的干净分块
- 让 agent 通过大纲定位并只读取需要的章节，节省 token
- 批量解析文件夹或 URL 列表并导出多格式结果

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: Lightning-fast (31 pages/sec), deterministic document parser and chunker for business documents. No LLM calls or hea
> L15: - **As a Python library — classic RAG.** The layout-aware chunker gives you clean, non-overlapping chunks, each car
> L16: - **As an MCP server — vectorless RAG.** For when you want an answer out of a document right now. Claude, Cursor, o

## 星数曲线

```mermaid
xychart-beta
    title "DocSlicer/DocSlicer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4dc5f5870a12` · [字段定义](../../DATASET.md)*
