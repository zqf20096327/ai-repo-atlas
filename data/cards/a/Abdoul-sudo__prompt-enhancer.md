# Abdoul-sudo/prompt-enhancer

⭐ 3 · TypeScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/Abdoul-sudo/prompt-enhancer) · 个人维护

**Claude Code 插件：一键结合上下文改写提示词**

以 Claude Code mod/插件形式提供的提示词改写工具：点击 Enhance prompt 按钮或 /enhance 命令后，插件读取草稿、最近 8 轮对话与可选的 project-context.md，用 Sonnet（可改配置为其他模型）改写为更清晰的提示词，结果填入输入框由用户确认后自行发送，原草稿可一键恢复。支持桌面应用与终端（全屏模式或命令行）。每次改写计入用户的 Claude Code 计划用量。通过 claude plugin marketplace 命令安装与更新，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键改写输入框草稿，改写结果经用户确认后才发送
- 读取聊天最近 8 轮对话与 project-context.md 作为上下文
- 支持桌面应用与终端两种运行方式
- 模型与 effort 可在 hooks/register.tsx 中修改

## 适用场景

- 把零散的短句草稿整理成结构清晰的提示词
- 让改写结果结合当前项目描述与对话上下文
- 改写不满意时一键恢复原始草稿

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Claude Code mod
> L22: - **Improves your prompt in one click**: a short draft becomes a clear prompt that gets a better result.
> L108: The mod uses Sonnet at medium effort. Each rewrite counts on your Claude Code plan.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d42a04b3aa58` · [字段定义](../../DATASET.md)*
