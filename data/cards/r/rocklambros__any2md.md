# rocklambros/any2md

⭐ 22 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/rocklambros/any2md) · 个人维护

**将 PDF/DOCX/HTML/URL/TXT 转为面向 RAG 的规范 Markdown 的 CLI 工具**

Python CLI 工具，读取 PDF、DOCX、HTML、URL 与纯文本，输出带固定 YAML frontmatter（SAGE 兼容 schema）的单一 Markdown 流，供下游检索/嵌入/分块管线使用。关键机制：基于 NFC 规范化正文生成可复现的 SHA-256 content_hash、标题层级保证（唯一 H1、不跳级）、token 估算与推荐分块级别。默认轻量安装（pymupdf4llm/mammoth/trafilatura，约 50MB），可选 high-fidelity 安装引入 Docling（约 2GB 模型，首次转换慢 3–10 倍）以处理多栏 PDF、复杂表格与扫描件 OCR。

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

- 固定 frontmatter 契约 + 确定性 content_hash，两台机器输出字节一致
- 轻量与 Docling 双后端路径，CLI 自动检测并可用 -H/--strict 强制
- 标题层级保证（唯一 H1、自动修复跳级）与 token 估算/分块建议
- 多阶段正文清理（去重 TOC、封面残留、重复 byline、HTML 实体循环解码）

## 适用场景

- 为 RAG 检索管线把混合格式的源文档统一成一种 Markdown 形态
- 多栏学术论文、复杂表格 PDF 转换时保留阅读顺序与 GFM 表格
- 利用 content_hash 做下游嵌入/分块的缓存失效判断

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: Convert PDFs, DOCX, HTML, URLs, and plain text into structured, machine-consumable Markdown for downstream RAG pipel
> L20: any2md ingests heterogeneous source documents and emits Markdown with a fixed YAML frontmatter contract. The frontm

## 星数曲线

```mermaid
xychart-beta
    title "rocklambros/any2md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5d240191c70d` · [字段定义](../../DATASET.md)*
