# conallob/jira-beads-sync

⭐ 18 · Go · BSD-3-Clause · 推送 2026-07-15 · [GitHub](https://github.com/conallob/jira-beads-sync) · 个人维护

**把 Jira 任务同步到 git-backed 的 beads 任务跟踪器并双向同步**

命令行同步工具：将 Jira issue 及其依赖（epic、story、子任务、链接）递归导入 beads——一个以 YAML 文件存储在仓库 .beads/ 目录的 git-backed 任务跟踪器，本地用 bd 命令离线管理后再同步回 Jira。内部经 Protocol Buffers 做类型安全的格式转换。提供两种使用界面：CLI 命令，或通过 Claude Code 插件 / Opencode 项目指令用自然语言操作；任何能执行 shell 命令的 AI 编码工具均可调用。以 Go 实现，提供 Homebrew、二进制、go install 等安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Jira ↔ beads 双向同步，递归抓取依赖与层级结构
- issue 以 YAML 文件形式存于仓库 .beads/ 目录，git 版本管理
- Claude Code 插件与 Opencode 指令支持自然语言管理 issue
- 内部基于 Protocol Buffers 做类型安全的数据转换

## 适用场景

- 在代码仓库中离线管理 Jira 任务并与代码同版本控制
- 让 Claude Code 等 AI 工具用自然语言导入、更新、同步 Jira issue
- 把本地 beads 中的状态变更推送回 Jira

## 场景标签

 · 领域:开发工具/任务跟踪

## 证据(README 行号)

> L11: **jira-beads-sync** synchronizes Jira issues with beads, a git-backed issue tracker. Work with Jira issues as YAML 
> L129: jira-beads-sync is a standard CLI binary that works with any AI coding assistant. Install it and configure Jira cr
> L164: Any AI coding tool that can run shell commands can use jira-beads-sync. Add these commands to your project's instr

## 星数曲线

```mermaid
xychart-beta
    title "conallob/jira-beads-sync 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `52ce37c68976` · [字段定义](../../DATASET.md)*
