# zackham/aloop

⭐ 18 · Python · MIT · 推送 2026-09-18 · [GitHub](https://github.com/zackham/aloop) · 个人维护

**可嵌入的 Python agent 循环库，用于多 agent 编排与接入任意 LLM**

面向开发者嵌入自家项目的 Python agent 循环库（非交互式终端编码代理）：提供 run()/stream()/complete() API 与 CLI，支持 8 个已测试提供商（OpenRouter、OpenAI、Anthropic、Google、Groq、DeepSeek、xAI、Cerebras）及任意 OpenAI 兼容端点。关键机制：通过内置 agent 工具派生子代理（fork/fresh 两条路径），权限以配置声明（工具集+路径 glob，工具执行前强制校验），`aloop serve` 以 ACP over stdio 对接 Zed、JetBrains、Neovim 等编辑器；另有 10 个 hook 点、`@tool` 装饰器、持久会话与上下文压缩。自述为 ~8.5K LOC 的小型库，v0.6.0 版本，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 编排：fork/fresh 两种派生路径，spawnable_modes 白名单结构性阻止权限提升
- 权限声明在 .aloop/config.json：工具集切换、路径 glob 限制、执行前强制校验
- 内置 ACP server（stdio），对接 acpx、Zed、JetBrains、Neovim、Stepwise
- 8 个已测试提供商 + 任意 OpenAI 兼容端点，自定义提供商 4 行 JSON 添加

## 适用场景

- 把 LLM agent 能力作为库嵌入自己的 Python 项目
- 在 Zed/JetBrains/Neovim 中通过 ACP 使用 agent 做代码任务
- 构建需要权限隔离的多 agent 编排（只读模式不可调用写模式）
- 通过 CLI 做管道友好的一次性推理或脚本化 agent 任务

## 场景标签

 · 领域:LLM 基础设施/agent 框架

## 证据(README 行号)

> L3: An embeddable Python agent loop for **multi-agent orchestration**, **declarative permissions**, and **editor integra
> L73: aloop is a **library, not an interactive coding agent**. It's optimized for three specific use cases:
> L87: **Not a complete product.** No UI, no telemetry, no billing, no marketplace. aloop is a small library you embed and

## 星数曲线

```mermaid
xychart-beta
    title "zackham/aloop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `662c122db9ab` · [字段定义](../../DATASET.md)*
