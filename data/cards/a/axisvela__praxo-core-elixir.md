# axisvela/praxo-core-elixir

⭐ 3 · Elixir · MIT · 推送 2026-11-27 · [GitHub](https://github.com/axisvela/praxo-core-elixir) · [官网](https://axisvela.github.io/praxo-core/languages/elixir/) · 组织维护

**Elixir 可嵌入式 AI agent 框架：策略、工具、事件、检查点**

PRAXO-CORE 的原生 Elixir 实现（镜像仓库），以 Hex 包 `praxo_core` 发布，MIT 许可。提供 agent 循环、上下文压缩、内存存储、路径策略、检查点白名单、工具调用解析，以及可选的工具选择、PII 脱敏、结构化输出校验、调用上限和人工中断决策。内置 OpenAI 兼容、Anthropic、Gemini 模型接入与 MCP 客户端，支持子 agent 委托与检索器。在 Elixir 1.20.4 / Erlang/OTP 29 上通过共享向量组验证，但 README 声明向量覆盖不等于完全对等或生产就绪。

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

- 原生内置 OpenAI 兼容、Anthropic、Gemini 三类模型接入（SSE 流式重组）
- MCP 客户端支持 stdio 与 Streamable HTTP 传输
- 策略治理：路径策略、身份策略、PII 脱敏、调用上限、人工审批中断
- 检查点白名单与会话历史保存/恢复

## 适用场景

- 在 Elixir/OTP 服务中嵌入带策略治理的 agent 循环
- 构建需要人工审批写操作的工作流
- 接入 MCP 工具服务器并做工具调用解析
- 对多模型端点做故障转移与重试

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native Elixir Core with source tag `e
> L23: - OpenAI-compatible model: native
> L129: PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-o


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `513809cd9dc0` · [字段定义](../../DATASET.md)*
