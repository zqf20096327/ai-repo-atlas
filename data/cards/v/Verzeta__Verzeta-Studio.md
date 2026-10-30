# Verzeta/Verzeta-Studio

⭐ 19 · C++ · NOASSERTION · 推送 2026-09-28 · [GitHub](https://github.com/Verzeta/Verzeta-Studio) · [官网](https://verzeta.com) · 个人维护

**本地优先的多 AI agent 团队工作区：多模型在同一对话协作**

基于 Qt 6 + Kirigami 的开源 AI 工作区应用，支持在单次对话中运行多个具名 agent，各自配置独立的提供商、模型、系统提示与工具白名单，通过 @mention 交接任务。内置 8 种 LLM 提供商（OpenAI/Claude/Gemini/OpenRouter/DeepSeek/Ollama/llama.cpp 等）及任意 OpenAI 兼容服务器。agent 可读写文件、运行沙箱 shell 命令、搜索网页、执行多步任务计划；支持 VS Code 与 Android 客户端经 WebSocket 连接。对话与设置存于本地，无遥测、无账户。GPL-3.0+/LGPL-3.0+/商业三重许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 群聊，每个 agent 独立提供商/模型/工具白名单
- 8 种内置 LLM 提供商 + 任意 OpenAI 兼容服务器（vLLM/LM Studio/Jan 等）
- VS Code 与 Android 客户端经 WebSocket (TLS) 连接主机
- 完整审计时间线：记录每次 agent 回合、工具调用、文件写入与投票

## 适用场景

- 让本地 Ollama 研究员、云端 Claude 写作者等在同一对话协作
- 在 VS Code 中让 agent 团队读写工作区文件并运行构建测试命令
- 无遥测、无账户地在本机离线运行多模型团队

## 场景标签

`多智能体` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L18: Verzeta Studio is an open-source AI workspace where several agents, each using its own model, role, and tools, work
> L26: - **Multi-agent group chats.** Several named agents per conversation, each with its own provider, model, system pro
> L27: - **Eight built-in LLM providers, plus any OpenAI-compatible server.** OpenAI, Anthropic (Claude), Google Gemini, O

## 星数曲线

```mermaid
xychart-beta
    title "Verzeta/Verzeta-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `74d9a865a7d8` · [字段定义](../../DATASET.md)*
