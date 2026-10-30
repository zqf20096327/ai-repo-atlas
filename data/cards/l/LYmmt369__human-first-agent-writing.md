# LYmmt369/human-first-agent-writing

⭐ 63 · MIT · 推送 2026-09-15 · [GitHub](https://github.com/LYmmt369/human-first-agent-writing) · 个人维护 · 中文 README

**面向 Claude Code 的多 Agent 写作工作流 Skill**

以 SKILL.md 提示词形式提供给 Claude Code 使用的写作工作流：定义 Chief、Researcher、Writer、Editor、Fact-Checker、Archivist 六个角色分工，支持主编协调、指定 Agent、任务分类三种调用方式，覆盖研究、写作、编辑与事实核查流程，写作默认遵循 Human Voice 协议。项目本身是工作流提示，不提供搜索、浏览器或并发能力，可用能力取决于 Agent 宿主；安装方式为克隆或复制到 ~/.claude/skills/ 目录。架构借鉴 newtype-profile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个专业 Agent 角色分工（主编/研究员/作者/编辑/核查员/档案员）
- 三种调用方式：Chief 协调、@指定 Agent、[task:category] 快速模式
- 以 SKILL.md 形式集成到 Claude Code，可与 51+ 其他 SKILL 配合
- 3 层质量检查机制与 Human Voice 写作协议

## 适用场景

- 在 Claude Code 中组织多角色协作完成深度文章写作
- 对生成内容做事实核查与编辑优化
- 将研究、写作、核查组织为结构化工作流以便复盘

## 场景标签

`AI 写作` `多智能体` `工作流自动化` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: **🎯 A practical multi-agent writing workflow for research, drafting, editing, and fact-checking.**
> L42: ### 🎭 6 大专业 Agent
> L95: 复杂任务使用 `Chief`，单一步骤直接调用对应角色。这个项目是工作流提示，不会凭空提供搜索、浏览器或并发能力；可用能力取决于你的 Agent 宿主。

## 星数曲线

```mermaid
xychart-beta
    title "LYmmt369/human-first-agent-writing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-30 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `12f4132e1510` · [字段定义](../../DATASET.md)*
