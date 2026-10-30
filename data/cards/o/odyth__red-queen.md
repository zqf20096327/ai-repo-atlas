# odyth/red-queen

⭐ 16 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/odyth/red-queen) · [官网](https://redqueen.sh) · 个人维护

**确定性编排器：把 Jira/GitHub 工单送过 AI 编码流水线**

一个用 TypeScript/npm 分发的确定性状态机编排器，面向已运行 Jira 或 GitHub Issues 驱动 SDLC 的团队：将工单依次送过 spec、编码、评审、测试、人工评审等阶段，最终产出已合并的 PR。编排器本身不消耗 AI token，只在阶段间调度 Claude Code（默认）或 OpenAI Codex CLI 作为 worker，并在配置的人工门禁处停下。阶段、技能与门禁在 redqueen.yaml 中声明，附带本地 Web 仪表盘（127.0.0.1:4400）、守护服务安装（macOS LaunchAgent/Linux systemd user unit）、堆叠分支与多仓库工作区模式。需 Node.js >= 24 及已认证的 AI CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排器自身零 token，仅调度 Claude Code / Codex CLI worker
- 阶段/技能/门禁均通过 redqueen.yaml 声明，可自定义新增阶段与覆盖技能提示词
- 本地仪表盘含状态 SSE 流、配置热重载、技能管理与工作流编辑五个标签页
- 支持阻塞链接的堆叠分支合并顺序与多仓库工作区模式

## 适用场景

- 让团队把 Jira 工单自动送过 spec-编码-评审-测试流水线
- 在人工门禁处介入审核 spec 与最终 PR
- 多仓库工作区内并行驱动多个仓库的 AI 编码流水线

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: A deterministic state machine that shuttles Jira or GitHub tickets through a
> L15: tokens; it just dispatches Claude Code workers between phases and stops at

## 星数曲线

```mermaid
xychart-beta
    title "odyth/red-queen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `41d11777d142` · [字段定义](../../DATASET.md)*
