# sdsrss/claude-mem-lite

⭐ 68 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/sdsrss/claude-mem-lite) · 个人维护 · 中文 README

**Claude Code 的持久化记忆插件：跨会话捕获决策与修复并检索召回**

面向 Claude Code 的跨会话记忆系统，以 MCP server 加七个 Claude Code hooks 形式运行：自动捕获编码过程中的观察、决策与 bug 修复，按 episode 批量分组后交给 LLM（Haiku 级）编码，写入单一 SQLite 库，无外部服务。检索基于 FTS5 BM25 加查询扩展（伪相关反馈、概念共现、100+ 同义词条含中英映射），另有时间线浏览、错误触发召回、编辑文件时注入相关历史观察等机制。自称 claude-mem 的低成本替代（成本对比为架构估算而非实测）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七个 Claude Code hook 生命周期事件自动捕获观察，episode 批量将 LLM 调用压缩至每批一次
- FTS5 BM25 检索加查询扩展、同义词与中英跨语言映射、上下文重排序
- Bash 出错时自动检索相关历史修复；编辑文件时主动注入该文件的历史观察
- 密钥/令牌/证书自动脱敏，原子写入与 PID 锁防止损坏

## 适用场景

- 让 Claude Code 在跨会话间记住我的决策、bug 修复和上下文
- 编码报错时自动召回以前解决过类似问题的记录
- 浏览项目历史观察时间线，回溯某个功能是怎么改的

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: `claude-mem-lite` is a **persistent memory** (also called *long-term memory* or *cross-session context*) system for 
> L108: - **Multi-provider LLM mode** -- Provider priority `ANTHROPIC_API_KEY` (direct Anthropic API) → `OPENROUTER_API_KE
> L78: - **Automatic capture** -- Hooks into the Claude Code lifecycle (SessionStart, PreCompact, PreToolUse, PostToolUse,

## 星数曲线

```mermaid
xychart-beta
    title "sdsrss/claude-mem-lite 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-30 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2df42a95aedd` · [字段定义](../../DATASET.md)*
