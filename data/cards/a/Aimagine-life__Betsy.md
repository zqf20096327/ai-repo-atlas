# Aimagine-life/Betsy

⭐ 10 · TypeScript · MIT · 推送 2026-05-25 · [GitHub](https://github.com/Aimagine-life/Betsy) · 组织维护

**自托管于服务器的个性化 AI 伴侣，无需代码即可配置**

Betsy 是部署在自有服务器上的自主 AI agent：通过 YAML 配置设置姓名、性别、语气与自定义指令来定义人格，支持 Telegram 与内置浏览器作为对话渠道。核心机制包括基于 OpenRouter 的多模型配置与余额耗尽时自动切换免费模型的 fallback 链、从对话中提取事实存入知识库的记忆系统、多步 agent 工具循环（11 个内置工具），以及语音回复、口型同步视频、自拍生成等多模态输出。运行要求 Node.js 20+ 与 OpenRouter API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个内置工具：shell、文件、HTTP、浏览器、记忆、调度、npm 自扩展等
- 多模型 fallback 链：余额耗尽时自动切换 OpenRouter 免费模型
- 对话记忆与事实提取存入知识库，重启后保留
- 语音回复（MiniMax/ElevenLabs）、口型同步视频与自拍生成（fal.ai）

## 适用场景

- 在自有服务器上搭建带人格与长期记忆的私人 AI 伴侣
- 通过 Telegram 让 AI 执行日程提醒、网页检索、文件管理等日常任务
- 自定义角色人格（语气、风格、头像）用于工作或闲聊

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L17: Betsy is an **autonomous AI agent** that lives on your server. She has her own personality, voice, face — and she g
> L78: Balance ran out? Automatically switches to free models via OpenRouter. Cycles through a chain of models until it fi
> L91: Doesn't just answer questions — **does things**. Multi-step agentic loop: gets a task → calls tools → checks result

## 星数曲线

```mermaid
xychart-beta
    title "Aimagine-life/Betsy 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `7f1260151f5a` · [字段定义](../../DATASET.md)*
