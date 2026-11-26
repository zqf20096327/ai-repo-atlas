# axisvela/praxo-core-delphi

⭐ 3 · Pascal · MIT · 推送 2026-11-25 · [GitHub](https://github.com/axisvela/praxo-core-delphi) · [官网](https://axisvela.github.io/praxo-core/languages/delphi/) · 组织维护

**Delphi/Free Pascal 可嵌入 AI agent 框架：内置工具、策略与检查点**

以 Object Pascal 实现的进程内 agent 框架核心，提供 agent loop、工具调用、策略控制、记忆、事件、检查点、上下文与中间件辅助。原生适配 OpenAI 兼容、Anthropic、Gemini 三类模型接口，内置 MCP 客户端、OpenTelemetry/Harmovela 事件 sink、子 agent 委托与检索器。通过 OPM 包或发布归档安装，附 14 个可运行示例与场景教程；仓库为规范 monorepo 的发现镜像，声明自身非托管模型、工作流引擎或安全控制器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 进程内 agent loop：工具、策略、记忆、事件、检查点一体化
- OpenAI 兼容/Anthropic/Gemini 模型接口均为原生适配，支持 SSE 流式重组
- 原生 MCP 客户端（stdio 与 Streamable HTTP 传输）
- 14 个可运行示例与场景教程，含 HITL、委派治理、结构化输出校验

## 适用场景

- 在 Delphi/Free Pascal 应用中嵌入带策略控制的 agent 能力
- 接入 OpenAI/Anthropic/Gemini 接口并做 provider 回退与重试
- 通过 MCP 客户端连接工具服务
- 用检查点保存与恢复多轮会话历史

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native Delphi / Free Pascal Core: an 
> L22: - OpenAI-compatible model: native
> L117: PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-o


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `23349b8aefc7` · [字段定义](../../DATASET.md)*
