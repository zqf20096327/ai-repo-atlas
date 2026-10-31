# daystar7777/agent-work-mem

⭐ 16 · MIT · 推送 2026-05-10 · [GitHub](https://github.com/daystar7777/agent-work-mem) · 个人维护

**跨 AI 编程 agent 的共享记忆与交接协议（纯 Markdown）**

面向同时使用多个 AI 编程 agent（Claude Code、Codex CLI、Cursor、Aider、Cline 等）的开发者的文件级协作协议：在项目中创建 AIMemory/ 目录（INDEX.md、PROJECT_OVERVIEW.md、work.log、handoff 文件），各 agent 会话开始按固定顺序读取、工作中写入，实现跨会话/模型/机器的持久共享记忆与工作交接。事件带厂商中立的能力标签；分层存储（archive/cold）避免旧上下文膨胀。无守护进程、无数据库、无 SaaS，通过一段提示词由 agent 自动安装，可选 tmux 面板直投交付，Gemini 面板交接需手动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一份 Markdown 协议实现多 agent 共享记忆与交接，无守护进程/数据库/SaaS
- work.log 记录带厂商中立能力标签（filesystem-write、shell-exec 等）的审计轨迹
- 分层存储（archive/cold）控制旧上下文对 LLM 上下文的占用
- 可选 tmux 面板直投交付，支持 IMPLEMENT/REVIEW/TEST 等接收角色标记

## 适用场景

- 在 Claude 与 Codex 之间交接设计、实现与评审工作
- 让新会话/新模型快速恢复项目上下文与决策记录
- 审计 agent 是否真正运行过测试与执行过操作
- 多机多人协作时维持同一份项目工作记忆

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A vendor-neutral, file-based collaboration protocol that lets multiple AI coding agents — Claude Code, ChatGPT Cod
> L153: **agent-work-mem** is a 1-prompt install that fixes all of this. It establishes a small protocol — a few markdown 

## 星数曲线

```mermaid
xychart-beta
    title "daystar7777/agent-work-mem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `35dd41fdb008` · [字段定义](../../DATASET.md)*
