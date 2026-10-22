# charlie947/ai-second-brain

⭐ 201 · MIT · 推送 2026-04-17 · [GitHub](https://github.com/charlie947/ai-second-brain) · 个人维护

**引导用户在 Claude Code 中搭建个人 AI 知识库的技能**

一个 Claude Code skill（技能包），通过对话引导非技术用户分三阶段搭建个人知识库：导出 ChatGPT 与 Claude 历史并整理为带标签链接的 Obsidian vault；按 Karpathy 方法建立 raw/wiki 文件夹生成持续更新的 wiki；连接 Gmail、NotebookLM、Granola 与 iMessage Channels 并创建 /today 等斜杠命令。所有数据保留在本机，通过 git clone 安装到 ~/.claude/skills 目录，需已装 Claude Code 与 Obsidian。

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

- 三阶段引导流程：AI Brain 导出整理 / Karpathy Wiki / Living Wiki 连接外部服务
- 整理 ChatGPT 与 Claude 历史为可搜索的 Obsidian vault
- 数据保留在本机，卸载不影响 vault 与 wiki 数据
- 需人工确认的步骤会暂停等待用户操作

## 适用场景

- 把我的 ChatGPT 和 Claude 对话历史整理成可搜索的知识库
- 按 Karpathy 方法用文件夹和 LLM 维护一个持续更新的个人 wiki
- 通过 iMessage 或连接器从手机和外部应用访问第二大脑

## 场景标签

 · 领域:个人知识管理

## 证据(README 行号)

> L3: > A Claude Code skill that walks you through building a living, searchable, AI-powered knowledge base from your own 
> L56: 1. **AI Brain** — exports your full ChatGPT and Claude history and turns the lot into a tagged, linked Obsidian vau
> L64: - Claude Code installed and working

## 星数曲线

```mermaid
xychart-beta
    title "charlie947/ai-second-brain 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 197 --> 202
    line [198, 201, 201]
```

2026-10-18 198 → 2026-10-22 201（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cd3ded6d20c7` · [字段定义](../../DATASET.md)*
