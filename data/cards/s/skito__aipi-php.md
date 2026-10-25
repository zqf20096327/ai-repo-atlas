# skito/aipi-php

⭐ 38 · PHP · Apache-2.0 · 推送 2026-05-04 · [GitHub](https://github.com/skito/aipi-php) · 个人维护

**面向 PHP 开发者的多厂商 AI 模型统一 API 客户端库**

纯 PHP 实现的轻量级库，为零依赖设计（仅要求 cURL 扩展），为 OpenAI、Anthropic、Google DeepMind、xAI 等厂商的模型提供统一接口，覆盖对话补全、视觉、图像生成、音频生成/转录、文档视觉、嵌入与内容审核等能力。支持通过 FunctionCall 工具实现 agentic 行为，可定义多个厂商与模型的回退链以在 API 失败时自动切换，并可通过继承 ModelBase 自行扩展模型。安装可用 composer、autoloader 或整包引入三种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多厂商统一 API：OpenAI/Anthropic/Google DeepMind/xAI 模型列表内置
- Fallback 机制：定义多个模型与厂商，API 失败时自动切换
- 工具调用支持（FunctionCall 与 Toolbox），实现 agentic 行为
- 零依赖纯 PHP 实现，仅要求 cURL，可通过继承 ModelBase 扩展模型

## 适用场景

- 在 PHP 项目中接入多家 AI 厂商而无需各自对接 SDK
- 为应用配置跨厂商的模型回退链提高可用性
- 构建带工具调用的 agentic 应用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Simple lightweight PHP library for interacting with common AI models, that provides universal interface.
> L10: 🤖 Multimodel support. Unified API for all models.
> L116: Currently supported: ``chat/completitions``, ``vision``, ``image generation``, ``audio generation``, ``audio trans

## 星数曲线

```mermaid
xychart-beta
    title "skito/aipi-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b8163d075e6e` · [字段定义](../../DATASET.md)*
