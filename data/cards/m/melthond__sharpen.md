# melthond/sharpen

⭐ 3 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/melthond/sharpen) · [官网](https://sharpen-site.vercel.app) · 个人维护

**Claude Code 插件：把含糊的输入重写成明确的工程化提示词**

一个 Claude Code 插件，把用户输入的简短提示词结合会话历史、代码库与已安装的 skills、agents、MCP servers 和 hooks 重写为完整的工程化提示词；仅在两种理解会导致不同工作时才追问。流程分 Gate 分类、快速检索（最多 3-6 次代码搜索）、按意图类型生成提示词、评审卡确认四步。零依赖、无 API 调用、无遥测，默认关闭，需用户通过 /sharpen on 启用。要求 Node.js 18+。

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

- 结合会话、代码与已装 skills/agents/MCP/hooks 生成工程化提示词
- 歧义时给出 2-3 个选项让用户选择，未确认前不运行任何内容
- 评审卡提供 Send it / Run my original / 修改三种选择，提示词同时复制到剪贴板
- 十个配套技能：改写、审计、交接、拆分、访谈、规划等

## 适用场景

- 给 Claude Code 发简短指令时获得明确的任务提示词
- 把一段对话转成新会话的交接提示词
- 把大型需求拆分成有序可并行的小提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L17:  A Claude Code plugin that rewrites your plain prompt into the prompt you meant, using your conversation, your code
> L38: **Requires** Claude Code with plugin support, and Node.js 18 or later, which runs the hooks.
> L109: Coming next: Codex, Gemini CLI and GitHub Copilot CLI. Each gets a dropdown here once Sharpen runs in it.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `34f85cd963e9` · [字段定义](../../DATASET.md)*
