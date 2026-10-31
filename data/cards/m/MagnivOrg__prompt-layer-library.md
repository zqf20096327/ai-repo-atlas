# MagnivOrg/prompt-layer-library

⭐ 785 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/MagnivOrg/prompt-layer-library) · [官网](https://www.promptlayer.com) · 组织维护

**面向开发者的提示词版本管理与 LLM 请求追踪 SDK（Python）**

PromptLayer 的官方 Python SDK：提供对 PromptLayer API 的访问，功能覆盖提示词模板获取/发布/缓存失效、请求日志与标注、工作流运行，以及基于 OpenTelemetry 的追踪。追踪开启后可自动对已安装的 OpenAI、Anthropic、Google GenAI、AWS Bedrock SDK 做自动埋点，并把 span 导出到 PromptLayer；另提供 OpenAI Agents 与 Claude Agents 的集成模块和表格 scorecard API。使用需要 PromptLayer API key，核心包支持 Python 3.9，自动埋点需 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提示词模板的获取/发布/列表与内存缓存（TTL、降级到过期缓存）
- OpenTelemetry 追踪并自动埋点 OpenAI/Anthropic/Google GenAI/Bedrock SDK
- 请求日志、标注（元数据/评分/分组）与工作流运行辅助方法
- 可包装 provider SDK 作为代理并记录请求到 PromptLayer

## 适用场景

- 在 Python 应用中管理提示词模板并做本地缓存渲染
- 为 LLM 调用添加追踪与请求日志，用于调试和监控
- 配合 Cursor/Claude Code 等 AI 编码代理安装文档技能与 MCP server

## 场景标签

`提示工程` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Version, test, and monitor every prompt and agent with robust evals, tracing, and regression sets.**
> L121: Note: When tracing is enabled, spans are exported to PromptLayer using OpenTelemetry.

## 星数曲线

```mermaid
xychart-beta
    title "MagnivOrg/prompt-layer-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 783 --> 786
    line [784, 785]
```

2026-10-18 784 → 2026-10-31 785（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1c3bf9d3fa30` · [字段定义](../../DATASET.md)*
