# lpaiu-cs/osk-system

⭐ 76 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/lpaiu-cs/osk-system) · 个人维护 · 中文 README

**给 LLM agent 用的本地 Markdown 记忆运行时（MCP）**

面向 Claude Code、Codex、Kiro、Antigravity 等 agent 宿主的长期记忆系统：以规则文档（constitution）约束记忆的保留、合并与拆分，Python 引擎通过 stdio 暴露 MCP 工具，知识以本地 Markdown 节点存储，BM25 检索；hooks 捕获对话轮次，agent 在会话内或后台分叉中复习并提炼为带出处（derived-from 指向 _cited/ 轮次）的节点。节点分属 Scope/Domain/Person 三个 Space，支持保护区域、批准快照与 changeset 审批。Obsidian 可选用于浏览图谱，Git 同步为可选项。当前为 developer public beta，macOS 日常使用未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五步循环：捕获→复习提炼→连接组织→召回→复核，节点均引用对话轮次为证据
- MCP 写入经 node-contract 校验，节点记录 author 与 drafter
- 保护区域 + 批准快照 + changeset 的人工审批与回退机制
- 适配 Codex / Claude Code / Kiro / Antigravity 四种宿主的 hooks 与适配器

## 适用场景

- 让跨会话的 agent 对话沉淀为可追溯的项目记忆
- 在 Obsidian 中浏览与编辑 agent 生成的知识图谱
- 多设备下用私有 Git 远端同步记忆库

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L141: A Python engine exposes MCP tools over stdio, stores knowledge in Markdown,
> L144: support **Codex, Claude Code, Kiro and Antigravity**. See the

## 星数曲线

```mermaid
xychart-beta
    title "lpaiu-cs/osk-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-28 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d30d5077c484` · [字段定义](../../DATASET.md)*
