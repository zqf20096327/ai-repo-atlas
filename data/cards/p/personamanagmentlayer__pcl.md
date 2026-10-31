# personamanagmentlayer/pcl

⭐ 44 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/personamanagmentlayer/pcl) · [官网](https://pclang.org) · 组织维护

**面向企业治理的 AI 人设与多智能体编排编程语言**

PCL 是一种治理优先的编程语言（TypeScript 实现），用于定义 AI persona 的能力、约束与风险分级，编排带人工监督的多智能体工作流，并通过不可变日志对齐 ISO 27001/42001、EU AI Act、OWASP LLM 等合规框架。支持 8 个 AI 提供商（Claude、GPT、Gemini、DeepSeek、Ollama、Azure、Bedrock、Mock），提供 LSP、MCP、技能生态兼容、4 种 Registry 后端与多目标代码生成。README 自述为‘接近生产就绪’（78/100），尚未面向高风险受监管系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 声明式定义 persona 的能力、约束与风险分类
- 支持 8 个 AI 提供商（Claude/GPT/Gemini/DeepSeek/Ollama/Azure/Bedrock/Mock）
- LSP、MCP、技能生态（兼容 agentskills.io 与 Claude Code）与 4 种 Registry 后端
- 多目标代码生成：TypeScript/Python/JSON/YAML/Markdown

## 适用场景

- 为企业 AI 系统统一定义与治理多个 agent persona
- 让 AI 行为对齐 ISO/EU AI Act 等合规框架并留存审计日志
- 用一份 PCL 定义跨多家 LLM 提供商部署 agent

## 场景标签

`多智能体` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L25: **PCL (Persona Control Language)** is a **governance-first programming language** for AI persona management and mul
> L33: - **Orchestrate** complex multi-agent workflows with human oversight

## 星数曲线

```mermaid
xychart-beta
    title "personamanagmentlayer/pcl 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 42 --> 45
    line [44, 43, 44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1559b7c5e59d` · [字段定义](../../DATASET.md)*
