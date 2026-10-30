# liruifengv/mini-agents

⭐ 17 · TypeScript · MIT · 推送 2026-02-26 · [GitHub](https://github.com/liruifengv/mini-agents) · 个人维护 · 中文 README

**极简 TypeScript Agent 框架与配套 CLI，供开发者构建 AI Agent**

由框架包 mini-agents 与命令行工具 mini-agents-cli 组成的 TypeScript 项目：框架提供 LLM 客户端（Anthropic/OpenAI/OpenAI Chat/Gemini 四类 provider）、Agent 执行循环、文件与 Shell 基础工具集、会话历史自动摘要、基于 MEMORY.md 的跨会话记忆、渐进式披露的 Skill 系统，以及可取消执行机制；CLI 可通过 npm 全局安装后交互使用，首次运行引导选择供应商并写入配置文件。框架可独立于 CLI 在项目中使用，参数校验依赖 Zod。

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

- 完整 Agent 执行循环，内置 read/write/edit/bash 等基础工具
- 支持 Anthropic、OpenAI、OpenAI Chat（兼容 Ollama/vLLM/DeepSeek 等）、Gemini
- 基于 MEMORY.md 的跨会话持久记忆与会话历史自动摘要
- 渐进式披露的 Skill 系统与执行取消机制

## 适用场景

- 在 TypeScript 项目中嵌入可调用工具的 LLM Agent
- 通过 CLI 快速体验多供应商的对话式 Agent
- 为 Agent 扩展自定义工具（基于 Zod 参数校验）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: - **mini-agents**: 可独立使用的 Agent 框架，提供 LLM 客户端、工具系统和 Agent 核心逻辑
> L70: **mini-agents** 是一个可独立使用的极简 Agent 开发框架

## 星数曲线

```mermaid
xychart-beta
    title "liruifengv/mini-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2fd63c980607` · [字段定义](../../DATASET.md)*
