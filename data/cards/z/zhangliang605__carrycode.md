# zhangliang605/carrycode

⭐ 44 · Rust · 推送 2026-03-15 · [GitHub](https://github.com/zhangliang605/carrycode) · [官网](https://carrycode.ai) · 组织维护 · 中文 README

**终端原生 AI 编程助手：对话式写码、重构、调试与理解代码**

以 Rust + Node.js 构建的终端 AI 编程 agent，通过自然语言对话完成代码编写、重构、调试与理解；提供 Build（自主生成/编辑代码）与 Plan（只读分析规划）双模式。接入 17+ LLM 提供商（OpenAI、Anthropic、Gemini、DeepSeek、Ollama、vLLM 及任意 OpenAI 兼容端点），支持 MCP 协议扩展、兼容 Claude Code 的 SKILL 体系、AGENTS.md 项目规则、LSP 诊断、会话管理与上下文压缩。安装提供一键脚本（macOS/Linux/Windows）、VSCode 扩展与源码构建三种途径；许可证附加 Logo/标识不得修改的使用条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 17+ LLM 提供商，含 Ollama/vLLM 本地模型与任意 OpenAI 兼容端点
- Build/Plan 双 agent 模式，read-only/agent/agent-full 三档审批控制
- 支持 MCP 协议扩展与兼容 Claude Code 的 SKILL 技能体系
- 终端 TUI：主题、语法高亮、diff 预览、Mermaid 图表渲染

## 适用场景

- 在终端通过对话让 AI 编写、重构或调试代码
- 接入本地 Ollama/vLLM 模型进行私有化代码辅助
- 通过 MCP 服务器与技能系统扩展 agent 能力
- CI 或脚本中以单次模式运行一次性代码任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: **CarryCode** is a terminal-native AI coding agent that helps you write, refactor, debug, and understand code — all
> L26: 3. 🔌 **17+ LLM Providers** — OpenAI, Claude, Gemini, DeepSeek, Kimi, GLM, MiniMax, Qwen, Grok, Ollama, vLLM, and an
> L78: On first launch, a **setup wizard** will guide you through:

## 星数曲线

```mermaid
xychart-beta
    title "zhangliang605/carrycode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c2a034c99165` · [字段定义](../../DATASET.md)*
