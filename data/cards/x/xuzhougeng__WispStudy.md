# xuzhougeng/WispStudy

⭐ 32 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/xuzhougeng/WispStudy) · [官网](https://xuzhougeng.github.io/WispStudy/) · 个人维护 · 中文 README

**本地优先的文献管理与阅读工具，支持向文献库提问**

基于 Rust + GPUI 的桌面文献管理工具（Windows/macOS/Linux），核心流程为收集、筛选、阅读、提问与写作：支持 DOI/PMID 导入、BibTeX/RIS/Zotero 导入、PDF 批注，AI 助手可批量给出筛选建议并附原文引用、回答问题时逐句核对引文并在 PDF 中定位、按章节辅助手稿写作并导出带修订的 Word。每个文献库为独立文件夹，数据本地保存；提问、筛选、翻译等功能需在设置中配置模型服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地优先：无账号无云端，每个文献库是一个独立文件夹
- 筛选建议附原文逐字引用，回答中的 [P3 p.5] 可点击跳转 PDF 对应页
- 写作页按章节组织，可从 Word/Markdown 起稿并导出带修订记录的 Word
- wisp CLI 与 MCP server（wisp mcp）将同一套工具开放给外部 AI 客户端

## 适用场景

- 批量导入 PubMed/arXiv 检索结果并让助手辅助筛选入组文献
- 向整个文献库提问，引文可点击溯源到 PDF 原文
- 在写作页逐节起草论文，边写边引用库内文献语句

## 场景标签

`AI 助手` `科研工具` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L7:  A local-first literature library: collect, screen and read papers, and ask your library questions.
> L34: **🐋 Import broadly first, then let the assistant help you screen.** Save search queries for PubMed, Europe PMC, Cro
> L100: Asking, the library wizard, screening, translation and the model's sectioning on the Writing page need a model pro


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `30097e95f819` · [字段定义](../../DATASET.md)*
