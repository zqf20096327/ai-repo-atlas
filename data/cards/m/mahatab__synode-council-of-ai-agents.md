# mahatab/synode-council-of-ai-agents

⭐ 60 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/mahatab/synode-council-of-ai-agents) · 个人维护

**让多个 AI 模型组会讨论并由主模型给出结论的桌面应用**

基于 Tauri v2 + React 19 的 macOS/Windows 桌面应用。将多个模型组成委员会：顺序模式逐个接续发言，独立模式并行互不可见回答，再由指定主模型汇总为最终结论；另提供 Direct Chat 一对一模式、@提及追问、动态提示词生成、会话自动保存、token 用量与费用统计、Telegram bot 接入及四家供应商的联网搜索。云模型需自带各供应商 API key，本地模型经 LM Studio 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型委员会讨论（Sequential/Independent 两种模式）+ 主模型裁决
- 接入 8 家云供应商并通过 LM Studio 运行本地模型，可混合组会
- 裁决后 @ 任意成员追问，携带完整讨论上下文
- 按模型统计 token 用量与估算美元成本

## 适用场景

- 让多个模型从不同角度讨论一个问题再取综合结论
- 本地 LM Studio 模型与云模型混编同一讨论组
- 通过 Telegram bot 在手机上与模型委员会对话
- 追踪各供应商 API 调用的 token 消耗与成本

## 场景标签

`多智能体` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L18: Synode is a desktop app for **macOS and Windows** that assembles a **council of AI models** to collaboratively tack
> L32: - **8 cloud providers + local models** — Anthropic, OpenAI, Google, xAI, DeepSeek, Mistral, Together AI, Cohere, an
> L90: ### Local Models (LM Studio)

## 星数曲线

```mermaid
xychart-beta
    title "mahatab/synode-council-of-ai-agents 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-11-26 60 → 2026-11-28 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `181b18564b91` · [字段定义](../../DATASET.md)*
