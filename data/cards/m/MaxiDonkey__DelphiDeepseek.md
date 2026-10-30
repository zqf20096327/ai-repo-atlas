# MaxiDonkey/DelphiDeepseek

⭐ 99 · Pascal · MIT · 推送 2025-11-30 · [GitHub](https://github.com/MaxiDonkey/DelphiDeepseek) · 个人维护

**Delphi 的 DeepSeek API 封装库，含 LM Studio 本地模型支持**

用 Delphi 12 实现的 DeepSeek 公共 API 非官方封装库，MIT 许可，面向桌面、移动与服务器应用开发者。提供同步、异步、Await 与 Promise 链式调用，支持 deepseek-chat、deepseek-reasoner 模型的对话、流式输出、并行提示与函数调用；另可通过 LM Studio 的 OpenAI 兼容服务器加载本地模型运行。HTTP 层以依赖注入方式实现，便于测试打桩。不提供嵌入（Embeddings）API。附 VCL/FMX 示例模板与 TutorialHUB 教程中间件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Sync/Async/Await 与 Promise 链式调用模式
- deepseek-chat 与 deepseek-reasoner（推理模型）接入
- 经 LM Studio OpenAI 兼容服务器运行本地任意模型
- HTTP 层依赖注入，支持 mock 测试；附 VCL/FMX 示例工程

## 适用场景

- 在 Delphi 桌面/移动应用中集成 DeepSeek 对话能力
- 通过流式与多轮对话 API 构建聊天机器人或客服助手
- 用 LM Studio 在本地运行开源模型并经同一封装调用
- 以 Promise 链编排多步提示词处理流程

## 场景标签

 · 领域:LLM API 客户端库/软件开发

## 证据(README 行号)

> L22: **Deepseek for Delphi** is a powerful Delphi library that brings the latest Deepseek APIs to your desktop, mobile, 
> L37: > This repository contains `Delphi` implementation over Deepseek public API.

## 星数曲线

```mermaid
xychart-beta
    title "MaxiDonkey/DelphiDeepseek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 98 --> 100
    line [99, 99]
```

2026-10-18 99 → 2026-10-30 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `61cc41720821` · [字段定义](../../DATASET.md)*
