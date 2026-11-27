# juanmaorta/mnemosyne

⭐ 4 · TypeScript · Apache-2.0 · 推送 2026-11-14 · [GitHub](https://github.com/juanmaorta/mnemosyne) · 个人维护

**给编码 agent 的本地 Markdown 记忆库，跨工具共享**

Mnemosyne 是一个本地优先、以纯 Markdown 文件为存储的记忆库，供 Claude Code、Codex CLI、OpenCode 及任何能执行 shell 命令的 agent 共享使用。安装器自动检测已有 agent 并注入会话启动 hook；记忆按相关性、新近度与重要性排序，支持强化与衰减；可选用本机 Ollama 提供语义搜索，无 Ollama 时退化为 tier 0 关键词搜索。通过 install.sh 脚本安装，需 Node.js ≥ 20 与 git，支持 macOS 与 Linux，可卸载并保留数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent 共享一份 Markdown 记忆存储，数据与具体 agent 解耦
- 按相关性、新近度、重要性排序，记忆随使用强化、被忽略则淡化
- scope 分区隔离（个人/工作/客户），删文件夹即彻底删除
- 可选本机 Ollama 语义搜索，离线运行，文件可同步跨机器共享

## 适用场景

- 让 Claude Code / Codex 等多个终端 agent 共享同一份项目偏好记忆
- 避免每次会话重新说明个人偏好与项目约束
- 在个人、雇主、客户等多上下文间隔离并按需彻底删除记忆
- 用 Obsidian 等编辑器直接查看和编辑 agent 记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Mnemosyne is a single, local memory store shared by Claude Code, Codex, OpenCode and any agent
> L20: - **Agent-agnostic.** The data knows nothing about any particular agent. The installer wires

## 星数曲线

```mermaid
xychart-beta
    title "juanmaorta/mnemosyne 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9222cc8d2128` · [字段定义](../../DATASET.md)*
