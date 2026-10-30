# monkey-sking/ai-memory-hub

⭐ 22 · JavaScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/monkey-sking/ai-memory-hub) · [官网](https://amh-hub.app.workbuddy.host/) · 个人维护 · 中文 README

**多 AI 编码工具共享的本地记忆与协调层**

面向同时使用多个 AI 编码工具（Claude Code、Codex、Gemini CLI 等）的开发者的本地优先共享层：所有 agent 通过同一 CLI 读写存于 ~/.ai-memory 的记忆、消息与任务。提供 FTS5 全文检索（支持 CJK）、跨工具消息总线、共享任务队列、多角色工作流、审批门与派发机制，附本地 React 仪表盘。不做 LLM 代理、不读其他工具的密钥、不依赖 MCP 和云。需 Node 24+，从源码安装，npm 同名包为无关项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨工具共享记忆（core/working/archive 三层，FTS5 全文，支持 CJK）
- Agent radio 跨工具消息与 replyTo 线程化回复
- 共享任务队列（open→claimed→in_progress→blocked→done）与审批门
- 纯 CLI 即可用，不依赖 MCP、不依赖云端

## 适用场景

- 让 Codex 与 Claude Code 等工具共享会话间的记忆与决策记录
- 多 agent 并行开发时协调任务分配与交接
- 在不接入云端服务的前提下为多个 AI 编码工具建立共享状态

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L30: AMH is a local-first ledger + coordination bus that sits *under* your AI tools.
> L78: amh search "<what am I working on>"     # read before you act

## 星数曲线

```mermaid
xychart-beta
    title "monkey-sking/ai-memory-hub 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c724b86b3e37` · [字段定义](../../DATASET.md)*
