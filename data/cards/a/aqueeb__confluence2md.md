# aqueeb/confluence2md

⭐ 48 · Go · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/aqueeb/confluence2md) · 个人维护

**将 Confluence MIME 导出（.doc）转为 Markdown 的 CLI 工具**

Go 编写的命令行工具，解析 Confluence"导出为 Word"实际生成的 MIME 编码 HTML 文件（仅 Word 能打开），经内嵌 pandoc 转为 GitHub 风格 Markdown，并清理 Confluence 特有 HTML、转换 emoji 图片与提示框、处理折叠区/代码块/表格，支持目录批量转换。发布版二进制内嵌 pandoc 无外部依赖，也可 go install 源码构建（此时需系统安装 pandoc）。面向需要把 Confluence 文档迁入 Git、静态站点或 LLM/RAG 管线的开发者；不处理二进制 .doc 与 .docx。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 Confluence MIME 编码导出并转为干净 Markdown
- 发布二进制内嵌 pandoc，零外部依赖
- 清理 Confluence HTML 产物：emoji 图片转 Unicode、信息框转 blockquote
- 支持目录批量转换与 dry-run

## 适用场景

- 把 Confluence 内容迁移到 GitBook/Docusaurus/MkDocs 等 Git 文档体系
- 把团队 Confluence 文档转为 Markdown 供 RAG/LLM 知识库使用
- 生成不依赖 Confluence 或 Word 阅读的可移植文档备份

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L23: You can't convert Confluence exports to Markdown for version control, static site generators, or LLM/RAG pipelines—
> L40: - **Build RAG/LLM knowledge bases** — Feed your Confluence docs to LangChain, LlamaIndex, or custom embedding pipel

## 星数曲线

```mermaid
xychart-beta
    title "aqueeb/confluence2md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e2a73997efef` · [字段定义](../../DATASET.md)*
