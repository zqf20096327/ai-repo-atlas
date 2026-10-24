# obsfx/trekker

⭐ 83 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/obsfx/trekker) · [官网](https://omercan.io/trekker) · 个人维护

**面向 AI 编程代理的本地 CLI 任务跟踪器**

基于 Bun 运行时的命令行 issue 跟踪器，将任务、epic、子任务、评论与依赖关系存入项目本地 SQLite 数据库，无需服务器。提供 ready 命令查询已解除阻塞的任务、FTS5 全文检索、变更审计日志与统一列表视图；任意命令可加 --toon 输出面向 AI agent 的省 token 序列化格式。另有可选的看板 dashboard 独立包。通过 Claude Code 插件（26 个 MCP 工具、13 个 slash 命令等）与 Codex 插件接入编码代理；Codex 支持自述处于早期阶段。作者声明其为 beads 的简化替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任务/epic/子任务/依赖管理，数据存于本地 .trekker SQLite
- ready 命令列出无阻塞任务及其将解锁的下游任务
- FTS5 全文检索与全量变更审计日志（history）
- --toon 输出面向 AI agent 的省 token 序列化格式
- Claude Code 插件提供 26 个 MCP 工具与自主任务 agent

## 适用场景

- 让 AI 编码代理跨会话跟踪自身任务进度
- 在提示中指示 agent 用 trekker 管理工作并通过 quickstart 学习用法
- 通过看板 dashboard 可视化监视代理的任务执行

## 场景标签

 · 领域:开发者工具/任务跟踪

## 证据(README 行号)

> L3: A CLI issue tracker built for AI coding agents. Stores tasks, epics, and dependencies in a local SQLite database. No
> L76: AI coding agents work better when they can track their own progress. A simple CLI-based task manager keeps them on 

## 星数曲线

```mermaid
xychart-beta
    title "obsfx/trekker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-24 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f15ac09818db` · [字段定义](../../DATASET.md)*
