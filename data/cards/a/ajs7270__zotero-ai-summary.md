# ajs7270/zotero-ai-summary

⭐ 20 · JavaScript · MIT · 推送 2026-05-26 · [GitHub](https://github.com/ajs7270/zotero-ai-summary) · [官网]( https://github.com/ajs7270/zotero-ai-summary/releases/latest) · 个人维护

**Zotero 插件+AI CLI 技能：把 AI 论文笔记存为 Zotero 子笔记**

由本地 Zotero 插件与两个 AI-CLI 技能（summary / pinpoint-lesson）组成：插件在 localhost:23119 暴露小 HTTP API，技能安装到 Claude Code、Codex CLI、Gemini CLI 的技能目录后，由 agent 从 PDF 提取证据、生成含图表/公式/高亮的 Markdown 笔记，发送到插件端点保存为 Zotero 条目下的子笔记。面向已使用 Zotero 的科研人员。需 Poppler 与 Python 3，插件要求 Zotero 9.0+；README 提示向云端模型发送 PDF 的隐私风险。提供交互式安装脚本与手动安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- summary 与 pinpoint-lesson 两种深度笔记技能，支持指定输出语言
- 提取 PDF 栅格图并渲染矢量页，LaTeX 转 Zotero KaTeX
- 同一技能可安装到 Claude Code / Codex CLI / Gemini CLI
- 插件自包含，内置 markdown-it 14.x，无需额外伴侣插件或 Web API 凭证

## 适用场景

- 让 AI CLI 读论文并生成结构化摘要存进 Zotero
- 把精读产出沉淀为含数学推导与测验的长篇课程笔记
- 通过引用键或标题在 Zotero 中定位论文并追加子笔记

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: **AI Summary for Zotero** turns AI-assisted paper reading into structured Zotero child notes. A local Zotero plugin
> L62: |1. Skills|`summary` and `pinpoint-lesson` are copied into your selected AI CLI skill directories.|
> L123: - **Portable skills.** The same skills install into Claude Code, OpenAI Codex CLI, and Google Gemini CLI.

## 星数曲线

```mermaid
xychart-beta
    title "ajs7270/zotero-ai-summary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f25a36a04239` · [字段定义](../../DATASET.md)*
