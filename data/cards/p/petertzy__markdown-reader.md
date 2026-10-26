# petertzy/markdown-reader

⭐ 41 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/petertzy/markdown-reader) · [官网](https://petertzy.github.io/markdown-reader/) · 个人维护

**本地优先的跨平台 Markdown 编辑器，内置 AI 翻译与对话**

基于 Tauri 打包、FastAPI 后端 + Next.js 前端的桌面 Markdown 编辑器：多标签、实时预览、斜杠命令、高级表格、浏览器预览与导出。AI 功能需用户自行配置 API，支持 OpenAI、Anthropic、OpenRouter、OpenAI 兼容接口及 LM Studio/Ollama 本地模型，提供 AI 翻译、逐句对比、摘要、格式化，且所有 AI 建议可审计与回滚。另支持通过 MarkItDown 导入 HTML/PDF/DOCX/EPUB 等多种格式、BibTeX 引用插入；macOS Intel 版因 PDF 依赖限制暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地优先架构，文件默认不离开本机
- AI 翻译/摘要/格式化等建议可审查后应用并支持一键回滚
- 支持 OpenAI、Anthropic、OpenRouter 及 LM Studio/Ollama 本地模型
- MarkItDown 通用导入：HTML/PDF/DOCX/EPUB/Office 等 转 Markdown

## 适用场景

- 离线撰写和管理 Markdown 文档，需要时接入 AI 辅助
- 翻译外文文档并逐句对比原文与译文
- 导入 PDF/DOCX/EPUB 等格式文件转为 Markdown 编辑
- 学术写作中插入 BibTeX 引用

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L16: **Markdown Reader bridges the gap.** It is a native desktop application built on Tauri, ensuring your files stay lo
> L21: - 🤖 **Bring-Your-Own-AI**: Configure OpenAI, Anthropic, OpenRouter, OpenAI-compatible providers, or local models.
> L178: Markdown Reader can call locally hosted OpenAI-compatible model servers. In the AI settings panel, choose **Local 

## 星数曲线

```mermaid
xychart-beta
    title "petertzy/markdown-reader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-26 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5fa991ba88ad` · [字段定义](../../DATASET.md)*
