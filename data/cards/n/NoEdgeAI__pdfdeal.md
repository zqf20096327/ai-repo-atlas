# NoEdgeAI/pdfdeal

⭐ 288 · Python · MIT · 推送 2026-03-18 · [GitHub](https://github.com/NoEdgeAI/pdfdeal) · [官网](https://noedgeai.github.io/pdfdeal-docs/) · 个人维护 · 中文 README

**Doc2X OCR API 的 Python 封装，附 PDF/Markdown 处理工具**

围绕 Doc2X 文档转换 API 的 Python 库：提供抽象封装类调用 Doc2X 将 PDF/图片转为 Markdown/LaTeX 等格式（支持 v3-2026 模型的 JSON 输出与 sidecar 文件），并附带本地文本处理工具——图片 OCR 回填原文、HTML 表格转 Markdown、图片上传远程存储/本地化、Markdown 按标题切分等，用于提升 PDF 在 graphrag、Dify、FastGPT 等 RAG 知识库中的召回效果。附带 v3 图表/表格裁剪辅助脚本。pip 安装，rag 扩展可选。

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

- Doc2X API 的抽象封装类（多种输出格式，v3 JSON sidecar）
- 图片 OCR 识别回填原文并保持原 PDF 页码
- Markdown 工具：HTML 表格转换、图片远程上传/本地化、按标题切分
- 基于 v3 JSON 的图表/表格裁剪辅助脚本与库导入接口

## 适用场景

- 把 PDF 转成 Markdown/LaTeX 后导入 RAG 知识库（Dify/FastGPT/graphrag）
- 将文档中的在线图片上传到远程存储以保证可访问性
- 从 PDF 提取图表/表格裁剪图用于知识库配图

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L20: Doc2X is a new universal document OCR tool that can convert images or PDF files into Markdown/LaTeX text with formu
> L26: After conversion and pre-processing of PDF using Doc2X, you can achieve better recognition rates when used with kno
> L64: pip install --upgrade pdfdeal

## 星数曲线

```mermaid
xychart-beta
    title "NoEdgeAI/pdfdeal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 287 --> 289
    line [288, 288]
```

2026-10-18 288 → 2026-10-23 288（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ff21a7549494` · [字段定义](../../DATASET.md)*
