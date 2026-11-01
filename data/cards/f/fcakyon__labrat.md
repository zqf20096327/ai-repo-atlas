# fcakyon/labrat

⭐ 444 · Shell · MIT · 推送 2026-10-31 · [GitHub](https://github.com/fcakyon/labrat) · 个人维护

**给 AI 编码 agent 的科研技能插件：论文复现与实验流程**

面向 Claude Code、Codex、Cursor 与 Gemini CLI 的技能插件，由作者从 2200+ 会话中提炼科研防护规则，让 AI agent 按科研方法执行 11 项技能：文献调研、论文复现、消融实验设计、训练启动前检查清单、同 epoch 结果对比、调试、数据集分析、论文核对与撰写、rebuttal 准备等。Claude Code 专属功能包括研究同行评审 hook 与通知（ntfy/Slack/邮件）；论文检索需额外安装 Paper Search CLI（uv、Python 3.10+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 项技能覆盖文献调研、复现、实验设计、对比与论文撰写全流程
- 规则源自真实科研失误案例（误删 checkpoint、无 diff 重启长训练等）
- Claude Code 提供 fresh-context 研究同行评审 hook 与长任务循环监控
- 支持 Claude Code/Codex/Cursor/Gemini CLI 四种 agent 环境

## 适用场景

- 让 Claude Code 复现 arXiv 论文并跑复现实验
- 训练启动前做 pre-flight 检查、避免误重启或误删 checkpoint
- 在同一 epoch 对比多次实验结果
- 准备论文投稿：核对数字、BibTeX 与审稿人预期问题

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Lab Rat teaches your AI coding agent to work like a careful ML researcher: reproduce papers, launch and compare runs
> L62: Every tool gets the same 11 skills. The research peer review and notifications run in Claude Code only. Paper searc


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a8ea81fd51e0` · [字段定义](../../DATASET.md)*
