# belingud/yaicli

⭐ 19 · Python · Apache-2.0 · 推送 2026-06-23 · [GitHub](https://github.com/belingud/yaicli) · [官网](https://belingud.github.io/yaicli/) · 个人维护 · 中文 README

**命令行 AI 助手：在终端对话、执行命令与快速问答**

基于 Python/Typer 的命令行 LLM 客户端，提供三种交互模式：带上下文的持久对话、生成并安全执行系统 Shell 命令、免交互快速问答；支持管道输入与图像（Vision）输入。内置 25+ 提供商适配（OpenAI/Anthropic/Gemini/Ollama/DeepSeek 等）及任意 OpenAI 兼容端点，支持 Function Calling（v0.5.0 起）与 MCP 工具（v0.7.0 起），工具调用前逐次确认。通过 config.ini 与环境变量分层配置，历史记录默认保存 500 条。需 Python 3.10+，pip/uv/源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对话/命令执行/快速问答三种交互模式，自动识别 shell 与 OS
- 内置 25+ LLM 提供商适配与任意 OpenAI 兼容端点
- Function Calling 与 MCP 工具支持，工具调用前逐次确认
- 图像输入（本地文件/URL/多图）与流式输出、持久历史

## 适用场景

- 在终端里与 LLM 对话或快速提问，不离开工作流
- 让 AI 生成并执行 shell 命令（执行前确认）
- 通过管道把日志或文件内容交给 AI 分析
- 用 Function Calling/MCP 工具在 CLI 中扩展 AI 能力

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L12: YAICLI is a powerful yet lightweight command-line AI assistant that brings the capabilities of Large Language Model
> L29: - **💬 Chat Mode**: Engage in persistent conversations with full context tracking
> L30: - **🚀 Execute Mode**: Generate and safely run OS-specific shell commands

## 星数曲线

```mermaid
xychart-beta
    title "belingud/yaicli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `69a862540074` · [字段定义](../../DATASET.md)*
