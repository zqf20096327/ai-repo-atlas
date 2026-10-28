# MegaByteMark/markdown-ui-dsl

⭐ 24 · MIT · 推送 2026-03-14 · [GitHub](https://github.com/MegaByteMark/markdown-ui-dsl) · 个人维护

**面向 AI 编码代理的文本 UI 线框 DSL 规范**

一套基于 Markdown 的严格中间表示（IR）规范：产品经理可编写低保真 `.ui.md` 规格，AI 编码代理以确定性方式解析并生成 React/Vue/HTML 等 UI 代码。语法覆盖容器布局、卡片/弹窗、表单控件、徽章等组件，通过 YAML frontmatter 关联设计系统文件，blockquote 指令支持对齐与响应式断点。以 SKILL.md 技能文件形式分发，提供 OpenClaw Hub、Copilot、Cursor/Cline/Roo、Claude Code、Gemini CLI、GPT Codex 等接入方式。事件与状态逻辑不在 DSL 范围内，需在提示词或需求文档中补充。

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

- Markdown 语法定义布局、组件与 Agent 指令（对齐/间距提示）
- YAML frontmatter 关联设计系统文件，结构与样式分离
- @<breakpoint> 响应式指令按移动优先叠加应用
- 事件与状态逻辑明确排除在 DSL 范围外

## 适用场景

- 产品经理编写低保真 UI 规格，交由 AI 代理生成组件代码
- Spec-Driven Development 流程中用 `.ui.md` 驱动 UI 迭代与代码同步
- 为不同 AI 编码代理（Copilot/Cursor/Claude Code 等）统一 UI 规格输入格式

## 场景标签

`提示工程` `编码 Agent` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L6: A lightweight, text-based wireframing standard designed specifically for AI coding agents and Spec-Driven Developmen
> L16: This project provides a strict Markdown-based Intermediate Representation (IR). Product managers can write easily r

## 星数曲线

```mermaid
xychart-beta
    title "MegaByteMark/markdown-ui-dsl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0369bc3cc6b2` · [字段定义](../../DATASET.md)*
