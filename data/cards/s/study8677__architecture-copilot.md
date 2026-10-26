# study8677/architecture-copilot

⭐ 85 · MIT · 推送 2026-07-10 · [GitHub](https://github.com/study8677/architecture-copilot) · 个人维护 · 中文 README

**给 Claude Code/Cursor/Codex 的架构引导 skill：写码前用提问理清架构**

面向 Claude Code、Cursor、OpenAI Codex 等 AI 编程助手的『架构共创』skill：以固定引导流程（改编自 awesome-architecture 的『灵魂六问』与『八步设计法』）在动手写代码前持续深度提问，经七个阶段收敛出架构全景图、数据模型、ADR 决策记录、瓶颈预警、演进路线与风险清单。以三种即取即用的文件形态分发（SKILL.md / .cursor 规则 / AGENTS.md），也可直接作为系统提示粘贴给其它 AI。方法论与模板来自同作者的 awesome-architecture 仓库。

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

- 七阶段引导流程：业务范围→灵魂六问→信封背面估算→质量属性取舍→关键决策追问→收敛产出→反挑战
- 产出架构图、数据模型、ADR、瓶颈预警、演进路线与风险清单
- 三种工具形态即取即用：SKILL.md、Cursor 规则文件、AGENTS.md，正文可粘贴为任意 AI 的系统提示
- 方法论源自 awesome-architecture，引导时会引用对应模板（如电商平台关键决策）

## 适用场景

- 开新项目时让 AI 助手先陪我通过提问想清架构再写代码
- 在 Claude Code/Cursor/Codex 中获得架构决策记录与演进路线产出
- 准备系统设计讨论或评审前的架构梳理

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 一个给 **Claude Code / Cursor / OpenAI Codex** 用的「架构共创」skill。
> L54: |**Claude Code**|`skills/architecture-copilot/SKILL.md`|`~/.claude/skills/` 或项目 `.claude/skills/`|
> L67: |📚|**awesome-architecture**|**知识**:架构思维教程 + 数十个模板/架构地图(只讲架构、不讲语法,数量以上游为准)。还有一个可交互教学站。|

## 星数曲线

```mermaid
xychart-beta
    title "study8677/architecture-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-26 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7d1d7cfd3fd1` · [字段定义](../../DATASET.md)*
