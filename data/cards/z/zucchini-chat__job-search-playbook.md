# zucchini-chat/job-search-playbook

⭐ 4 · MIT · 推送 2026-11-21 · [GitHub](https://github.com/zucchini-chat/job-search-playbook) · [官网](https://zucchini.chat) · 个人维护

**让已有个人 Agent 代跑求职全流程的 Markdown 剧本**

纯 Markdown 仓库，不含应用与代码：通过一组 playbook 文件指导用户已有的 Claude Code/Codex Agent 代为执行求职——先与用户敲定规则，再进行职位搜寻、筛选、ATS 表单填写、按岗位生成简历版本，并用带类型定义的追踪器与仪表盘记录投递结果。源自约 12 周、约 400 份由 Agent 代投申请的实践经验。运行依赖 Zucchini 聊天、Claude Code 与 shared-chrome-mcp；流程默认处于演练状态，提交前需用户确认。URL 与数据易过时，仓库内置提示说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Markdown playbook，无应用无代码，运行在用户已有的 Agent 上
- 覆盖规则设定、职位搜寻/筛选、ATS 表单、简历版本与追踪仪表盘全流程
- typed tracker（applications.tyaml）与仪表盘记录投递进展
- 默认演练模式，未经用户确认不提交任何申请

## 适用场景

- 让 Claude Code 或 Codex Agent 代替自己完成职位投递流程
- 整理已有投递记录并在仪表盘上查看各申请进展
- 按不同岗位维护多版简历并交给 Agent 选用

## 场景标签

 · 领域:求职/个人生产力

## 证据(README 行号)

> L3: A job-search playbook for the personal agent you already have. It tells your Claude Code or Codex agent how to run a
> L5: There is no app and no code here, only markdown. It was built from about 12 weeks and ~400 applications an agent fil
> L8: - Zucchini: your agent runs in its chats. Zucchini keeps the standing chats running, runs the watch that starts an a

## 星数曲线

```mermaid
xychart-beta
    title "zucchini-chat/job-search-playbook 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-26 4 → 2026-11-27 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a89daaf190e1` · [字段定义](../../DATASET.md)*
