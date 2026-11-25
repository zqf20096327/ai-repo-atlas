# kirder24-code/ai-agent-manager

⭐ 10 · JavaScript · MIT · 推送 2026-06-29 · [GitHub](https://github.com/kirder24-code/ai-agent-manager) · [官网](https://launchsoloai.com/runcap) · 个人维护

**AI coding agent 的本地花销上限与合并前 CI 验证控制层**

Runcap 是面向 AI coding agent 的本地优先控制层：本地网关记录经其路由的 API 调用 token 用量并按价目表计价，达到日预算上限时返回阻断；提供任务范围预估、循环卡死检测、三层 token 压缩与 Verified Outcome Cost 收据。通过钉住版本的 GitHub Action 从 PR base commit 重放验证，产出 PASS/BLOCKED/HUMAN_APPROVAL_REQUIRED 判定后 PR 才获得合并资格。使用者需自备 provider API key、已有 agent，并习惯运行 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地网关记录真实 token 用量并在达到日上限时阻断请求
- 三层无损 token 压缩：字段裁剪、重复块去重、近重复 delta 编码
- CI Proof Gate 从 base commit 重放验证并给出 PASS/BLOCKED/HUMAN_APPROVAL_REQUIRED
- Verified Outcome Cost：总花费除以通过验证的任务数，产出带真值标签的收据

## 适用场景

- 为 agent 的 API 调用设置每日硬性花费上限
- 在合并 AI 生成的 PR 前要求 CI 重放验证
- 检测 agent 卡在同一错误循环并发出告警
- 离线用 mock 模式试用命令流程

## 场景标签

`编码 Agent` `LLM 可观测性` · 领域:编码与开发

## 证据(README 行号)

> L9: Runcap is a local-first control layer for AI coding agents. It can cap routed AI
> L67: Observability tools (Langfuse, Helicone, LangSmith, AgentOps) measure the past, and some run evals on outputs. Gate
> L87: - **Your own provider API key** (OpenAI or Anthropic). Runcap does not sell or supply model access.

## 星数曲线

```mermaid
xychart-beta
    title "kirder24-code/ai-agent-manager 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `84ae810d1775` · [字段定义](../../DATASET.md)*
