# dcsnak/GitHub-Copilot-app

⭐ 62 · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/dcsnak/GitHub-Copilot-app) · 组织维护

**GitHub 官方的 agent 驱动桌面端：跨仓库查找、运行、掌控并落地软件工作**

GitHub, Inc. 维护的桌面应用，作为管理软件工作的单一控制中心：查找待办工作、启动与引导 Copilot agent、在 Canvas 中检视计划/终端/预览/差异、经 Agent Merge 走完审查与合并。每个本地会话运行在隔离的 git worktree，云会话运行在 GitHub 托管的隔离环境。前置要求为 Git 与任一 Copilot 订阅（含免费版），也支持自带 key（BYOK）接入自有模型提供方。安装包从 Releases 页下载，仓库同时用于反馈 issue 与讨论；声明会收集使用数据与对话数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地会话运行于隔离 git worktree，云会话运行于 GitHub 托管环境
- Canvas 将 agent 的计划、终端、预览、diff 呈现为可检视可编辑的面板
- My Work 聚合会话、issue、PR 与仓库上下文；Automations 支持定时/后台任务
- 无 Copilot 订阅时可通过 BYOK 使用自有模型提供方

## 适用场景

- 并行驱动多个 agent 分别调查 bug、实现 issue、处理审查意见
- 在一个桌面端内完成从选题到 PR 合并的完整流程，减少工具切换
- 把重复性提示词与流程固化为定时或后台自动化任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software wo
> L15: The app is built for parallel agent-driven development. Each local session runs in its own isolated git worktree, a
> L25: - Git


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `ef82cf6db0cd` · [字段定义](../../DATASET.md)*
