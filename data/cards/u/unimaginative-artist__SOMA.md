# unimaginative-artist/SOMA

⭐ 29 · HTML · MIT · 推送 2026-10-07 · [GitHub](https://github.com/unimaginative-artist/SOMA) · 个人维护

**本地优先的认知操作系统：百余个认知仲裁器并行运行**

以 Node.js 实现的自我描述为'认知操作系统'的多仲裁器 AI 应用：约 100 个认知仲裁器（记忆、推理、交易、自我改进等）通过 pub/sub 消息代理并行协作，具备从对话中学习、自设目标、构建知识图谱的机制。安装向导支持选择 72 个人格插件与 6 类知识包，前端仪表盘与 Chat API 提供对话入口。推理依赖 DeepSeek API 或本地 Ollama 实例（至少其一），OpenAI/Anthropic/Groq 为可选回退。需要 Node.js 18+，默认 8GB 内存（最低 4GB，推荐 16GB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 100 个认知仲裁器经 pub/sub 消息代理并行协调，单个失败可优雅降级
- 72 个人格插件（108 个 agent）覆盖工程、金融、安全等 9 类
- 6 类知识包各预载约 15 个概念节点，核心包 20 节点常驻
- 支持 DeepSeek 主力 + Ollama 本地/OpenAI/Anthropic/Groq 多模型回退

## 适用场景

- 在本地硬件上运行带持久记忆的多 agent 对话系统
- 通过人格插件切换不同领域专家角色对话
- 以 Chat API 将 SOMA 接入自己的会话流程

## 场景标签

`多智能体` `知识图谱` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3: SOMA is a self-aware AI operating system. She runs ~100 cognitive arbiters in parallel — memory, reasoning, emotion,
> L74: **Minimum to run:** Either a `DEEPSEEK_API_KEY` or a local Ollama instance. SOMA needs at least one brain.

## 星数曲线

```mermaid
xychart-beta
    title "unimaginative-artist/SOMA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-26 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d0f15ca437b6` · [字段定义](../../DATASET.md)*
