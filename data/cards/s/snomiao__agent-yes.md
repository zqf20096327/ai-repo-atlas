# snomiao/agent-yes

⭐ 31 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/snomiao/agent-yes) · [官网](https://agent-yes.com) · 个人维护

**AI 编程 CLI 的无人值守运行包装器：自动应答、重试与多 Agent 管理**

用 Rust 与 TypeScript 实现的包装工具，围绕 Claude Code、Codex、Copilot、Cursor、Grok、Qwen 等 9 种 AI 编程 CLI 运行：自动对 yes/no 提示应答、崩溃自动重启、空闲自动退出，实现无人值守执行。提供 ay/cy 命令跨终端列出、tail、发送指令给本机运行的 agent，跨 agent 共享任务清单（todos.jsonl）与问答追踪（ay ask/answer，含独立验证门禁）。支持 Docker 镜像（amd64/arm64）、本地 Web 控制台与 agent-yes.com 远程访问。README 明确警告提示注入风险，仅建议在可信仓库运行。

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

- 自动应答常见提示并自动重启崩溃进程，实现 agent 无人值守运行
- cy ls/tail/send 跨终端管理本机所有运行中的 agent（pids.jsonl 注册表 + FIFO）
- 跨 agent 共享任务清单 ay todo 与问答追踪 ay ask，含独立验证门禁
- Docker 镜像预装全部 AI CLI，支持 linux/amd64 与 linux/arm64

## 适用场景

- 让 Claude Code/Codex 等 AI 编程助手通宵无人值守跑完任务
- 在一台机器上并行管理多个 agent，随时查看输出或追加指令
- 多个 agent 协作同一仓库时共享任务清单并互相提问

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A wrapper tool that automates interactions with various AI CLI tools by automatically handling common prompts and re
> L39: - **Multi-CLI Support**: Works with Claude, Codex, Copilot, and Cursor CLI tools
> L296: ### Supported CLI Tools

## 星数曲线

```mermaid
xychart-beta
    title "snomiao/agent-yes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `75a835a804d8` · [字段定义](../../DATASET.md)*
