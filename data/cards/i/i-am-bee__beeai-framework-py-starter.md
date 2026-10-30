# i-am-bee/beeai-framework-py-starter

⭐ 32 · Python · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/i-am-bee/beeai-framework-py-starter) · 组织维护

**BeeAI 框架 Python 项目起步模板：快速搭好 agent 开发环境**

由 i-am-bee 维护的 Python 起步模板，基于 uv 包管理与容器化服务，帮助开发者快速启动 BeeAI 框架的 agent 开发。内置 BeeAI Code Interpreter 用于执行任意 Python 代码，带 linting 与 formatting 的完整工程配置。要求 Python 3.11+、容器系统（Docker/Rancher/Podman）与 LLM Provider（外部 WatsonX/OpenAI/Groq 或本地 Ollama，需拉取 granite3.3:8b 模型）。附带 agent、代码解释器 agent、三角色多 agent 工作流示例，以及基于 OpenInference + Phoenix 的可观测性配置。项目自述状态为 Alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 BeeAI Code Interpreter 安全执行任意 Python 代码
- 基于 uv 的完整 Python 工程配置（含 linting 与 formatting）
- 内置 agent、代码解释器 agent、多 agent 工作流三类示例
- OpenInference + Phoenix 的 agent 可观测性接入

## 适用场景

- 快速搭建 BeeAI 框架的 Python agent 开发环境
- 体验带工具调用的 agent 与代码解释器 agent
- 搭建多 agent 协作工作流（研究/天气/汇总）
- 为 agent 运行接入 Phoenix 追踪观测

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: This starter template helps you **quickly** get started with the BeeAI framework for Python
> L7: - 🔒 Safely execute an arbitrary Python Code via BeeAI Code Interpreter.

## 星数曲线

```mermaid
xychart-beta
    title "i-am-bee/beeai-framework-py-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b69c50907cbf` · [字段定义](../../DATASET.md)*
