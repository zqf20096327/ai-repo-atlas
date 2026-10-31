# hamish-mackie/sloop

⭐ 22 · Rust · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/hamish-mackie/sloop) · 个人维护

**Rust 编写的后台编码 agent 调度器：自动运行、审查并合并工单**

面向使用 Claude Code、Codex、OpenCode 等编码 agent 的开发者：每张工单（Markdown 文件）分配独立 Git worktree 与 agent，由 Rust 守护进程在设定工作时段内后台调度执行。流程由阶段组成（action/result_check/fail_action），判定基于自身观察到的证据（进程退出、提交、测试）而非 agent 自述；通过检查后在合并策略下合入分支。提供安装脚本与预编译二进制，SQLite 存储 runtime 状态。

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

- 每工单独立 Git worktree 与 agent，支持并行多 agent 执行
- action 与 result_check 分离，判定基于进程退出/提交/测试等自观察证据
- 流程含 fail_action 策略：fail/continue/return_to 重试
- 工单与项目以 Markdown 文件形式存放于仓库，可分享与重跑

## 适用场景

- 让编码 agent 在后台无人值守地完成积压的工单
- 为每个工单指定不同 agent、模型与力度并自动审查合并
- 用依赖关系（blocked_by）编排多张工单的执行顺序

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Sloop runs agentic coding work autonomously: each ticket gets its own Git
> L27: Under the hood it's a small deterministic kernel that checks what untrusted

## 星数曲线

```mermaid
xychart-beta
    title "hamish-mackie/sloop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f0e4f0f98a73` · [字段定义](../../DATASET.md)*
