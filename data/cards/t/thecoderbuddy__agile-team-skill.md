# thecoderbuddy/agile-team-skill

⭐ 10 · Shell · 推送 2026-09-01 · [GitHub](https://github.com/thecoderbuddy/agile-team-skill) · 个人维护

**为独立开发者提供 AI 敏捷团队的多 agent 工作流插件**

基于 Claude Code 插件机制构建的敏捷流程多 agent 套件：13 个角色化 agent（PO、PM、dev、QA、安全、tech-lead 及 6 个扩展专家）通过 30 个斜杠命令覆盖 /init、/sprint-plan、/standup、/review、/retro 等仪式；/review 中 QA 有硬否决，四个 agent 顺序审查 diff 后由 PO 汇总结论。提供 Pixel Office 浏览器实时可视化、NEXT.md/CHECKPOINT.md 会话恢复，每个 agent 可在 frontmatter 中独立指定 sonnet/opus/haiku 模型。支持插件市场安装或 install.sh 脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个单职责 agent + 30 个命令的敏捷仪式流程
- QA 硬否决的安全审查管线（OWASP、secrets、CVE 扫描）
- NEXT.md/CHECKPOINT.md 跨会话状态恢复机制
- Pixel Office 浏览器端实时可视化，仅依赖 Python 内置 http.server

## 适用场景

- 独立开发者按敏捷流程管理需求、评审与迭代
- 用 AI 对每次代码 diff 做安全与质量审查
- 在多次会话间保持冲刺状态并续接中断任务链

## 场景标签

`多智能体` `代码审查` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: > An AI agentic team designed for your agile workflow. For anyone building a product independently — with the discip
> L33: This gives you that team. An AI agentic team designed around your agile workflow, not a single assistant trying to 
> L249: /plugin install agile-team@agile-team-marketplace


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `58f21ea3a97e` · [字段定义](../../DATASET.md)*
