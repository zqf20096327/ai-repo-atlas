# aaryanbindage/twinbraid

⭐ 4 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/aaryanbindage/twinbraid) · [官网](https://aaryanbindage.github.io/twinbraid/) · 个人维护

**让两个编码 agent 在同一工作区协作的桌面编排器**

Electron 桌面应用与 CLI，将两个已有编码 agent（Claude Code、Codex、本地模型、Gemini CLI、Aider 等）放在同一项目文件夹同时工作：agent 间以短消息交接任务，用户可实时查看思考流、工具调用与 token/代码行统计，可中断单个或广播给两者。本地模型通过 OpenAI 兼容 API 走自建的工具循环（Read/Write/Edit/Bash 等）。含消息数上限、文件冲突警告等护栏。Codex、LM Studio 等部分适配目前仅通过模拟器验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同一文件夹双 agent 并行协作，agent 间短消息交接
- 实时面板展示思考流、工具调用、token 与代码行增删统计
- 本地模型走自建工具循环（Read/Write/Edit/LS/Glob/Grep/Bash），需支持 tool calling
- 内置无账号模拟器可 60 秒体验；提供 headless CLI 运行

## 适用场景

- 强模型规划评审、本地/低价模型执行编辑的双 agent 分工
- 两个不同模型对同一任务交叉检查
- 在终端以 headless 方式编排两个 agent 跑任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L4: Claude Code, Codex, local models (Ollama, LM Studio, llama.cpp), Gemini CLI, Aider, or any OpenAI-compatible API. An
> L126: **Is this a new agent?** No. It orchestrates agents you already have. Twinbraid itself calls no model except the l


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `0ffed3e591ff` · [字段定义](../../DATASET.md)*
