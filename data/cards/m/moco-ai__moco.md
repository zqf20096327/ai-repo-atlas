# moco-ai/moco

⭐ 20 · Python · MIT · 推送 2026-01-31 · [GitHub](https://github.com/moco-ai/moco) · 组织维护

**多 Agent 编排框架：profile 配置协调多个 LLM Agent 执行任务**

Python 编写的轻量级多 Agent 编排框架，通过 YAML 与 Markdown 定义的领域 profile（如 14 个 Agent 的 development 团队）组织 Agent，以 delegate_to_agent 工具实现层级、并行、流水线、同行评审等组织模式。支持 Gemini、OpenAI、OpenRouter、Z.ai 多个 LLM 供应商切换，提供 CLI（moco run/chat）、Web UI、后台任务与会话管理、WhatsApp 移动接入，以及 FAISS 语义记忆、上下文自动压缩、护栏与 Docker 沙箱执行。安装方式为 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商支持：Gemini/OpenAI/OpenRouter/Z.ai 经环境变量或 CLI 切换
- profile 式配置定义领域 Agent 与工具，内置 development 等 14-Agent 开发团队
- 五种 Agent 组织模式：层级、多级层级、并行、顺序流水线、同行评审
- FAISS 语义记忆、上下文自动压缩、护栏与 Docker 沙箱执行、MCP 支持

## 适用场景

- 在终端或 Web UI 中以多 Agent 团队执行开发任务
- 通过 WhatsApp 远程调用本机 Agent 处理任务
- 按领域自定义 profile 组织自己的 Agent 分工结构

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Multi-provider, profile-based lightweight AI agent orchestration framework**
> L13: MOCO is an orchestration framework that supports multiple LLM providers (Gemini, OpenAI, OpenRouter, Z.ai) and allo

## 星数曲线

```mermaid
xychart-beta
    title "moco-ai/moco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b5fbb5f841ef` · [字段定义](../../DATASET.md)*
