# PiaoyangGuohai1/cli-anything-zotero

⭐ 139 · Python · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/PiaoyangGuohai1/cli-anything-zotero) · [官网](https://pypi.org/project/cli-anything-zotero/) · 个人维护 · 中文 README

**让 AI 助手经 CLI/JS 桥管理本地 Zotero 文献库的工具**

基于 CLI-Anything 的 Python CLI/SDK，供 Claude Code、Cursor 等可执行终端命令的 AI agent 操作本地 Zotero 7/8/9：通过安装到 Zotero 桌面端的 JS Bridge 插件提供特权端点，覆盖检索、全文搜索、DOI/arXiv/RIS/BibTeX 导入、导出、PDF 附加与补找、元数据/标签/笔记写操作及 DOCX 引用占位符转换（静态/动态两种模式）。写操作本地运行，无需 API key；前置条件是 Zotero 桌面端必须运行。语义检索与 AI 分析为可选功能，需额外的 embedding 端点或 OPENAI_API_KEY。MCP 支持已冻结在 v0.9.5，此后仅维护 CLI/SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ CLI 命令覆盖检索、导入导出、PDF、笔记、写操作
- JS Bridge 本地特权端点，写操作无需 API key 或联网
- DOCX 引用占位符 {{zotero:KEY}} 转静态文本或可刷新 Zotero 字段
- 可选本地 embedding 语义检索与 AI 分析

## 适用场景

- 用自然语言让 AI 助手查询、导入和整理 Zotero 文献
- AI 写作流程中将草稿 DOCX 的引用占位符转为正式引文与参考文献
- 批量补找缺失 PDF、维护标签与笔记

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L34: Built on CLI-Anything by HKUDS, this tool gives AI agents full access to your local Zotero library through a **JS B
> L88: `cli-anything-zotero` is now maintained as a CLI/SDK-first tool. The primary interface is the `zotero-cli` shell co

## 星数曲线

```mermaid
xychart-beta
    title "PiaoyangGuohai1/cli-anything-zotero 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-27 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1ea931797aae` · [字段定义](../../DATASET.md)*
