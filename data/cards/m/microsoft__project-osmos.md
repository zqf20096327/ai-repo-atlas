# microsoft/project-osmos

⭐ 17 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/project-osmos) · 组织维护

**面向 Copilot/Claude Code/Codex 的 Microsoft Fabric 数据工程技能插件**

Project Osmos 是一个数据工程 agent 技能，使用自然语言在 Microsoft Fabric 中探索 Lakehouse 数据、构建 notebook 并运行数据工程工作流。当前以 Skills for Fabric（SFF）集合中的 fabric-skills 技能分发，取代旧的独立包 project-osmos@project-osmos；README 主体为迁移与更新指引：通过 Copilot CLI、Claude Code、Codex 的插件命令注册 microsoft/skills-for-fabric 市场并安装，涵盖旧安装更新、进行中任务的恢复处理与旧包清理，MIT 许可，由 Microsoft 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言探索 Fabric Lakehouse 数据、构建 notebook、运行数据工程工作流
- 通过 SFF 市场分发，支持 Copilot CLI / Claude Code / Codex 三种客户端的插件命令安装与更新
- 提供旧独立包的迁移指引、任务恢复保护与清理流程

## 适用场景

- 在 Copilot/Claude Code/Codex 中用自然语言操作 Fabric Lakehouse 数据
- 数据工程师在熟悉的编码 agent 内完成 Fabric 数据工程任务
- 从旧的 project-osmos 独立包迁移到 SFF 集合并清理旧安装

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Project Osmos is a data engineering agent for Microsoft Fabric. Use natural language
> L14: Install `fabric-skills@fabric-collection` using your client's commands below.
> L33: |Copilot CLI|`copilot plugin marketplace add microsoft/skills-for-fabric`|`copilot plugin install fabric-skills@fab

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/project-osmos 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `19fa1e22aa62` · [字段定义](../../DATASET.md)*
