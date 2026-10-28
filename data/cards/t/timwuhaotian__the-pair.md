# timwuhaotian/the-pair

⭐ 384 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/timwuhaotian/the-pair) · [官网](https://apps.timwuhaotian.dev/) · 个人维护 · 中文 README

**开源桌面双 AI 智能体结对编程应用：规划者与执行者互相校验代码**

基于 Tauri/React/TypeScript 的本地桌面应用，运行两个 AI 编码智能体：只读的 Mentor 负责规划与审查，Executor 负责写代码和执行命令，二者交叉校验以拦截 AI 生成代码中的错误。支持混合搭配 10 个 provider CLI（opencode、Claude Code、Codex、Antigravity、Kimi Code、Pi、Kiro、Aider、Grok Build、Muse Code），并可经 Ollama 使用本地模型离线运行。需预装至少一个 provider CLI；另有终端版 Pair Code（npm 安装）。提供 macOS/Windows/Linux 安装包，功能含会话恢复、Git 变更跟踪、资源监控与迭代预算（默认 20 轮）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mentor（只读规划审查）+ Executor（写码执行）双智能体交叉校验
- 支持 10 个 provider CLI 任意组合，可经 Ollama 离线运行
- 会话快照恢复、Git 变更跟踪与 diff 查看器、逐智能体 CPU/内存监控
- 提供桌面版与终端 CLI 版（Pair Code）两种界面

## 适用场景

- 让两个 AI 智能体自主迭代完成编码任务，我回来做最终审查
- 自动化代码重构与 bug 修复，且有独立审查角色把关
- 观察 AI 智能体如何拆解和解决问题，作为学习工具

## 场景标签

`编码 Agent` `多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L44: **The Pair is a free, open-source desktop app that runs two AI coding agents — a read-only _Mentor_ that plans and 
> L55: The Pair is an **open-source AI pair programming** app and **multi-agent coding assistant** for developers who want
> L104: The Pair is the desktop app for visual monitoring and hands-on oversight. **CLI** users can install Pair Code, the

## 星数曲线

```mermaid
xychart-beta
    title "timwuhaotian/the-pair 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 382 --> 384
    line [383, 383]
```

2026-10-18 383 → 2026-10-28 383（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `0311ca4a4a20` · [字段定义](../../DATASET.md)*
