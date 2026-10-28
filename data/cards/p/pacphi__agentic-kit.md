# pacphi/agentic-kit

⭐ 61 · JavaScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/pacphi/agentic-kit) · 个人维护

**一条命令安装、修复并验证 ruflo/agentic-qe 的多主机 agent 工具箱**

npm 包形式的 agent CLI 安装与维护工具箱：一条 ak setup 命令全局安装 ruflo (claude-flow)、agentic-qe、agent-browser 执行器与 RuvNet Brain 离线知识库（约 2 GB 可选下载），并通过 ak sync 在升级后重新收敛被破坏的组件、ak status 报告各子系统状态。支持将 Claude Code、Codex、OpenCode 三种主机接到 Anthropic/OpenAI/OpenRouter/Ollama 等 provider，附本地 Web 仪表盘（127.0.0.1:7431）。跨 macOS/Linux/Windows，零运行时依赖（内嵌 SQLite）。当前发布于 alpha 渠道（4.0.0 GA 前）。

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

- 一条命令安装、修复并验证 ruflo + agentic-qe + RuvNet Brain
- Claude/Codex/OpenCode 三主机共享一套可配置活动路由策略
- ak sync 自愈：升级后重装被清掉的组件并重新校验
- 本地 Web 仪表盘展示状态、用量与观测数据（仅 localhost）

## 适用场景

- 一次性装好并配置 Claude Code / Codex 的 agent 工具链
- npm 升级后自动修复 ruflo 原生绑定漂移导致的记忆/安全组件失效
- 在一个项目里同时路由 Claude 与 Codex 双主机

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: **One npm package that installs, repairs, and checks ruflo (claude-flow), its compatible browser executor, and agent
> L39: - **Multi-host execution (optional):** Claude, Codex, and opt-in OpenCode can share one activity policy; `ak run` i
> L51: A **host** is the agent CLI driving a session (Claude Code, Codex CLI, or OpenCode). A

## 星数曲线

```mermaid
xychart-beta
    title "pacphi/agentic-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-28 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6f1bbb47cdcc` · [字段定义](../../DATASET.md)*
