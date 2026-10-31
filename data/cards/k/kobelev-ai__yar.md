# kobelev-ai/yar

⭐ 14 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/kobelev-ai/yar) · 个人维护

**给高管的生产力文件夹规则系统：让 AI 助手基于本地文件持续完成任务**

以纯文件夹结构与 Markdown 规则构成的工作系统：将任务材料放入 tasks/，由 Claude Code、Codex 等文件夹型 AI 助手读取规则（CLAUDE.md/AGENTS.md）后执行任务、保存结果与续作指针，并提供 GTD 式行动清单（ops/gtd/todo.md）、收件箱路由、会议转录处理与带来源的记忆索引。数据留在用户本地文件夹，模型与应用可更换；Python 3.10+ 仅用于可选的初始化、演示与升级脚本。基于 Claude Code 构建，MIT 许可。

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

- tasks/inbox/GTD 三层结构，任务结果保存在本地文件夹并支持续作
- 兼容 Claude Code、Codex 及其他文件夹型助手（读取 AGENTS.md）
- 带来源索引的记忆：原文与派生摘要并存，决策需人工确认
- python3 scripts/yar_workspace.py 提供 init/demo/升级辅助

## 适用场景

- 把材料丢进文件夹，让 AI 助手产出对比、摘要等可续作的结果
- 用 GTD 清单和收件箱路由管理待办与 incoming 文件
- 处理会议转录并提取行动项与待确认事项

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L38: - **Claude Code:** reads `CLAUDE.md`; workflows are in `.claude/skills/<name>/SKILL.md`.
> L42: - **Other folder-enabled assistants:** give access to the folder and explicitly
> L43:  ask them to read `AGENTS.md`. Check file/tool support and permissions first.

## 星数曲线

```mermaid
xychart-beta
    title "kobelev-ai/yar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `59c89dbc555d` · [字段定义](../../DATASET.md)*
