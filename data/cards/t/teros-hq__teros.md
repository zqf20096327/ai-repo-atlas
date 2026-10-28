# teros-hq/teros

⭐ 64 · TypeScript · NOASSERTION · 推送 2026-08-06 · [GitHub](https://github.com/teros-hq/teros) · [官网](https://teros.ai) · 组织维护

**开源自托管 AI agent 运行平台：构建、运行带工具能力的智能体**

用 TypeScript/Node.js 编写、通过 Docker Compose 自托管部署的 AI agent 平台。Agent 具有持久记忆与人格，通过 MCA（Model Context Apps）工具包获得能力：内置 43 个 MCA，覆盖 Gmail、GitHub、Sentry、Linear、文件系统、bash、Playwright 等。支持 Anthropic/OpenAI/OpenRouter/Ollama/Zhipu 等多种 LLM 后端，每个 agent 可用不同模型；工作区内多 agent 可共享上下文协作。前端为 React Native (Expo)，数据库用 MongoDB 7.0；提供一键安装脚本与 MCA SDK 供自定义工具开发，运行要求 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 43 个 MCA 工具包（邮件、日历、GitHub、Sentry、bash、文件系统等）
- 支持 Anthropic/OpenAI/OpenRouter/Ollama/Zhipu 等 LLM 后端，每 agent 可配不同模型
- 工作区内多 agent 共享上下文与看板任务管理
- 提供 MCA SDK 与目录结构约定用于自定义工具开发

## 适用场景

- 自托管运行能操作 GitHub、Linear、日历等服务的自动化 agent
- 搭建多 agent 协作处理开发工作流的工作区
- 为团队构建带真实工具调用能力的私有 AI agent 平台

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L33: Teros is an open-source platform for building and running **AI agents with real tool capabilities**. Think of it as
> L53: LLM backends. Teros supports Anthropic, OpenAI, OpenRouter, Ollama (local), Zhipu, and OAuth-based providers like C

## 星数曲线

```mermaid
xychart-beta
    title "teros-hq/teros 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-28 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d75b5de7fe1c` · [字段定义](../../DATASET.md)*
