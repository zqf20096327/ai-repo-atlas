# conorbronsdon/agent-context-os

⭐ 30 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/conorbronsdon/agent-context-os) · [官网](https://chainofthought.show/go/agent-context-os) · 个人维护

**Git 托管的跨 agent 项目上下文与工作流共享层**

Context OS 将项目上下文（身份、决策、工作状态、交接记录）以纯 Markdown 保存在 Git 仓库中，供多个编码 agent 读写：为 Claude Code、Codex、OpenClaw、OpenCode、Cursor、Devin、Hermes Agent 提供一级适配器，经共享生命周期内核将 setup/start/update/end 请求转为哈希校验的提案与回执，变更需人工审查。提供选择性迁移工作流导入既有聊天与指令，外部能力默认全部 opt-in。安装途径为下载发布版资产或 git clone 源码后运行 setup 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 个编码 agent 宿主的一级适配器，共享同一生命周期内核
- setup/start/update/end 操作生成哈希校验提案与回执，需审查后应用
- 迁移工作流将选定聊天、指令、记忆导出转为可审查的规范文件
- 发布版提供 tar 模板、SHA256SUMS 与离线验证文档

## 适用场景

- 在 Claude Code 与 Codex 等多个 agent 间保持同一份项目上下文
- 把散落在聊天记录和提示词中的决策与状态沉淀为可审查文件
- 会话结束时生成哈希校验的交接记录供下次会话读取

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Keep durable project context and workflows in a Git-backed repository that supported coding agents can read and upda
> L18: adapters route to shared repository state, with a deterministic lifecycle kernel
> L25: |Work across coding agents|Provider-neutral state, skills, and lifecycle transitions live outside host adapters. Re

## 星数曲线

```mermaid
xychart-beta
    title "conorbronsdon/agent-context-os 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `92b777675a35` · [字段定义](../../DATASET.md)*
