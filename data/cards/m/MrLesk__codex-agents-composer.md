# MrLesk/codex-agents-composer

⭐ 29 · TypeScript · MIT · 推送 2026-03-17 · [GitHub](https://github.com/MrLesk/codex-agents-composer) · 个人维护

**桌面应用：可视化管理 Codex agents 及其技能**

ElectroBun 桌面应用，为使用 OpenAI Codex CLI 的用户提供 agents 的创建、配置与组织界面：设置模型、推理级别与开发者指令，无需手改配置文件；agents 可全局保存于 ~/.codex/agents/ 或绑定到项目 .codex/agents/。内置技能目录（来自 skills.sh 仓库）与技能编辑器，支持拖拽分配技能；所有更改写入 ~/.codex/ 配置，命令行立即可用。需 Bun 运行，通过 bun 命令安装与开发运行，可打包 macOS/Windows/Linux 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化创建与配置 Codex agents（模型、推理级别、指令）
- 全局（~/.codex/agents/）与项目级（.codex/agents/）两种作用域
- 浏览 skills.sh 技能目录并在内置编辑器中自建技能
- 拖拽分配技能，配置持久化到 ~/.codex/ 供命令行使用

## 适用场景

- 不想手改配置文件，用 GUI 管理 Codex agents
- 为不同项目绑定各自的 agents 与技能组合
- 从 skills.sh 浏览或自建技能并拖拽分配给 agents

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A desktop application for managing your Codex agents and their skills.
> L11: Codex Agents Composer provides a visual interface for creating, configuring, and organizing Codex agents. Instead o

## 星数曲线

```mermaid
xychart-beta
    title "MrLesk/codex-agents-composer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4f72329d8615` · [字段定义](../../DATASET.md)*
