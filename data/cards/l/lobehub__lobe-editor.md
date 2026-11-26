# lobehub/lobe-editor

⭐ 186 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/lobehub/lobe-editor) · [官网](https://editor.lobehub.com) · 组织维护

**给开发者构建 AI 应用的 React 富文本编辑器**

基于 Meta Lexical 的 React 富文本编辑器组件库，提供内核与 React 集成双入口（`@lobehub/editor` 与 `/react`），面向构建 AI 应用的开发者。核心组件包括带斜杠命令、@ 提及与附件的聊天输入框（ChatInput），支持 Markdown 输入输出、表格/代码块/数学公式等富内容；提供模型改动逐条接受/拒绝的 AI 编辑流程，以及无 DOM 的服务端读写与 SSR 安全渲染入口。要求 React 19 与若干 peer dependencies。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatInput 组件：斜杠命令、@ 提及、附件与发送按钮
- AI 编辑流程：模型改动后由用户逐条接受或拒绝
- headless 入口支持无 DOM 的服务端内容处理，renderer 入口支持只读 SSR 渲染与 diff
- 提供 skills.md 与 llms.txt 供编码 agent 读取使用

## 适用场景

- 给 AI 聊天应用接入带提及、命令和附件的富文本输入框
- 构建模型编辑文档、用户审核改动的写作/知识工具
- 在服务端无浏览器环境下转换或渲染编辑器内容
- 搭建需要实时同步文档的协作编辑器

## 场景标签

 · 领域:开发工具/前端组件库

## 证据(README 行号)

> L29: Lobe Editor (`@lobehub/editor`) is a drop-in rich text editor for React apps that talk to AI, from chat input boxes
> L33: - **Let AI edit safely** — Models can change the document while users review and accept or reject each change
> L91: - **AI chat apps** that need a rich input box with mentions, commands and attachments

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-editor 星数(近 8 点)"
    x-axis ["2026-10-24", "2026-10-27", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-18", "2026-11-23", "2026-11-26"]
    y-axis "stars" 178 --> 187
    line [179, 180, 179, 181, 182, 183, 184, 186]
```

2026-10-24 179 → 2026-11-26 186（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `79e28355e5c1` · [字段定义](../../DATASET.md)*
