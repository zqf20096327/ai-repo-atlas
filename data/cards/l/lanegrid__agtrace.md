# lanegrid/agtrace

⭐ 62 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/lanegrid/agtrace) · 个人维护

**AI 编码 agent 的可观测性工具：实时查看 agent 行为与上下文**

面向 Claude Code 与 Codex 使用者的命令行观测工具：读取现有日志，零配置发现会话，以 TUI 展示多 agent 树（主 agent、teammates、子 agent、fork、Codex 子线程）及各自的上下文窗口占用、工具调用、compaction 与模型变更，并提供 agent 间消息流。支持浏览历史会话、跨会话搜索，可通过 MCP 让 agent 查询自身执行历史。限制：仅支持 Claude Code ≥ 2.1.24x 与 Codex ≥ 0.153，旧日志格式不支持；无法解码的行计为诊断并跳过。提供 npm 安装与 Rust SDK。

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

- 多 agent 实时树状视图，展示每个 agent 状态与上下文窗口占用
- 零配置：自动发现 Claude Code / Codex 现有日志
- MCP 集成：agent 可查询自身历史会话并检索过往错误
- 提供 Rust SDK（crates.io）供工具构建者集成

## 适用场景

- 我在用 Claude Code/Codex 时想实时看到 agent 在做什么、上下文用了多少
- 判断对话是否过长、agent 是否陷入循环，决定何时开新会话
- 让 agent 通过 MCP 检索昨天做过什么、过去的错误

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L28: - **Every agent at once**: the lead, its teammates, background subagents, forks, and Codex child threads, as one li
> L29: - **Live activity**: tool calls, spawns, compactions, and model changes of the selected agent as they happen
> L46: Works with Claude Code and Codex (OpenAI). Zero config: it discovers existing logs.

## 星数曲线

```mermaid
xychart-beta
    title "lanegrid/agtrace 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-30 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a6f711f5dadb` · [字段定义](../../DATASET.md)*
