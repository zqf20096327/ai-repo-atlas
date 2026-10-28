# theonly1me/shadowclone

⭐ 22 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/theonly1me/shadowclone) · [官网](https://shadowclone.co) · 个人维护

**统一管理并分发个人编码规范技能到多种编码 agent 的工具**

面向使用多种编码 agent（Claude Code、Codex、Cursor、Pi、Antigravity、OpenCode）的开发者：维护一套技能与指令，分发给各 agent，避免逐工具复制规则。可从用户授权的会话中学习规则并转为可读、可编辑、可撤销的技能；支持以 Docker 容器在本机运行 clone 代为提交草稿 PR，并通过 GitHub Actions bot 在云端执行任务与 PR 审查。提供 CLI 安装、技能向导与本地 review 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套技能同步到六种编码 agent
- 从授权会话学习规则并转为可读可撤销的技能
- clone 在本机 Docker 中代为工作并提交草稿 PR
- GitHub Actions bot 支持 Anthropic/OpenAI/OpenAI 兼容端点/Cursor 的 API key

## 适用场景

- 在多个编码 agent 之间保持同一套工程规范
- 让 clone 在自己机器上离线时代为修 bug 并开 PR
- 团队共享一个带技能的 GitHub Actions bot 处理 issue 与审查

## 场景标签

 · 领域:开发者工具/编码 agent 基础设施

## 证据(README 行号)

> L10: **shadowclone keeps your engineering preferences the same in every coding agent.** It maintains one set of skills a
> L12: **It works as you while you are away.** Ask your agent to start a clone. Claude Code or Codex works with your skill

## 星数曲线

```mermaid
xychart-beta
    title "theonly1me/shadowclone 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `205c5e7bb8e5` · [字段定义](../../DATASET.md)*
