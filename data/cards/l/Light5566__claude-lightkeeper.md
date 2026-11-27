# Light5566/claude-lightkeeper

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Light5566/claude-lightkeeper) · [官网](https://light5566.github.io/claude-lightkeeper/) · 个人维护 · 中文 README

**为 AI 编码代理维护代码库活知识地图的插件**

Lightkeeper 是一个 Claude Code 插件，也可作为 Hermes Agent 与 Codex 插件运行。它在代码仓库之外（~/vaults）维护一份 Obsidian 兼容的 Markdown 知识地图，记录模块、流程、集成、决策与术语；通过五类钩子（session primer、prompt 提示、文件指针、Stop 提醒、维护信号）让代理在编辑前读取地图、在停止前更新地图。提供 vault 命令行用于检索、lint 与导出；依赖 Claude Code、git 与 Python 3.9+，无需 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个钩子行为：编辑前文件指针、停止前更新提醒、压缩后重查询提示
- 地图存于仓库外的 Obsidian 兼容 Markdown vault，支持多仓库/worktree
- vault CLI 提供检索、lint（含密钥泄露检查）与 AGENTS.md/HTML 导出
- 每个 [[链接]] 须携带理由，形成可搜索的链接图谱

## 适用场景

- 让 Claude Code 每个会话免于重新探索代码库架构
- 团队共享一份跨多个仓库的系统知识地图
- 给不运行钩子的代理（Cursor、Gemini CLI）导出 AGENTS.md 说明块

## 场景标签

`编码 Agent` `知识图谱` · 领域:编码与开发

## 证据(README 行号)

> L5: **A knowledge map of your codebase that your coding agent reads before it edits and updates before it stops.** For C
> L21: Lightkeeper is a Claude Code plugin, and runs as a Hermes Agent and a Codex plugin too. It keeps an Obsidian-compat


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `c1e48a3aa778` · [字段定义](../../DATASET.md)*
