# krapie/mycelium

⭐ 42 · JavaScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/krapie/mycelium) · [官网](https://tiny.kevinprk.com/mycelium-npm) · 个人维护

**管理 AI 编码会话并把知识带入下一次会话的 CLI 工具**

面向使用 AI 编码代理的开发者的终端（TUI）工具：自动捕获 Claude Code、Codex、Kiro、OpenCode 的会话，按项目/工单/服务分组组织，从中提炼重复出现的知识与上下文，下次从 Mycelium 启动的会话自动继承这些内容。LLM 调用复用用户自己的 claude/codex CLI，数据本地存储（~/.mycelium，无服务器无遥测）。另提供 VS Code 扩展，Windows 下需在 VS Code 集成终端运行；多机同步与清理功能标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动捕获 Claude Code / Codex / Kiro / OpenCode 会话到统一位置
- 从会话文件夹提炼可复用知识，供下一次会话继承
- 本地优先（~/.mycelium 存储，无服务器与遥测），LLM 调用走用户自己的 CLI
- 提供 VS Code / Cursor / Windsurf 扩展与 TUI 两种界面

## 适用场景

- 把散落的 AI 编码会话按项目整理并沉淀知识
- 在新会话开始时自动带上此前会话的上下文与洞察
- 跨 Claude Code、Codex 等不同代理 CLI 交接工作

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L21: - **Capture**: Claude Code, Codex, Kiro, and OpenCode sessions land in one place, automatically.
> L23: - **Learn**: what repeats across a folder's sessions becomes durable knowledge.
> L47: > **Mycelium uses your own LLM usage.** `organize`, `autotag`, `knowledge`,

## 星数曲线

```mermaid
xychart-beta
    title "krapie/mycelium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf8e34587abd` · [字段定义](../../DATASET.md)*
