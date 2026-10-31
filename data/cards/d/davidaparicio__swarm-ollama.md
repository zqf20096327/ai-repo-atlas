# davidaparicio/swarm-ollama

⭐ 24 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/davidaparicio/swarm-ollama) · [官网](https://github.com/openai/swarm) · 个人维护

**给开发者的本地多智能体编排框架，基于 Ollama 离线运行**

OpenAI Swarm 的教育性框架封装，将底层调用替换为 Ollama，实现离线的轻量级多智能体编排。核心抽象为 Agent 与 handoff：Agent 封装指令与工具，可在对话中将执行移交给其他 Agent；函数自动转为 JSON Schema 传给工具调用，支持流式输出与上下文变量。默认模型 llama3.2:3b，需工具支持的模型，可通过 base_url 连接远程 Ollama。README 明确标注为实验性、非生产用途、无官方支持。提供 Python 包经 git 安装，附多个示例工程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent + handoff 双原语实现多智能体编排与移交
- 底层封装 Ollama，可离线运行，默认模型 llama3.2:3b
- 函数自动转 JSON Schema 供工具调用，支持流式输出与上下文变量
- 附 basic/triage_agent/airline/support_bot 等示例工程

## 适用场景

- 学习和实验多智能体编排的 handoff 与 routines 模式
- 在本地离线环境跑带工具调用的多 Agent 应用
- 构建分诊、客服等需要 Agent 间移交的对话流程原型

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: The educational framework lightweight multi-agent orchestration with the Ollama wrapper.
> L87: Start by instantiating a Swarm client (which internally just instantiates an `Ollama` client).

## 星数曲线

```mermaid
xychart-beta
    title "davidaparicio/swarm-ollama 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [25, 24, 24]
```

2026-10-18 25 → 2026-10-31 24（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2ae2e223f61d` · [字段定义](../../DATASET.md)*
