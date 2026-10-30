# jamjet-labs/jamjet

⭐ 23 · Rust · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/jamjet-labs/jamjet) · [官网](https://jamjet.dev) · 组织维护

**AI agent 运行时安全层：拦截危险工具调用、审批、预算与审计**

面向 agent 开发者的运行时治理组件，置于 Claude Code、OpenAI Agents SDK、MCP 客户端、LangChain、Spring AI 等框架之下：用统一 policy.yaml 在运行时拦截不安全工具调用、对高风险动作暂停等待人工审批、按 agent/run/project 限额预算，输出 JSONL 审计日志，并支持从检查点恢复崩溃运行。底层为事件溯源的持久执行引擎，含会话记忆、多 agent 编排、评测与部署。提供 Python/Java/TypeScript SDK 与多种适配器；Java 运行时需 Java 21。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 policy.yaml 在运行时拦截/审批工具调用，适配 Claude Code hook、MCP shim、OpenAI guardrail 等多端
- 持久化执行：事件日志、检查点、崩溃后恢复与确定性重放
- 按 agent/run/project 的预算上限与 JSONL 审计日志
- 配套 Engram 记忆层（Rust crate / MCP server / Python 库 / Spring AI ChatMemoryRepository）

## 适用场景

- 阻止 agent 执行数据库删除、支付等危险操作
- 对高风险动作引入可持久化的人工审批环节
- 为多个框架的 agent 汇聚同一策略与统一审计视图
- 长时运行 agent 崩溃后从检查点恢复

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: JamJet sits underneath your agent (Claude Code, OpenAI Agents SDK, MCP clients, LangChain, CrewAI, ADK, Spring AI, 
> L22: - 🛡️ **Block unsafe tool calls** at runtime: database deletes, payments, file writes

## 星数曲线

```mermaid
xychart-beta
    title "jamjet-labs/jamjet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d14194e718eb` · [字段定义](../../DATASET.md)*
