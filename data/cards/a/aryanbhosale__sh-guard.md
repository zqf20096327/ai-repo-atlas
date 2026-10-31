# aryanbhosale/sh-guard

⭐ 29 · Rust · GPL-3.0 · 推送 2026-06-13 · [GitHub](https://github.com/aryanbhosale/sh-guard) · [官网](https://sh-guard.pages.dev) · 个人维护

**面向 AI 编程 agent 的 shell 命令风险分类器（Rust，<100μs）**

用 Rust 编写的 shell 命令安全分类工具：将命令解析为 AST，做管道数据流污点分析，输出 0-100 风险分与 Safe/Caution/Danger/Critical 四级判定，风险映射到 MITRE ATT&CK 技术 ID。内置 157 条命令规则、51 条路径规则、25 条注入模式等，支持 TOML 自定义规则。面向让 AI 编程 agent（Claude Code、Codex、Cursor、Cline、Windsurf）在执行前拦截危险命令的用户，提供 --setup 一键接入 hook 或 MCP server，并提供 Python/Node/Rust 绑定。npm 绑定包需本机 Rust 工具链从源码构建，预编译 .node 未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AST 解析 + 管道污点分析，检测 cat .env | curl 类数据外泄流
- 风险分映射 MITRE ATT&CK 技术 ID
- --setup 自动检测并配置 Claude Code/Codex/Cursor/Cline/Windsurf 五种 agent
- 提供 CLI、MCP server、Python/Node/Rust 绑定与 Docker 镜像

## 适用场景

- 在 AI agent 执行 shell 命令前自动拦截 rm -rf 等高危操作
- 用退出码 0-3 将风险分级接入 CI 或自动化流程
- 在自研 agent（LangChain/Vercel AI SDK 等）中调用分类 API 做命令门控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: Semantic shell command safety classifier for AI coding agents. Parses commands into ASTs, analyzes data flow throug
> L21: AI coding agents (Claude Code, Codex, Cursor, etc.) execute shell commands on your behalf. Real incidents include:
> L51: |**Claude Code**|PreToolUse hook &mdash; blocks critical commands automatically|

## 星数曲线

```mermaid
xychart-beta
    title "aryanbhosale/sh-guard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7ee5e80964d4` · [字段定义](../../DATASET.md)*
