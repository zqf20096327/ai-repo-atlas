# axisvela/praxo-core-r

⭐ 3 · R · MIT · 推送 2026-11-27 · [GitHub](https://github.com/axisvela/praxo-core-r) · [官网](https://axisvela.github.io/praxo-core/languages/r/) · 组织维护

**R 语言的嵌入式 AI agent 框架，含工具与策略**

PRAXO-CORE 的 R 实现：以进程内 agent loop 形式嵌入应用，提供工具调用、policy 治理、事件、memory、checkpoint、middleware 与 JSON Schema 校验，基于 base R 编写。原生适配 OpenAI-compatible、Anthropic、Gemini 模型接口及 MCP client，支持 SSE 流式重组、子 agent 委派与检索器。安装来源为 r-universe（CRAN 未发布），提供 16 个可运行示例与场景教程，含人类审批（hitl）、身份策略绑定、provider fallback 等治理能力。明确声明非托管模型、非工作流引擎。

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

- 进程内 agent loop：tools、policy、events、memory、checkpoint、middleware
- OpenAI-compatible 模型原生支持，含 SSE 流式重组；Anthropic/Gemini 为 transport seam
- MCP client 与 subagent 同步委派、检索器能力
- 人类审批工具（hitl）与基于可信主体的 policy 决策绑定

## 适用场景

- 在 R 应用中嵌入带策略治理的 agent 循环
- 接入 OpenAI-compatible 端点并注册工具调用
- 需要人类审批的写操作 agent 流程
- 跨回合保存与恢复会话 checkpoint

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native R Core: an in-process agent lo
> L23: - OpenAI-compatible model: native


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `dc639e2a9aa5` · [字段定义](../../DATASET.md)*
