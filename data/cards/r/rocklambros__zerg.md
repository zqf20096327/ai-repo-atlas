# rocklambros/zerg

⭐ 35 · Python · MIT · 推送 2026-04-19 · [GitHub](https://github.com/rocklambros/zerg) · 个人维护

**协调多个 Claude Code 实例并行开发功能的执行系统**

ZERG 是 Python CLI 工具，用于编排多个 Claude Code 实例（zergling）并行构建软件功能：自动检测技术栈、从 TikiTribe/claude-secure-coding-rules 拉取安全规则（OWASP Top 10 2025 等）、生成 dev container 配置、将功能拆分为带独占文件所有权的原子任务，在隔离 git worktree 中并行执行，避免合并冲突。Worker 无状态、读取规格文件而非对话历史以应对上下文遗忘。提供 26 个 slash 命令覆盖 brainstorm/plan/design/rush/monitor/review/test/security/git 全流程。前置要求 Python 3.12+、Git、Claude Code CLI，Docker 容器模式为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 功能拆分为带独占文件所有权的原子任务，5-10 个 Claude Code 实例并行执行无合并冲突
- 无状态 spec 驱动 worker：崩溃后重启可从断点继续
- 三种执行隔离模式：task/subprocess/Docker 容器
- 从外部仓库自动拉取技术栈相关安全规则并按文件扩展名过滤

## 适用场景

- 多文件功能开发时并行运行多个 Claude Code 实例缩短交付时间
- 为项目统一配置安全编码规则与 dev container 脚手架
- 对并行产出执行代码审查、测试与 OWASP 安全扫描

## 场景标签

`编码 Agent` `多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Zero-Effort Rapid Growth** — A parallel Claude Code execution system that coordinates multiple Claude Code instan
> L29: **ZERG breaks features into parallel tasks** with exclusive file ownership, so 5-10 Claude Code instances work simu

## 星数曲线

```mermaid
xychart-beta
    title "rocklambros/zerg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `01e322b6ca78` · [字段定义](../../DATASET.md)*
