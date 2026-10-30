# dotdevdotdev/agentwire-dev

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/dotdevdotdev/agentwire-dev) · [官网](https://agentwire.dev) · 个人维护

**自托管键盘驱动的 Claude Code 多 agent 编排驾驶舱**

运行在本机的桌面式门户，通过 tmux 会话同时管理多个 Claude Code agent：每个会话是一个可拖拽窗口，提供命令面板、git worktree 并行隔离、定时任务调度器（产出草稿 PR）、Council 多角色商议、语音输入与 Kokoro-82M CPU 神经 TTS 输出、SSH 远程机器接入，以及 300+ 危险命令拦截。默认绑定回环地址、无遥测，可配置 LAN/手机访问（需 SSL 证书与 token）。要求 Python 3.10+、tmux、Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多会话窗口化编排：F3 拼贴、Tab 切换、Cmd/Ctrl+K 命令面板
- git worktree 隔离并行工作 + 定时任务产出草稿 PR 而非直接提交
- 语音层：push-to-talk 输入 + Kokoro-82M 纯 CPU 神经 TTS，可接自定义 TTS shim
- 300+ 危险命令拦截（rm -rf、force push 等），全部留审计日志

## 适用场景

- 同时跑多个 Claude Code agent 做并行开发，不想在 tmux 面板间切换
- 把重复性任务（研究、测试、清理）交给定时调度器无人值守运行
- 在手机/平板上通过 LAN 访问并语音操控本机的 agent 会话

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A self-hosted, keyboard-driven cockpit for running a whole fleet of Claude Code agents at once.
> L45: You → AgentWire Portal → tmux sessions → a fleet of Claude Code agents
> L70: **Requirements:** Python 3.10+, tmux, Claude Code. Optional: ffmpeg (only for host-mic push-to-talk capture — brows

## 星数曲线

```mermaid
xychart-beta
    title "dotdevdotdev/agentwire-dev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e795484fb998` · [字段定义](../../DATASET.md)*
