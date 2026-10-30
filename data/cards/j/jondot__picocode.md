# jondot/picocode

⭐ 63 · Rust · MIT · 推送 2026-01-30 · [GitHub](https://github.com/jondot/picocode) · 个人维护

**Rust 编写的轻量 CLI 编码 agent，支持多 LLM 接入**

picocode 是用 Rust 基于 Rig 库构建的命令行编码 agent：提供交互聊天、单次提示与基于 picocode.yaml 的 Recipes 非交互执行（面向 CI/CD 与小规模代码修改）。支持 Anthropic、OpenAI、DeepSeek、Gemini、Ollama 等多家 LLM 提供方切换；内置文件、搜索、bash、浏览器自动化等工具，破坏性操作默认需人工确认；另提供 15 种专家人格切换与本地 AGENTS.md 自定义指令。可作为 CLI 工具或 Rust 库使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Rust 二进制，通过 Rig 接入 Anthropic/OpenAI/DeepSeek/Gemini/Ollama 等多家 LLM
- picocode.yaml Recipes 支持非交互自动化执行（CI/CD）
- 文件读写/编辑、grep/glob、bash、浏览器自动化等工具集，破坏性操作默认需确认
- 可作为 CLI 使用，也可作为 Rust 库集成

## 适用场景

- 在 CI 流程中自动执行代码审查或小规模代码修改
- 交互式地在终端里让 AI 读写文件、运行命令完成编码任务
- 在 Rust 项目中以库形式嵌入自己的 agent 能力

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4: **picocode** is a minimal, high-performance Rust-based coding agent. It's a small, robust tool designed for develope
> L22: - **Multi-LLM Sovereignty**: Works with Anthropic, OpenAI, DeepSeek, Google (Gemini), Ollama, and many more via Rig
> L53: Picocode supports named **Recipes** in a `picocode.yaml` file for non-interactive execution (CI/CD, automation).

## 星数曲线

```mermaid
xychart-beta
    title "jondot/picocode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-30 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `eae84ee23fe4` · [字段定义](../../DATASET.md)*
