# Wennington123/omni-token-optimizer

⭐ 15 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Wennington123/omni-token-optimizer) · 个人维护

**给 AI agent 用的本地 token 优化套件：hooks+行为 skill 降消耗**

面向使用 agent 的开发者，将三个参考项目（Caveman、Punisher Mode、Ponytail）与 6 篇论文的做法合并为两部分：本地 hooks 在工具输出进入模型 API 前过滤截断（shell 输出超 160 行/6000 字符时保留首 40 行、错误行、末 30 行），以及行为系统提示 skill（精简回复、最小 diff、状态表 VARS/TODO/GUARDRAUILS、上下文预算）。通过 install.sh 自动探测 Claude Code/Command Code/OpenCode 的 skills 目录安装，Cursor/VS Code 用 AGENTS.md，Python 自定义 agent 直接集成 hooks。README 给出的节省数字来自其所引论文与自身建模，未见独立验证。

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

- 本地 hooks 过滤工具输出，执行成本 0 token（OpenCode plugin 经 tool.execute.after 真正替换输出）
- Master Skill 含 5 个子技能：精简沟通、最小 diff 执行、观察截断、状态压缩、提示预算
- 安装脚本自动探测 ~/.claude/skills、~/.commandcode/skills、~/.config/opencode/skills
- 基于 9 个来源（3 仓库 + 6 篇论文）并给出激活成本与净节省的数学建模

## 适用场景

- 长任务 agent 会话中降低工具输出与上下文累积的 token 消耗
- 给 Claude Code/OpenCode/Cursor 等 agent 装上精简回复与最小 diff 的行为约束
- 自定义 Python agent 中替换工具返回的日志/CSV 长输出

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L43: 1. **Zero-Token Local Middleware (Hooks)**: Filtra e trunca saídas brutas de ferramentas (terminal, CSVs, respostas
> L181: - **Claude Code / Command Code**: a skill é auto-descoberta na pasta de skills; para o `context_monitor.py` (que f
> L182: - **OpenCode (v2)**: suporte completo via skill + plugin local — veja Integração OpenCode.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `253415535c1c` · [字段定义](../../DATASET.md)*
