# axisvela/praxo-core-perl

⭐ 3 · Perl · MIT · 推送 2026-11-22 · [GitHub](https://github.com/axisvela/praxo-core-perl) · [官网](https://axisvela.github.io/praxo-core/languages/perl/) · 组织维护

**Perl 嵌入式 AI agent 框架：agent 循环、工具分发与策略控制**

PRAXO-CORE 的 Perl 实现，一个可嵌入的 MIT 许可 agent 框架：提供 agent 循环、工具注册与分发、策略钩子、人工审批中断、类型化事件、内存与检查点、上下文预算、中间件、MCP 客户端、检索器与同步子 agent 委派、JSON Schema 校验及插件清单解析。原生适配 OpenAI 兼容、Anthropic、Gemini 模型端点，支持流式 SSE 重组。本仓库为发现镜像，规范源在 praxo-core 单体仓库。README 声明其非托管模型、工作流引擎或安全控制器，不保证 exactly-once 执行或沙箱隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 循环 + 工具注册分发 + 策略钩子与人工审批（HITL）
- 原生适配 OpenAI 兼容 / Anthropic / Gemini 端点，支持 SSE 流式重组
- MCP 客户端（stdio 与 Streamable HTTP）、检查点、事件 sink 与子 agent 同步委派
- CPAN 发布（cpanm Praxo::Core），附 conformance/测试脚本

## 适用场景

- 在 Perl 应用中嵌入带策略控制与人工审批的 agent 能力
- 需要 OpenAI 兼容/Anthropic/Gemini 多端点及失败回退的 agent 运行时
- 通过 MCP 客户端接入工具服务并做 JSON Schema 校验的结构化输出

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed AI agent framework. This distribution is its native Perl Core: an agent lo
> L11: |Install|`cpanm Praxo::Core`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `718b1696c9f3` · [字段定义](../../DATASET.md)*
