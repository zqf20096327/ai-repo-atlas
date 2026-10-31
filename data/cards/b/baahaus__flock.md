# baahaus/flock

⭐ 24 · Swift · MIT · 推送 2026-07-14 · [GitHub](https://github.com/baahaus/flock) · [官网](https://baahaus.github.io/flock/) · 个人维护

**macOS 终端复用器：单窗口并行管理多个 Claude Code 会话**

基于 Swift/AppKit 的原生 macOS 应用，在一个窗口内平铺运行任意数量的 Claude Code 会话，同时提供 shell 终端窗格与可编辑 markdown 窗格，自动排列布局。claude 窗格实时检测活动状态（thinking/working/waiting/idle）并以覆盖层展示文件读写与命令日志；另提供命令面板、broadcast 广播输入、全局查找、经 wren（MLX 上运行的 LoRA 模型）的提示压缩、token 用量与费用统计、会话恢复、原生通知等功能。面向同时运行多个 Claude Code 会话的开发者，通过 GitHub releases 的 .pkg/.zip 安装，也可用 Xcode 自行编译。

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

- 单窗口平铺运行多个 Claude Code 会话，实时状态指示与文件/命令变更日志覆盖层
- broadcast 模式一次输入同步到所有窗格
- wren 提示压缩（MLX/Apple Silicon 上的 LoRA 模型），宣称压缩 50-80%
- 跨所有窗格的 token 用量与费用追踪，含 Anthropic 计划限额监控

## 适用场景

- 我在一个窗口里并行跑多个 Claude Code 会话观察它们工作
- 我想给多个 agent 同时广播同一条指令
- 我想跟踪各会话的 token 消耗与费用

## 场景标签

 · 领域:开发者工具/终端复用

## 证据(README 行号)

> L14: flock is a tiny, beautiful macOS app that lets you run as many Claude Code sessions as you want, all at once, all i
> L32: - **claude panes** run full Claude Code sessions with real-time activity detection, state indicators (thinking, wor

## 星数曲线

```mermaid
xychart-beta
    title "baahaus/flock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9888a1d24aa8` · [字段定义](../../DATASET.md)*
