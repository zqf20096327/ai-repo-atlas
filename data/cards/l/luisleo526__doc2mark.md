# luisleo526/doc2mark

⭐ 51 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/luisleo526/doc2mark) · 个人维护

**文档转 Markdown 的 Python 库：面向 RAG 保留表格与版式**

Python 库（3.10+），将 PDF、Word、Excel、PowerPoint、图片、HTML、邮件等转为 Markdown，保留合并单元格（以 HTML 表格内嵌）、按序读取多栏、剔除页眉页脚；扫描页可经视觉 LLM 或本地 Tesseract 做 OCR，输出结构化 OCRPage 并区分转写与模型解读。默认确定性解析、无需任何 AI 组件；可选 TypeSafe Jev 质量裁判（默认关闭，开启会把文档文本发给第三方）。面向为 LLM/检索管线准备语料的开发者，提供 pip 安装、Python API 与 CLI，内置分节切块与转换报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 合并单元格以 HTML 表格保留（Word/PowerPoint/Excel/PDF 划线表格）
- 按页信号路由 OCR：仅扫描页/乱码文本层/矢量文字走 OCR，好文本层保留
- LLM OCR 返回结构化 OCRPage，转写与模型解读分离，拒答型回答不入索引
- 可选 Jev 质量裁判（默认关闭）判定文本层可读性/页眉页脚/OCR 拒答
- 分节切块（按字符或 token）带页码范围与标题路径

## 适用场景

- 把 PDF/Office 文档批量转成干净 Markdown 喂给 RAG 管线
- 保留复杂合并表格结构供下游解析
- 扫描件经 LLM 或本地 Tesseract OCR 后结构化归档

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L15: doc2mark converts PDFs, Word, Excel and PowerPoint files, images, HTML, e-mail and more into
> L141: - **No ML stack to host.** Text, tables and structure are parsed locally and deterministically;
> L143:  only when you turn that on.

## 星数曲线

```mermaid
xychart-beta
    title "luisleo526/doc2mark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-31 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e771582f3ab2` · [字段定义](../../DATASET.md)*
