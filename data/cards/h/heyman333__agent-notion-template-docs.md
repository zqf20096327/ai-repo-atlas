# heyman333/agent-notion-template-docs

⭐ 107 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/heyman333/agent-notion-template-docs) · 个人维护

**让 AI agent 生成 Notion 视觉风格 HTML 文档的技能插件**

面向 Codex 与 Claude Code 的 agent 技能：提供单一 HTML 模板与 Notion 常用内容块（callout、TOC、表格、toggle、代码高亮等），agent 复制模板填充内容而非自写 CSS，从而获得 Notion 风格的浅色/深色文档并支持打印导出。附 lint.py 用 Python 标准库检查产出是否偏离模板，PostToolUse 钩子自动运行；模板取值自 Notion 官方 design token，每周 CI 任务 notion-sync 比对官方参考页防止漂移。以插件或手动复制目录安装，也可用于 Cursor、Gemini CLI 等可读指令文件的 agent。

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

- 单一 template.html 复制填充机制，agent 不生成 CSS
- lint.py 检测 CSS 漂移、未知 class、内联样式等，仅依赖 Python 标准库
- 模板取自 Notion 官方 design token，每周 CI notion-sync 比对防漂移
- Codex 与 Claude Code 共用同一 skill 目录（symlink），避免分叉

## 适用场景

- 让我的 agent 写出 Notion 风格的报告、复盘、提案文档
- 在 CI 中自动检查 agent 生成文档是否符合模板规范
- 导出浅色打印/PDF 版 Notion 风格文档

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L13: **notion-doc** is an agent skill that gives those documents a Notion-like visual style.
> L51: `plugin.json`, one `skills/` directory, one hook. Codex and Claude Code install

## 星数曲线

```mermaid
xychart-beta
    title "heyman333/agent-notion-template-docs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 105 --> 108
    line [106, 107]
```

2026-10-18 106 → 2026-10-25 107（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `bb7a3d505422` · [字段定义](../../DATASET.md)*
