# angadhn/botference

⭐ 20 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/angadhn/botference) · [官网](https://botference.com) · 个人维护

**终端多 LLM 规划议事厅：用户与 Claude Code、Codex 协作产出实施方案**

基于 Ink TUI 的多 LLM 协作规划工具：用户与 Claude Code、Codex CLI 在一个‘议事厅’式群聊中讨论，bot 之间可相互交接发言权并直接辩论，最终产出 implementation-plan.md 与 checkpoint.md。附带 Google-Docs 式文档评审界面，支持 LaTeX/Markdown/Jupyter Book 论文的批注、bot 回复与确定性应用更改。需预装并认证 Claude Code 与 Codex CLI。README 自述研究计划模式与构建模式处于深度实验阶段，不推荐一般使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 用户与 Claude、Codex 三方议事厅式实时协作规划，产出 implementation-plan.md
- 文档评审界面：论文渲染为可批注 HTML，margin 批注转为 bot 回合，更改按 Apply/Commit/Revert 确定性应用
- 支持通过 cloudflared 隧道共享评审 URL（密码门控）或经 git 同步多人协作

## 适用场景

- 在终端里让多个编码 LLM 与我辩论并形成实施方案
- 为 LaTeX/Jupyter Book 论文搭建带 AI 批注回复的评审站点
- 通过共享 URL 让合作者批注论文并触发 bot 回复

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L17: **The primary contribution of this repository is plan mode** — a multi-LLM
> L88: - Claude Code CLI installed and authenticated
> L89: - Codex CLI installed and authenticated

## 星数曲线

```mermaid
xychart-beta
    title "angadhn/botference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3082e31d605d` · [字段定义](../../DATASET.md)*
