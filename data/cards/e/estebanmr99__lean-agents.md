# estebanmr99/lean-agents

⭐ 4 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/estebanmr99/lean-agents) · 个人维护

**为多款编码 agent 一键安装共享规则、子代理与省 token 工具**

一个跨 agent 的 AI 编码环境配置工具：一条 npx 命令向 Claude Code、OpenCode、GitHub Copilot CLI、Antigravity、VS Code Copilot 和 Cursor 写入共享规则（AGENTS.md）、默认使用低成本模型档位的子代理，以及 RTK、Context Mode、Serena、Playwright 等 MCP 工具；支持 --dry-run 预览、--uninstall 全量回滚、--adopt 收编已有配置、--upgrade-agent 迁移 OpenCode 1.x→2.x。需 Node.js 22.20+ 与 git，支持 macOS/Linux/Windows，隐私预设可控制遥测与外呼。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令向 6 个编码 agent 写入共享规则、子代理与 MCP 工具，且可 --uninstall 完整回滚
- 子代理按 fast/balanced/strong 档位分配不同模型以节省 token
- --dry-run/--doctor/--adopt 提供 previews、体检与已有配置收编
- 支持团队 --project 模式、西班牙语规则（--lang es）与代理环境

## 适用场景

- 新机器上一键为多个编码 agent 配置统一规则和工具
- 团队统一 rollout 编码 agent 规范（--project）
- 把 OpenCode 1.x 配置迁移到 2.x（--upgrade-agent）
- 工作电脑在代理/隐私受限环境下配置 agent（--privacy strict）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: A cross-agent, token-efficient AI coding setup: one command installs shared rules, cheap-by-default subagents, and 
> L23: **What it changes on your machine:** rules (`AGENTS.md`), subagents, RTK and MCP tools (Context Mode, plus optional
> L87: - **Cheap subagents:** exploration, research and review run on the cheapest fitting model tier.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9e738615e04b` · [字段定义](../../DATASET.md)*
