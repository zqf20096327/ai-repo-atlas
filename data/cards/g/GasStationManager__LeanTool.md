# GasStationManager/LeanTool

⭐ 87 · Python · GPL-3.0 · 推送 2026-01-16 · [GitHub](https://github.com/GasStationManager/LeanTool) · 个人维护

**让 LLM 直连 Lean 4 的“代码解释器”工具，辅助定理证明**

LeanTool 是连接 LLM 与 Lean 4 可执行程序的 Python 工具：LLM 通过工具调用提交 Lean 代码，得到可执行反馈并循环修正错误。借助 Pantograph 从 sorry 中抽取目标状态，以拆解复杂证明；附带针对 Lean 交互特性的系统提示。通过 LiteLLM 接入 OpenAI/Anthropic/OpenRouter 及 ollama、vLLM 本地模型，可用作 Python 库、命令行聊天、Streamlit 界面、OpenAI 兼容代理服务器或 MCP 服务器，适配 Cursor、Cline、Aider、Claude Code 等编码助手。安装依赖 elan、uv 与 lake/Mathlib。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 提交 Lean 代码并基于可执行反馈循环修错
- Pantograph 从 sorry 抽取目标状态，支持任务拆解
- 多种交付形态：Python 库/CLI/Streamlit/OpenAI 兼容 API/MCP 服务器
- 纯文本模式兼容不支持函数调用的推理模型（如 DeepSeek r1）

## 适用场景

- 让 AI 编码助手产出并验证 Lean 4 证明
- 自动化证明/形式化工作流中接入 Lean 反馈循环
- 通过 OpenAI 兼容 API 或 MCP 接入 Cursor、Cline、Claude Code 等工具

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: LeanTool is a simple utility that connects LLMs with a "Code Interpreter" for Lean. This is implemented as *tool cal
> L17: - Uses LiteLLM so you can plug in any compatible LLM, from OpenAI and Anthropic APIs to local LLMs hosted via ollam
> L25: - Flexible usage: as python library, as command-line chat interface, as OpenAI-compatible API server, or as Model C

## 星数曲线

```mermaid
xychart-beta
    title "GasStationManager/LeanTool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-24 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `79b4e05909d7` · [字段定义](../../DATASET.md)*
