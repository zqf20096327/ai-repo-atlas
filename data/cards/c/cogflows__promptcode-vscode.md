# cogflows/promptcode-vscode

⭐ 17 · TypeScript · MIT · 推送 2025-12-24 · [GitHub](https://github.com/cogflows/promptcode-vscode) · [官网](https://marketplace.visualstudio.com/items?itemName=cogflows.promptcode) · 组织维护

**面向 AI 编码工具的 VS Code 扩展与 CLI：选文件、生成提示词、应用改码**

以 VS Code 扩展和独立 CLI 两种形式提供：从工作区挑选文件作为上下文（支持 .gitignore/.promptcode_ignore 过滤与实时 token 计数），配合内置或自定义提示词模板生成发给 LLM 的提示词；用户将模型回复粘贴回 Merge 标签页，工具解析代码改动并以 diff 预览、批量应用。兼容任意 AI 模型（含无 API 的网页版），CLI 另有 Expert Mode 直接咨询（需 OpenAI/Anthropic/Google/xAI API key）、预算控制、Claude Code 斜杠命令与 Cursor 集成。限制：需 VS Code ≥1.96.0；Expert 模式需联网与 API key；默认收集匿名遥测（可关闭）。

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

- 文件级上下文选择 + 提示词模板生成 + 回复解析为 diff 批量应用
- 复制粘贴方式兼容任意 AI 模型，含无 API 的网页/桌面端
- CLI Expert Mode 直接 AI 咨询，支持预算上限、dry-run 与审批流程
- promptcode cc / promptcode cursor 提供 Claude Code 与 Cursor 集成

## 适用场景

- Cursor/Windsurf 卡住时，自选文件上下文手写精确提示词求助 LLM
- 把 AI 回复粘贴回来，diff 预览并一键应用多文件改动
- 在终端/CI 中以 Expert Mode 带代码上下文咨询多厂商模型

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L12: PromptCode is your go-to solution when code agents like Cursor or Windsurf hit a wall. Available as both a powerful
> L62: - **Copy & Paste**: Works with ANY AI model or assistant - including OpenAI, Anthropic Claude, Google Gemini, and o
> L75: - **Claude Code Integration**: Custom slash commands for Claude Code (`promptcode cc`)

## 星数曲线

```mermaid
xychart-beta
    title "cogflows/promptcode-vscode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4c7332a4c449` · [字段定义](../../DATASET.md)*
