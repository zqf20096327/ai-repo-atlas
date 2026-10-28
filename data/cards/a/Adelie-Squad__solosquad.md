# Adelie-Squad/solosquad

⭐ 25 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Adelie-Squad/solosquad) · 组织维护

**面向独立创始人的 24/7 AI 团队助手系统（Discord 机器人）**

以单个 npm 包分发的层级式 orchestrator-workers 多 agent 系统：1 个 Chief 监督 agent 作为唯一面向用户的入口，向下调度 4 个主管 bot 与 20 个专家 agent（产品/工程/设计/营销 4 队，共 25 个 agent），通过 Discord 或终端交互。AI 引擎使用 Claude Code（Node.js 18+），记忆采用 JSONL 文件并按组织隔离。内置定时 crons、6+1 阶段决策循环、research 自动化研究工作流（可无人值守运行 8 小时以上）。跨平台 CLI，Slack 适配器代码已包含但不在 v1.0 SemVer 承诺内，Telegram 支持已在 v0.2.4 移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 层级 supervisor 架构：1 Chief + 4 主管 + 20 专家，共 25 个 agent，委托图为 DAG
- 6+1 阶段决策循环（TRIAGE→…→RETROSPECT），Chief 拥有 SYNTHESIZE 步骤
- research 工作流：假设验证→实验循环→盲评 backtest→报告，可无人值守 8h+
- 按组织隔离的 JSONL 文件记忆与自动化每日 crons

## 适用场景

- 独立创始人通过 Discord 指挥虚拟团队完成产品/营销/设计任务
- 定时 crons 自动执行例行运营与研究任务
- 小团队或多工作区下运行多 agent 协作工作流

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A 24/7 AI assistant system for solo founders, small teams, and n-jobbers — Discord bot + scheduled crons + team-ba
> L7: Running a company alone doesn't mean working alone. SoloSquad gives you a virtual team — **1 Chief** (org-level supe
> L28: **Stack:** TypeScript + Node.js 18+ · Claude Code as the AI engine · file-based memory (JSONL)

## 星数曲线

```mermaid
xychart-beta
    title "Adelie-Squad/solosquad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2d4ddeb91abc` · [字段定义](../../DATASET.md)*
