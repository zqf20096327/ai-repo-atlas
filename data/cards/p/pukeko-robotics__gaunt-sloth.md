# pukeko-robotics/gaunt-sloth

⭐ 16 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/pukeko-robotics/gaunt-sloth) · [官网](https://gauntsloth.app) · 组织维护

**配置驱动的命令行 AI 编码助手：代码审查、PR 分析与问答**

Gaunt Sloth（命令 gth）是基于 LangChain.js 的命令行 AI 助手，面向开发者提供代码审查、PR 分析、问答与交互式编码会话。用户自带 API key 选择模型与提供商（Anthropic、OpenAI、Google、Ollama 等），全部提示词为可编辑 markdown，支持自定义工具、MCP 服务器与 A2A。状态无关的代码审查可接入 CI。以 pnpm monorepo 组织，npm 全局安装需 Node.js 24+，macOS/Linux 可用 Homebrew，核心包也可作为依赖嵌入其他项目。MIT 许可。

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

- 全部提示词为可编辑 markdown，无厂商锁定
- 支持自定义 shell 工具、MCP 服务器（含远程 OAuth）与 A2A 对接
- gth batch/eval 跨模型与输入矩阵运行并输出 JUnit/TeamCity 报告
- 核心库以 workspace 包形式发布，可作为项目依赖嵌入

## 适用场景

- 在 CI 中对 PR 做基于关联 GitHub/Jira issue 的代码审查
- 本地对任意模型提问、聊天和带文件系统访问的编码会话
- 跨多个模型/提供商做批量实验与评测

## 场景标签

`代码审查` `AI 助手` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L4: Gaunt Sloth (`gth`) is a command-line AI assistant for code review, PR analysis, Q&A, and
> L44: A **configuration-driven CLI** you wire into your own workflows — you choose the model, provider,

## 星数曲线

```mermaid
xychart-beta
    title "pukeko-robotics/gaunt-sloth 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6d60048816a0` · [字段定义](../../DATASET.md)*
