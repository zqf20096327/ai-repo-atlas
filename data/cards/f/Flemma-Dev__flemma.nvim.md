# Flemma-Dev/flemma.nvim

⭐ 58 · Lua · AGPL-3.0 · 推送 2026-07-29 · [GitHub](https://github.com/Flemma-Dev/flemma.nvim) · 组织维护

**Neovim 的纯文本 AI 知识工作台：以 .chat 文件承载对话**

面向 Neovim 用户的模型无关 LLM 客户端与代理工具：把会议记录、简报、邮件等输入整理为工作文档，多轮迭代，可在同一草稿上切换模型获取第二意见。核心机制是对话即 .chat 纯文本文件——无数据库、无隐藏会话状态，可编辑、grep、git 提交；每个文件可携带独立模型与系统提示设置。内置 Anthropic/OpenAI/Vertex/Moonshot 四个 provider（另实验性 Codex），代理模式支持 bash/read/edit/write 等工具与 MCP（经 MCPorter），提供审批、Bubblewrap 沙箱与回合上限。需 Neovim 0.11+ 与 curl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对话即 .chat 文件：可编辑、grep、git 提交，无隐藏状态
- 四个内置 provider，支持中途切换与统一 thinking 参数
- 代理模式：bash/read/edit/write 等工具、审批流程、Bubblewrap 沙箱、100 回合上限
- 经 MCPorter 支持 MCP，可从 Claude Code/Cursor/VS Code/Windsurf 导入服务器

## 适用场景

- 在编辑器内起草与迭代工作文档（方案、规格、状态更新）
- 同一草稿切换不同模型对比观点
- 让代理自动读代码、改文件、跑测试完成任务
- 把带系统提示的 .chat 文件作为团队共享模板

## 场景标签

`编码 Agent` `知识库管理` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L12: Flemma is a plain-text, model-agnostic LLM client for real knowledge work: statements of work, solution designs, sp
> L95: - **Draft and refine the documents your work runs on.** Statements of work, solution designs, specs, proposals, sta

## 星数曲线

```mermaid
xychart-beta
    title "Flemma-Dev/flemma.nvim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 56 --> 59
    line [58, 57, 58]
```

2026-10-18 58 → 2026-10-31 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `36c4003ad44e` · [字段定义](../../DATASET.md)*
