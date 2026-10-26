# memex-lab/dart_agent_core

⭐ 46 · Dart · MIT · 推送 2026-10-20 · [GitHub](https://github.com/memex-lab/dart_agent_core) · [官网](https://memexlab.ai) · 组织维护 · 中文 README

**Dart/Flutter 的有状态 AI Agent 开发与评测库**

面向移动优先、本地优先场景的 Dart 库，用纯 Dart 实现完整 Agent 循环：工具调用、流式输出、规划（write_todos）、子 Agent 委派、上下文压缩、循环检测、多轮记忆与状态持久化，并内置 Agent 评测套件（任务、评分器、record/replay、pass@k/pass^k 指标）。通过统一 LLMClient 接入 OpenAI、Gemini、Claude（直连与 AWS Bedrock）及 OpenAI 兼容 API（Kimi、Qwen、GLM、Ollama、OpenRouter 等），支持 MCP、多模态输入与 SKILL.md 文件技能，适用于无需 Python/Node 后端的 Flutter 应用。

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

- 统一 LLMClient 接入 OpenAI/Gemini/Claude 及 OpenAI 兼容 API
- 纯 Dart 实现 Agent 循环：工具调用、规划、子 Agent 委派、上下文压缩
- Agent 评测套件：graders、record/replay、pass@k/pass^k
- MCP stdio/Streamable HTTP 接入与 SKILL.md 文件技能系统

## 适用场景

- 在 Flutter 应用中内建带工具调用的有状态 AI Agent
- 连接本地 Ollama 或多家乡土模型 API 构建移动端 Agent
- 为 Dart Agent 代码运行评测与回归测试

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A mobile-first, local-first Dart library for building and evaluating stateful, tool-using AI agents**
> L11: `dart_agent_core` is a mobile-first, local-first Dart library that implements a full agentic loop with tool use, st

## 星数曲线

```mermaid
xychart-beta
    title "memex-lab/dart_agent_core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 45 --> 48
    line [47, 46, 46]
```

2026-10-18 47 → 2026-10-26 46（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6eff05e8e723` · [字段定义](../../DATASET.md)*
