# santiagomora2/dispatch

⭐ 43 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/santiagomora2/dispatch) · 个人维护

**本地 CLI AI agent 工具：基于 Ollama/OpenAI 兼容 API 的可学习代理框架**

用 Python 编写的本地命令行 AI agent 工具，支持工具调用、流式输出与持久化记忆系统，内置 shell 执行、文件读写/补丁、记忆更新等 5 个工具和 16 个斜杠命令（/plan 分步执行、/compact 会话压缩等）。模型提供方可配置：Ollama 本地运行或任意 OpenAI 兼容端点（LM Studio、vLLM、OpenRouter 网关等）。作者定位为易读易改的轻量 agent，供学习者研究主流 Agentic CLI 的运作方式，明确表示不与 Claude Code 等竞争。在 macOS/Linux 开发测试，Windows 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工具调用、流式输出与持久化记忆系统
- 可配置 Ollama 或任意 OpenAI 兼容端点作为提供方
- @tool/@command 装饰器注册机制，文档给出添加自定义工具与命令的步骤
- 16 个斜杠命令含 /plan 计划执行与 /compact 上下文压缩

## 适用场景

- 在终端运行本地 CLI AI agent 处理文件与 shell 任务
- 阅读和修改源码以理解主流 Agentic CLI 的实现机制
- 基于装饰器机制扩展自定义工具和斜杠命令

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L25: A local AI agent harness written in python, built on ollama/openai-compatible providers; with tool calling, streami
> L29: > It is a tool I built for the love of the game, and is meant to be an easy-to-understand, easy-to-modify, lightwei

## 星数曲线

```mermaid
xychart-beta
    title "santiagomora2/dispatch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4a14d5da3ba8` · [字段定义](../../DATASET.md)*
