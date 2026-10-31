# lobehub/lobe-editor

⭐ 180 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/lobehub/lobe-editor) · [官网](https://editor.lobehub.com) · 组织维护

**面向 AI 应用的 React 富文本编辑器（基于 Lexical）**

基于 Meta Lexical 框架的 React 富文本编辑器组件库，双架构设计：编辑器内核与 React 集成层，面向构建 AI 应用的开发者。提供即插即用的 ChatInput 聊天输入框（斜杠命令、@提及、附件）、Markdown 输入输出、AI 修改文档供用户逐项接受/拒绝的机制，以及 headless 与 renderer 入口支持服务端读写与 SSR 只读渲染。需 React 19，通过 bun/pnpm 安装。

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

- ChatInput 聊天输入框：斜杠命令、@提及、附件、发送按钮
- 模型修改文档、用户逐项接受或拒绝的 AI 编辑机制
- headless 入口支持无 DOM 服务端读写，renderer 支持 SSR
- 发布 skills.md 与 llms.txt 供编码 agent 使用的机器可读文档

## 适用场景

- 为 AI 聊天应用添加带命令和附件的富文本输入框
- 构建模型编辑文档、用户审核改动的写作/知识工具
- 在服务端转换或只读渲染编辑器内容

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: A rich text editor for React, built on Meta's Lexical, for developers building AI apps: chat composers, Markdown doc
> L29: Lobe Editor (`@lobehub/editor`) is a drop-in rich text editor for React apps that talk to AI, from chat input boxes
> L33: - **Let AI edit safely** — Models can change the document while users review and accept or reject each change

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-editor 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-27", "2026-10-31"]
    y-axis "stars" 174 --> 181
    line [175, 176, 179, 180, 180]
```

2026-10-18 175 → 2026-10-31 180（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `514e01e406d4` · [字段定义](../../DATASET.md)*
