# oujingzhou/build-your-own-openclaw

⭐ 23 · TypeScript · 推送 2026-03-18 · [GitHub](https://github.com/oujingzhou/build-your-own-openclaw) · 个人维护 · 中文 README

**面向开发者的教程：用 ~2,600 行 TypeScript 从零构建 AI 助手**

教程型仓库，分 12 章讲解如何用 TypeScript + ESM 从零实现一个精简版 OpenClaw（MyClaw）：覆盖 LLM 抽象与 Agent Loop、CLI 框架、Zod/YAML 配置、WebSocket 网关、通道抽象（Terminal/飞书/Telegram）、消息路由、插件与技能系统，每章附完整代码与设计分析。运行时支持 Anthropic/OpenAI/OpenRouter 三家 LLM 提供商，需 Node.js>=20 与至少一个 API Key。附与完整版 OpenClaw 的功能对比（通道 3 vs 23+、工具集差异等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 章教程覆盖 Agent 运行时、网关、多通道接入、插件与技能系统
- 支持 Anthropic / OpenAI / OpenRouter 三种 LLM 提供商
- 提供可运行的 CLI（onboard/agent/gateway/doctor 命令）
- 含飞书与 Telegram 外部通道接入实现

## 适用场景

- 学习 OpenClaw 类 AI 助手的核心架构模式
- 跟随章节构建一个可对话、可接飞书/Telegram 的自用 AI 助手
- 作为阅读完整 OpenClaw 源码前的过渡教材

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: **Build a OpenClaw from scratch in ~2,600 lines of TypeScript.**
> L9: This tutorial has 12 chapters, each focusing on a core module. It's recommended to read them in order. Each chapter 

## 星数曲线

```mermaid
xychart-beta
    title "oujingzhou/build-your-own-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `932200ed198b` · [字段定义](../../DATASET.md)*
