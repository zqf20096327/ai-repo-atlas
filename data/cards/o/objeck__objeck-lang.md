# objeck/objeck-lang

⭐ 167 · C++ · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/objeck/objeck-lang) · [官网](https://objeck.org) · 个人维护

**带内置 Agent/MCP 与本地模型支持的面向对象编程语言及 JIT 运行时**

Objeck 是一门面向对象与函数式编程语言，配套 JIT 编译的虚拟机（AMD64/ARM64）。v2026.11.4 引入 AI agent 工具链：函数经 `@tool` 文档注释声明即成为 MCP 工具，`obr --mcp` 以 stdio 或 HTTP 提供 MCP 服务器，`API.Agent` 提供 provider 无关的工具调用循环（取消、预算、AgentScope 限界），并通过 OllamaBackend 运行本地模型。标准库含 ML（梯度提升、时序）、NLP、计算机视觉（OpenCV）与 ONNX GPU 推理。各平台提供 .deb/.msi/.pkg/.tgz 安装包，另有浏览器 Playground。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `@tool`/`@resource`/`@prompt` 注释声明即编译为 MCP 工具与 JSON Schema
- provider 无关的 agent 循环，支持 Ollama 本地模型（无需 API key）
- 内置 ML/NLP/计算机视觉/ONNX GPU 推理库，无需第三方包
- REPL、LSP（VSCode/Sublime/Kate）、DAP 调试器与在线 Playground

## 适用场景

- 用注释声明将函数发布为 MCP 服务器供 Claude Code/Claude Desktop 调用
- 在本地 Ollama 模型上运行带预算与取消机制的 agent 循环
- AI/ML 原型、计算机视觉与 Web 服务的快速开发
- 跨平台（x64/ARM64，含树莓派）部署小型编译型应用

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L21: A function is a tool, a program is an MCP server, and an agent is a loop with limits. A doc comment with `@tool` is
> L44: - 🏠 **Local or hosted models**: Ollama (no key), Anthropic, OpenAI, Gemini, ONNX, OpenCV — no third-party packages
> L242:  * **A toolkit for AI agents** &mdash; `API.Agent` is a provider-neutral tool-use loop for Claude, OpenAI, Gemini 

## 星数曲线

```mermaid
xychart-beta
    title "objeck/objeck-lang 星数(近 3 点)"
    x-axis ["2026-11-22", "2026-11-26", "2026-11-28"]
    y-axis "stars" 165 --> 168
    line [166, 167, 167]
```

2026-11-22 166 → 2026-11-28 167（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a9f2a1a3396f` · [字段定义](../../DATASET.md)*
