# shoryasethia/markdrop

⭐ 211 · Python · GPL-3.0 · 推送 2026-08-09 · [GitHub](https://github.com/shoryasethia/markdrop) · [官网](https://pypi.org/project/markdrop) · 个人维护

**把 PDF 转成 Markdown/HTML 并用 LLM 为图表生成描述的 Python 包**

基于 Docling 的 PDF 转 Markdown 工具，保留格式、按 XRef 提取图片、用 Table Transformer 检测表格，支持 PDF URL 输入并输出可下载 Excel 表格的交互式 HTML。AI 部分为提取的图片和表格生成文字描述，支持 Gemini/OpenAI/Anthropic/Groq/OpenRouter/LiteLLM 六类提供商，另有批量图片描述（qwen/molmo/pixtral 等客户端）与 API key 管理命令。提供 CLI 与 Python API，pip 安装，GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF→Markdown/HTML 转换（Docling）+ XRef 图片提取 + Table Transformer 表格检测
- 6 类 LLM 提供商生成图片/表格描述，OpenRouter/LiteLLM 可路由更多模型
- 交互式 HTML 输出含可下载 Excel 表格
- markdrop CLI 覆盖转换、描述、key 设置与批量图片分析

## 适用场景

- 把 PDF 报告或论文批量转成 Markdown 归档
- 为文档中的图片和表格自动生成文字描述
- 从 PDF URL 直接抓取并转换（如 arXiv 论文）

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L11: A Python package for converting PDFs to structured Markdown and interactive HTML, with AI-powered image and table d
> L15: - [x] PDF → Markdown conversion with formatting preservation (via Docling)
> L19: - [x] AI-powered image and table descriptions — **6 providers**: Gemini, OpenAI, Anthropic Claude, Groq, OpenRouter

## 星数曲线

```mermaid
xychart-beta
    title "shoryasethia/markdrop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 210 --> 212
    line [211, 211]
```

2026-10-18 211 → 2026-10-31 211（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `04432afd8d61` · [字段定义](../../DATASET.md)*
