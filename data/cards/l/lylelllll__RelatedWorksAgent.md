# lylelllll/RelatedWorksAgent

⭐ 16 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/lylelllll/RelatedWorksAgent) · 个人维护 · 中文 README

**本地优先的文献综述写作助手：上传论文生成相关工作章节与 Survey 草稿**

面向科研写作的本地部署工作台：创建研究项目、上传 PDF 文献，经解析、分段与向量检索后，由 LangGraph agent 生成 Related Work 章节或完整 Survey 草稿，引文来源在编辑器中可核对，可导出 Word 或 LaTeX/PDF。默认 PDF 解析走 MinerU 官方 API、嵌入与重排走阿里云百炼，写作模型可配置 OpenAI/Anthropic/DeepSeek/Kimi/Qwen/GLM/MiniMax/Ollama；PyMuPDF 与本地检索模型为显式高级选项。项目数据与 ChromaDB 索引留在本机，自称处于早期开源预览阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 两种写作模式：Related Work 章节或完整 Survey 草稿
- 引文溯源映射与审阅建议，导出 Word/LaTeX/PDF
- 默认云端解析与检索，PyMuPDF/本地模型/Ollama 为显式本地选项
- 本地 SQLite/文件存储，无中央应用服务器

## 适用场景

- 整理一批参考论文并生成带证据引用的相关工作章节
- 撰写文献综述初稿并逐条核验引用来源
- 对敏感文档使用 PyMuPDF 与本地检索模式保持数据不出本机

## 场景标签

`科研工具` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L26: Related Works Agent is a local-first workspace for literature review and evidence-aware academic writing. Create a 
> L42: - **Two focused writing modes:** generate a Related Work section or a complete Survey from the same paper collectio

## 星数曲线

```mermaid
xychart-beta
    title "lylelllll/RelatedWorksAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `436998c2f86b` · [字段定义](../../DATASET.md)*
