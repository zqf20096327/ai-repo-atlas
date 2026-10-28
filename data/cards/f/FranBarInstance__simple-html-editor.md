# FranBarInstance/simple-html-editor

⭐ 27 · JavaScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/FranBarInstance/simple-html-editor) · [官网](https://franbarinstance.github.io/simple-html-editor/demo/grayscale/) · 个人维护

**无依赖的 WYSIWYG HTML 编辑器，含 AI Agent 编辑辅助**

轻量级 JavaScript WYSIWYG 内容编辑器，可编辑整份 HTML 文档（body 与 head），不使用已废弃的 execCommand，通过单个 JS/CSS 文件引入，无外部依赖。面向需要在已有模板上做可视化编辑的 Web 开发者，提供撤销/重做、图片处理、链接管理、源码编辑等能力。AI 部分基于 ClientAgentJS：支持 openai-compatible/anthropic/google/openai 提供商、流式代码生成、MCP 服务器接入与自定义提示词。README 声明对 90% 以上现代模板无需修改即可工作，动态生成内容存在保存时误存属性的限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可编辑整份文档（body 与 head），不使用 execCommand
- 基于 ClientAgentJS 的 AI Agent：流式代码生成，支持 openai-compatible/anthropic/google/openai
- MCP 服务器接入扩展 AI 能力
- restorable/removable 标记与可恢复动态内容

## 适用场景

- 让用户在既有模板上可视化编辑并保留原设计
- 在编辑器中通过 AI 对话修改或生成 HTML 代码
- 为落地页/静态页提供带 AI 辅助的编辑面板

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A lightweight, customizable **WYSIWYG JavaScript HTML content editor** with **AI Agent** and **MCP (Model Context Pr
> L18: - AI-assisted code editing and generation with streaming responses
> L137: The editor uses **ClientAgentJS** for AI capabilities. You can pre-configure a default model or let users configur

## 星数曲线

```mermaid
xychart-beta
    title "FranBarInstance/simple-html-editor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f7cf24ccb469` · [字段定义](../../DATASET.md)*
