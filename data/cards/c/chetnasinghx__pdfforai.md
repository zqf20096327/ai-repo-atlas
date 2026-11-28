# chetnasinghx/pdfforai

⭐ 10 · TypeScript · MIT · 推送 2026-03-28 · [GitHub](https://github.com/chetnasinghx/pdfforai) · [官网](https://pdfforai.com) · 个人维护

**终端 PDF 转 AI 可用文本/Markdown 的 CLI 工具**

Node.js 命令行工具，将 PDF 转换为面向 LLM 的 XML 封装文本、Markdown 或纯文本。通过 13 阶段转换流水线保留标题、表格、列表、代码块等结构；对扫描件内置 tesseract.js OCR。支持管道输出、目录批处理、页码范围选择，默认本地运行不上传文档。以 npm 包形式发布，提供 CLI 与 TypeScript 编程 API，要求 Node.js ≥20，OCR 引擎与 canvas 打包内置、无需系统依赖。

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

- 13 阶段转换流水线保留标题/表格/列表/代码块等结构
- 扫描件 OCR（tesseract.js），OCR 引擎与 canvas 打包内置
- 三种输出格式：AI Context（XML 封装）、Markdown、纯文本
- 支持目录批量处理、ZIP 打包、stdin 输入与 TypeScript API

## 适用场景

- 把论文/报告 PDF 转成结构化文本粘贴给 ChatGPT/Claude 等处理
- 批量转换目录下的 PDF 并打包为 ZIP
- 在代码中通过 convertPdf API 集成 PDF 转 Markdown 能力

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L15: LLMs like ChatGPT, Claude, and Gemini work best with clean, structured text -not raw PDF bytes. Most PDF-to-text to
> L171: - **Node.js** >= 20.0.0


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `bf1c68a33801` · [字段定义](../../DATASET.md)*
