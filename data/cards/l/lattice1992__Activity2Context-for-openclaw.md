# lattice1992/Activity2Context-for-openclaw

⭐ 30 · PowerShell · 推送 2026-03-25 · [GitHub](https://github.com/lattice1992/Activity2Context-for-openclaw) · 个人维护 · 中文 README

**把本地活动转为上下文注入 OpenClaw 的运行时钩子**

面向 OpenClaw agent 用户的运行时钩子（非 Skill）：持续采集本地活动（浏览器页面、文档编辑、应用窗口），聚合压缩为带时间与时长标注的结构化实体，并在每轮对话前将 memory.md 注入 OpenClaw 系统提示。输出原始行为流、聚合记忆文件与语义 JSON 三类文件。数据默认本地存储；若使用云端模型，注入内容会随提示发送给模型提供商。提供 Windows PowerShell 与 macOS Bash 安装脚本，macOS 需授予辅助功能与自动化权限并依赖系统 Python 3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 采集浏览器/文档/应用三类本地活动并聚合为结构化实体
- 每轮对话前将 memory.md 注入 OpenClaw 系统提示
- 原始日志行数封顶（默认 5000）并在启动时自动裁剪
- 仅注入聚合记忆而非原始日志以控制 token 开销

## 适用场景

- 让 agent 了解我正在编辑的文件与浏览的页面，无需反复交代背景
- 减少每轮对话重复说明上下文的开销
- 在敏感环境中配合本地模型限制上下文外发范围

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: Activity2Context is a Runtime Hook, not a Skill.
> L24: 3. Inject: before each chat turn, inject `activity2context/memory.md` into the OpenClaw system prompt.
> L110: You only need `memory.md` injection. No Skill file is required.

## 星数曲线

```mermaid
xychart-beta
    title "lattice1992/Activity2Context-for-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4d9402223c58` · [字段定义](../../DATASET.md)*
