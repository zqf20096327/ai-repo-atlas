# iam-xiaofeng/SlotFlow

⭐ 24 · Python · 推送 2026-08-15 · [GitHub](https://github.com/iam-xiaofeng/SlotFlow) · 个人维护 · 中文 README

**本地优先的可扩展 AI agent 工作台：研究/编码/分析/报告**

FastAPI + LangGraph 后端与 Next.js 聊天界面构成的本地 agent 工作台，面向研究、编码、分析与报告生成流程。运行时通过 LiteLLM 发现已配置的模型提供商（DeepSeek/OpenAI/Anthropic 及 OpenAI 兼容中继），提供可见推理流、Skills、MCP 工具、长期记忆与本地 SQLite 持久化、Docker 沙箱代码执行、产物预览与子 agent 委派。推荐 Linux/WSL2 环境，经 bootstrap.sh + make dev 启动，另提供只读静态演示站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LiteLLM 运行时模型发现，支持 DeepSeek/OpenAI/Anthropic 及 OpenAI 兼容中继
- Skills、MCP 工具（含内置 Playwright MCP 预设）、长期记忆与 SQLite 持久化
- Docker 沙箱代码执行与产物发布（sandbox_exec / sandbox_artifact_copy）
- 分层子 agent 委派与可见推理流

## 适用场景

- 本地自托管一个能读文件、调工具、记上下文的 agent 工作台
- 编码、分析与报告生成工作流中让子 agent 并行执行任务
- 在沙箱中执行不受信任代码并预览生成的产物

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: SlotFlow is a local-first, extensible AI agent workspace. A FastAPI + LangGraph
> L16: It is designed for research, coding, analysis, and report-generation workflows where

## 星数曲线

```mermaid
xychart-beta
    title "iam-xiaofeng/SlotFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9e4abcf572ea` · [字段定义](../../DATASET.md)*
