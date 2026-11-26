# codeaholicguy/ai-devkit

⭐ 1,674 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/codeaholicguy/ai-devkit) · [官网](https://ai-devkit.com) · 个人维护

**多 AI 编码代理的本地控制面：统一配置、会话监管与技能**

面向同时使用多个 AI 编码代理（Claude Code、Codex CLI、Gemini CLI、Cursor 等）的开发者，提供本地运行的统一管理层：一份 `.ai-devkit.json` 配置同步各代理的规则、MCP 与技能安装；`agent console`/`agent list`/`agent send` 监管并向运行中的 CLI 会话（tmux 承载）发送提示与日志；本地 SQLite 存储项目决策与约定，代理按需检索；内置 28 个以 `dev-lifecycle` 为锚的工程技能（verify/tdd/debug/security 等）。经 npm 安装，Apache-2.0 许可，无遥测；控制面仅支持 macOS/Linux，Windows 不支持 console。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一份 `.ai-devkit.json` 跨代理统一配置与技能安装
- agent console/list/send 对运行中 tmux CLI 会话的监管与消息路由
- 本地 SQLite 记忆库经 MCP/CLI 按需检索，避免上下文膨胀
- 28 个内置技能与 30+ 发布者技能注册表（skill add）

## 适用场景

- 团队多个 AI 编码代理需要共享一套规则与技能配置
- 向运行中的代理会话发送日志、提示或后续任务
- 要求代理在声明完成前提供新的测试/构建证据
- 跨会话留存并检索项目决策与编码约定

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **The control plane for AI coding agents.**
> L7: AI DevKit gives Claude Code, Codex CLI, Gemini CLI, opencode, Pi, Cursor, GitHub Copilot, Devin, and other coding ag
> L205: - **Not a replacement for Claude Code, Codex, Cursor, Gemini CLI, or opencode.** AI DevKit configures, supervises,

## 星数曲线

```mermaid
xychart-beta
    title "codeaholicguy/ai-devkit 星数(近 19 点)"
    x-axis ["2026-10-24", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 1650 --> 1676
    line [1652, 1653, 1654, 1653, 1654, 1656, 1652, 1661, 1662, 1664, 1666, 1667, 1668, 1669, 1671, 1670, 1672, 1673, 1674]
```

2026-10-24 1,652 → 2026-11-26 1,674（+22）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `e472122ae170` · [字段定义](../../DATASET.md)*
