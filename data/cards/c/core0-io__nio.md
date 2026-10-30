# core0-io/nio

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/core0-io/nio) · [官网](https://core0-io.github.io/nio/) · 组织维护

**自主 AI agent 的执行守卫与可观测性插件**

以插件形式加载进 Claude Code、Codex CLI、OpenClaw、Hermes、Pi、opencode 等 agent 宿主的守卫与采集层：在每次工具调用执行前经 Phase 0–6 管线（工具门→白名单→模式→静态→行为→LLM→外部评分）产出 0–1 加权评分并决定 allow/deny/confirm；Phase 0–4 离线运行，LLM 与外部评分阶段可选。同时以 OpenTelemetry 输出指标/追踪/日志并双写本地 JSONL 审计日志。Gemini CLI、Cursor、GitHub Copilot 仅支持 skill 级 scan/action 命令。经 curl 安装脚本一键安装，发布包预构建，终端用户无需 Node/pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工具调用执行前的 Phase 0–6 风险评估管线（allow/deny/confirm）
- 每个 hook 事件以 OpenTelemetry 信号输出并双写本地 audit.jsonl
- 静态扫描：15 条静态规则、7 条跨 6 语言的行为规则
- Gemini CLI/Cursor/GitHub Copilot 支持 skill 级 scan/action 流程

## 适用场景

- 生产环境 agent 的工具调用前风险拦截与审批
- 把 agent 执行事件接入 OTEL 后端做可观测性
- 对代码库按需运行执行风险静态扫描

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: - **What it does:** Nio hooks into your agent platform (Claude Code, Codex CLI, OpenClaw, Hermes, Pi, opencode) and
> L77: Captures every hook event (`UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `TaskCreated`, `TaskCompleted`, `Stop`,
> L85: - **Dynamic Guard** runs on every `PreToolUse` hook through a **Phase 0–6** pipeline (Tool Gate → Allowlist → Patte

## 星数曲线

```mermaid
xychart-beta
    title "core0-io/nio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `211d988d7950` · [字段定义](../../DATASET.md)*
