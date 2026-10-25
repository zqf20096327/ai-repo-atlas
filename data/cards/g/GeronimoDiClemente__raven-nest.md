# GeronimoDiClemente/raven-nest

⭐ 33 · TypeScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/GeronimoDiClemente/raven-nest) · 个人维护

**在单窗口并行运行多个 AI agent CLI 的桌面终端工作区**

基于 Electron + React 的桌面应用（NestMux），以网格/平铺面板让 Claude、Gemini、Codex、Copilot、DeepSeek、Grok、Qwen 等多个 AI agent 会话并行运行，每个面板有独立账号、历史与环境。配套功能包括 git worktree 分支级隔离、内置 Monaco 编辑器面板、Teams 工作区与团队流分析、Hub 常用终端聚合、GitHub/GitLab 集成与 CI 查看、按面板的端口检测。v1.3.1 起可在应用内一键安装 agent CLI。许可为 PolyForm Strict（source-available）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网格工作区中每个面板是独立 AI 会话，多 agent 并行
- git worktree 分支级隔离 + 内置 Monaco 编辑器面板
- 面板级端口检测（PTY 树/父 PID/cwd 三级回退链）
- 应用内一键安装各 agent CLI（走系统包管理器）

## 适用场景

- 同时跑多个 AI 编程 agent 并排对照输出
- 为每个任务建独立 worktree 隔离 agent 工作区
- 团队查看 commits/PR/周期时间等聚合分析

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: Run Claude, Gemini, Codex, Copilot and more — side by side in a single window. Each pane is its own AI session, with
> L17: Think of it as a terminal multiplexer — but built specifically for AI agents and the way teams ship code. Instead o

## 星数曲线

```mermaid
xychart-beta
    title "GeronimoDiClemente/raven-nest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `925ea3c85531` · [字段定义](../../DATASET.md)*
