# Ultimate-Multisite/superdav-ai-agent

⭐ 31 · PHP · GPL-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Ultimate-Multisite/superdav-ai-agent) · [官网](https://sdaiagent.com/) · 组织维护

**WordPress 站点的 AI Agent 插件：对话生成与管理站点内容**

以 WordPress 插件形式提供 agentic AI 助手：通过循环工具调用生成 Gutenberg 页面/区块、管理内容与媒体、审查 SEO、处理 WooCommerce 订单等，内置 28 个能力类。基于 WordPress 7.0 的 AI Client SDK 与 Abilities API，自动发现任何插件注册的工具；自带自定义 Agent、会话管理、记忆、技能、RAG 知识库与定时/事件驱动自动化。要求 PHP 8.2+ 与 WordPress 7.0+，zip 上传安装，GPL v2+ 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主工具调用循环，1-50 次迭代可配置，破坏性操作需确认
- 基于 Abilities API 自动发现站点内所有插件注册的工具
- 直连 OpenAI/Anthropic/Google 或任意 OpenAI 兼容端点，支持本地 Ollama
- 内置 RAG 知识库、记忆、技能与 Cron/事件驱动自动化

## 适用场景

- 用对话生成 Gutenberg 页面并做局部改写
- 让 Agent 日常巡查 SEO、站点健康并生成报告
- 给 WooCommerce 站点配置自动订单管理与内容准备
- 接入自有 API（HTTP/CLI 工具）扩展 Agent 能力

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L14: SD AI Agent is your AI teammate for the WordPress site you already run. Ask one assistant to improve content, prepa
> L51: - **AI Client SDK** — A unified interface for AI providers. Any connector plugin (OpenAI, Anthropic, Google, Ollama
> L131: - Autonomous tool-calling loop — the AI plans, executes tools, reads results, and iterates until the task is done

## 星数曲线

```mermaid
xychart-beta
    title "Ultimate-Multisite/superdav-ai-agent 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-24"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-11-20 31 → 2026-11-24 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `270770dc79f1` · [字段定义](../../DATASET.md)*
