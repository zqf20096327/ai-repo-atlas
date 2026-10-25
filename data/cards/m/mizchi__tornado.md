# mizchi/tornado

⭐ 63 · MoonBit · MIT · 推送 2026-04-25 · [GitHub](https://github.com/mizchi/tornado) · 个人维护

**多 agent 开发编排器：按计划文件驱动编码与审查 agent**

带 TUI 的多 agent 开发编排工具：读取一个计划文件（如 plan.md），指定开发 agent 与审查 agent 的组合（如 --dev=codex --review=claude）运行开发流程。支持的 agent 类型包括 claude/claude-code、codex、api 和 mock。可通过 npx 直接运行，或用 npm 全局安装后从计划文件启动。仓库描述注明其工作流由 codex 审查、claude-code 开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从计划文件（plan.md）启动多 agent 开发流程
- 可分别指定开发 agent 与审查 agent（--dev/--review）
- 支持 claude/claude-code、codex、api、mock 四类 agent
- 提供 TUI 界面

## 适用场景

- 用一个计划文件驱动 codex 开发、claude 审查的自动化流程
- 为多个编码 agent 搭配不同角色完成开发任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: Multi-agent development orchestrator with TUI.
> L11: npx -y @mizchi/tornado ./plan.md --dev=codex --review=claude

## 星数曲线

```mermaid
xychart-beta
    title "mizchi/tornado 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-25 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9c086fb3b7f7` · [字段定义](../../DATASET.md)*
