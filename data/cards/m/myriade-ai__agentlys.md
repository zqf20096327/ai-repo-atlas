# myriade-ai/agentlys

⭐ 31 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/myriade-ai/agentlys) · 组织维护

**轻量 Python 库：把现有函数/类即刻变成 AI 工具**

Agentlys 是一个异步原生的 Python AI agent 库，核心约 500 行代码：通过 add_function 将函数注册为工具，将类的实例注册为有状态工具（__llm__() 方法注入状态供模型每轮读取），并支持工具延迟加载以减少上下文占用。支持 Anthropic（默认）等多 provider 与 MCP 集成，异步对话与单次调用均有 API。附 agentlys-dev 示例：15 行代码实现编码 agent。面向希望复用现有 Python 代码的开发者，不提供沙箱代码执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 函数与类实例一键注册为 AI 工具，__llm__() 注入状态
- 异步原生：run_conversation_async 与 ask_async
- 工具延迟加载（Tool Search），大工具集下减少 50-85% 上下文占用
- MCP 支持与多 provider（Anthropic 默认）

## 适用场景

- 把现有的数据库、文件系统等 Python 类直接接入 AI agent
- 构建工具数量多、需要按需发现工具的 agent
- 快速搭建小型编码 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Turn any Python class into an AI tool. Instantly.**
> L9: Async-native • MCP support • Multi-providers • ~500 lines of core code
> L34: pip install 'agentlys[all]'  # OpenAI + Anthropic + MCP

## 星数曲线

```mermaid
xychart-beta
    title "myriade-ai/agentlys 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2aae4916dd12` · [字段定义](../../DATASET.md)*
