# Prism-Shadow/model-message-stream-protocol

⭐ 116 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/Prism-Shadow/model-message-stream-protocol) · [官网](https://mmsp.penguin.ooo/) · 个人维护

**统一接入 1000+ LLM 的消息流协议 SDK（Python/TS）**

MMSP 提供 Python 与 TypeScript SDK，用统一的消息格式（UniMessage）与流式事件语法（UniEvent）调用多家模型服务商：官方客户端对接 OpenAI/Anthropic/Google/Z.AI/Moonshot/DeepSeek/MiniMax 等原生 API，协议客户端（openai-chat/openai-responses/ant-messages 等）可指向任意兼容端点，包括 vLLM、OpenRouter、SiliconFlow。AutoLLMClient 支持零代码切换模型，有状态/无状态两种流式接口，内置按 trace_id 的执行追踪，无需数据库。另提供模型清单查询（含价格）与 Codex/Claude Code 技能文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一消息格式与流式语法覆盖多家服务商与兼容网关
- AutoLLMClient 零代码切换模型，模型 id 前缀自动路由客户端
- 单一 trace_id 参数实现 LLM 执行追踪，无需数据库
- 自动处理多步工具调用中的交错思考

## 适用场景

- 在多模型之间切换而不改业务代码
- 统一 Agent 开发中不同 LLM 的调用接口
- 调试与审计 LLM 执行过程

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: MMSP, the Model Message Stream Protocol, takes the per-provider differences off a developer's mind: one message for
> L60: `AutoLLMClient` takes a model id and a `client_type`. An **official client** speaks its

## 星数曲线

```mermaid
xychart-beta
    title "Prism-Shadow/model-message-stream-protocol 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 112 --> 117
    line [113, 115, 116]
```

2026-10-18 113 → 2026-10-27 116（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6d73460bdb80` · [字段定义](../../DATASET.md)*
