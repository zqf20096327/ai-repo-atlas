# syncra-studio/brigadier-skill

⭐ 3 · Shell · MIT · 推送 2026-11-27 · [GitHub](https://github.com/syncra-studio/brigadier-skill) · 组织维护

**给 Claude Code 排班多 worker 夜间自动干活的编排技能**

Brigadier 是一个 Claude Code skill：用户给定目标后，它在 cmux/tmux 终端中派出多个独立的 Claude Code（可选 Codex）worker 会话并行执行任务。它依据用户的计划、CLAUDE.md 和规则代答 worker 的问题，在 worker 上下文将满时以交接文件替换新会话，每阶段由独立会话核验 diff 与完成条件，运行结束生成报告。安装需 skills.sh 或 Claude Code 插件机制，setup 会检查 git、jq、claude、终端复用器等依赖。安全文档说明默认权限绕过、订阅额度消耗及禁推/禁付费等规则限制。

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

- 在 cmux/tmux 中运行多个独立 Claude Code/Codex worker 会话
- 上下文将满时写交接文件并由新会话接续，而非压缩
- 每阶段由独立会话核验 diff 与 done-when 条目
- 代答有边界：推送、付费、注册等操作列入 Waiting on you

## 适用场景

- 睡前下达编码任务，早上查看提交与晨报
- 用多个 worker 会话并行推进 PLAN.md 的多个阶段
- 在 5 小时额度窗口用满时切换 Codex 处理有界任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9: Brigadier is a Claude Code skill that keeps work moving while you sleep. It runs a crew of Claude Code workers (plus
> L64: - **One brigadier, a few workers.** Your session becomes the brigadier. It doesn't write code. Each worker is a ful


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e576b8b76afb` · [字段定义](../../DATASET.md)*
