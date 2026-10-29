# InternScience/ResearchHarness

⭐ 50 · Python · MIT · 推送 2026-07-16 · [GitHub](https://github.com/InternScience/ResearchHarness) · [官网](https://huggingface.co/spaces/InternScience/ResearchHarness) · 个人维护 · 中文 README

**轻量通用工具调用 LLM agent 运行时：跑基准评测与个人助理**

面向工具调用 LLM agent 的基础 harness：单条 ReAct 主循环、显式 workspace 根目录、原生 OpenAI 兼容工具调用，提供文件读写、PDF/图像读取、shell 执行与持久终端等工具。支持以 Python 包、CLI 或 /v1/chat/completions API 服务方式部署，接入 GPT、Gemini、Qwen、GLM 等 OpenAI 兼容模型；附上下文压缩、JSONL trace 记录与本地聊天 UI。定位明确为基准评测底座（如 ResearchClawBench）、harness 研究基线与轻量个人助理运行时，不做工作流引擎或多租户平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 ReAct 主循环 + 显式 workspace 的轻量执行底座
- 可部署为 OpenAI 兼容 /v1/chat/completions agent 后端服务
- 内置上下文压缩与 JSONL trace（含 LLM 调用与压缩事件）
- 可作基准评测执行底座与 harness 优化研究的 meta harness

## 适用场景

- 给 agent 基准（如 ResearchClawBench）提供可复现的公平运行时
- 让现有 OpenAI SDK 客户端直接调用工具型 agent 后端
- 日常编码、文件处理与报告写作的本地个人 agent
- 作为 harness 研究的参考基线做提示词/循环策略优化

## 场景标签

`Agent 框架` `模型评测` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L14: ResearchHarness is a foundational harness for running tool-using LLM agents on
> L124: - **OpenAI-compatible API serving**
> L147: ResearchHarness should be understood as a **base harness**: a small execution

## 星数曲线

```mermaid
xychart-beta
    title "InternScience/ResearchHarness 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27", "2026-10-29"]
    y-axis "stars" 48 --> 51
    line [50, 49, 50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `22eda4ef15ab` · [字段定义](../../DATASET.md)*
