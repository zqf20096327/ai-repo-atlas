# seanyao/roll

⭐ 14 · TypeScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/seanyao/roll) · [官网](https://seanyao.github.io/roll/) · 个人维护 · 中文 README

**编排已装 AI 编码 CLI 自主交付任务的命令行工具**

npm 全局安装的 CLI，驱动用户已安装登录的 AI 编码 CLI（Claude Code、Codex、Kimi、Pi、Antigravity、Reasonix、Cursor）完成需求交付：将需求拆分为带验收标准的任务清单，逐个在独立 git worktree 中交给 agent 执行，要求测试通过并由第二个 agent 评审打分，CI 绿后才经 PR 合并视为完成，同时归档验收证据。自身不含模型，不自动后台运行，需手动执行 roll loop go；依赖 Node.js 22+、git 仓库与至少一个 AI CLI。

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

- 需求拆分为带验收标准的小任务，逐个交给已安装的 AI 编码 CLI
- 独立 git worktree 隔离 + 第二 agent 评审 + PR 合并后任务才算完成
- 每任务归档测试输出与截图证据，Done 视为待验证声明而非事实
- roll status/north 提供自主时长、交付率、返工率等健康指标

## 适用场景

- 让已有的 Claude Code/Codex 等 CLI 按任务清单自主完成小型需求并开 PR
- 以验收证据页核验 agent 声称完成的工作
- 跟踪 AI agent 交付的健康度与 token 花费

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L19: You already have an AI that writes code when you sit there and prompt it. Roll is
> L57:  Kimi, Pi, Antigravity, Reasonix, or Cursor. Roll drives them; it does not
> L58:  replace them and does not ship a model of its own.

## 星数曲线

```mermaid
xychart-beta
    title "seanyao/roll 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9e4523c5d140` · [字段定义](../../DATASET.md)*
