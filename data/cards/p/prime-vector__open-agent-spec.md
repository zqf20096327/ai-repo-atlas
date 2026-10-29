# prime-vector/open-agent-spec

⭐ 20 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/prime-vector/open-agent-spec) · [官网](https://www.openagentspec.dev) · 组织维护

**YAML 声明式 AI agent 规范与 CLI：一次定义、多引擎运行**

用 YAML 定义 agent 的输入/输出 schema、prompt、模型配置与工具，通过 oa 命令直接运行或生成 Python 脚手架；输出不符 schema 时任务失败。每次运行输出归一化 token 用量与尽力估算成本，支持多引擎切换（OpenAI、Anthropic、Grok/xAI、Cortex、本地 Ollama/LM Studio/vLLM/llama.cpp、自定义类）、depends_on 多任务管道、MCP/原生/自定义工具、沙箱约束、行为契约与 OpenTelemetry 追踪，并提供 oa:// 托管 spec 注册表与 Node.js CLI。面向需要以代码化契约方式管理 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML spec 定义输入/输出 schema，输出不符合即验证失败
- 每次运行报告归一化 token 用量与尽力估算美元成本
- 一行切换引擎：OpenAI/Anthropic/Grok/xAI/Cortex/本地/自定义，多数引擎免 SDK
- 沙箱约束、行为契约、depends_on 管道与 oa:// spec 注册表

## 适用场景

- 把 agent 以 spec 文件形式纳入仓库并在 CI 中调用
- 在多个 LLM 提供商与本地模型之间切换而不改代码
- 追踪每个 agent 任务的 token 消耗与成本
- 通过沙箱与行为约束限制 agent 可调用的工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: Open Agent Spec lets you define an agent once in YAML, validate inputs and outputs against a schema, and either run 
> L327: Switch models by changing one line. All engines except Anthropic and Codex speak the OpenAI Chat Completions API o
> L332:   engine: openai       # openai | anthropic | grok | xai | cortex | local | codex | custom

## 星数曲线

```mermaid
xychart-beta
    title "prime-vector/open-agent-spec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2647ec2ec360` · [字段定义](../../DATASET.md)*
