# termaxa/termaxa

⭐ 27 · Rust · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/termaxa/termaxa) · [官网](https://termaxa.com) · 组织维护

**拦截 AI 编程 agent 危险 shell 命令的 Rust 守门工具**

单个 Rust 二进制，安装到 Claude Code、Codex、Cursor、Copilot CLI 的 hook 路径中，在命令执行前按仓库内策略文件判定 allow/ask/deny，预览命令的破坏后果（被删文件、丢失提交、DROP 的行数），执行前做备份以便 termaxa rollback 撤销，并对跨 shell 重试的破坏性意图设熔断。每次决策写入 append-only 哈希链审计日志，提供 observe 观察模式、replay 回放历史命令与 doctor 验证 hook 是否真正生效。无模型、无服务、无账号，本地运行不联网发遥测。限制：无法理解命令意图本身，路径打错时只忠实报告所输路径的影响范围。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命令执行前的后果预览：被删文件、force push 丢失的提交、DROP TABLE 影响行数
- 执行前自动备份（文件复制、ref 固定、表导出），termaxa rollback 可撤销
- 跨 shell/拼写统计破坏性意图的熔断器，默认阈值 2
- append-only 哈希链审计日志，agent 无法改写

## 适用场景

- 无人值守运行 Claude Code/Codex 等 agent 时拦截 rm -rf、reset --hard 等危险命令
- 采用守门前先回放 agent 历史命令，评估策略的打扰频率
- 团队通过 PR 审阅仓库内策略文件来管理 agent 权限

## 场景标签

 · 领域:开发者工具/Agent 安全

## 证据(README 行号)

> L23: Termaxa is a single Rust binary that sits in the agent's hook path, with no model, no service and no account. For e
> L186: |Harness|Wire it|How a verdict reaches the agent|Measured on|The caveat that matters|

## 星数曲线

```mermaid
xychart-beta
    title "termaxa/termaxa 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f46f152ec0c5` · [字段定义](../../DATASET.md)*
