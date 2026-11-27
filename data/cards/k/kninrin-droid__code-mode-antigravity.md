# kninrin-droid/code-mode-antigravity

⭐ 5 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/kninrin-droid/code-mode-antigravity) · 个人维护

**给 AI agent 提供持久 Python REPL 以合并工具调用省 token**

为 Antigravity 等 AI coding agent 提供一个 MCP stdio 服务器，暴露 py_exec/py_reset 两个工具，让 agent 用一段脚本批量处理多个文件操作，仅输出摘要，会话状态（变量、导入、cwd）跨调用保持。零外部依赖、输出截断上限约 5 万字符、可配置 1-600 秒超时、强制 UTF-8。提供一键安装脚本自动写入配置并附带 AGENTS.md 规则；非沙箱运行，以当前 OS 用户权限执行，仅建议在可信环境使用。

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

- MCP stdio 服务器暴露 py_exec/py_reset，批量化 agent 工具调用
- 持久 Python 会话：变量、导入与 cwd 跨调用保持
- stdout 约 50,000 字符截断（保留头尾）与 1-600s 可配置超时
- 零依赖，纯 Python 标准库实现

## 适用场景

- agent 批量读取/查询多个日志、JSON、CSV、SQLite 文件时减少往返
- 多文件分析场景下压缩进入上下文的原始数据量
- 为 Antigravity/Claude Code/Cursor 等 MCP 客户端扩展 Python 执行能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Give your AI agent a persistent Python REPL — batch 10+ tool calls into 1.**
> L14: **Code Mode Antigravity** fixes that with a minimal, zero-dependency MCP server exposing a **live Python session** 
> L62: * **Works everywhere** — built for **Antigravity**, also compatible with **Claude Code**, **Cursor**, and any stdio

## 星数曲线

```mermaid
xychart-beta
    title "kninrin-droid/code-mode-antigravity 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-26 5 → 2026-11-27 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `94f5c1a837ef` · [字段定义](../../DATASET.md)*
