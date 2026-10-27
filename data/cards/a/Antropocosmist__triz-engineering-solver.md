# Antropocosmist/triz-engineering-solver

⭐ 23 · MIT · 推送 2026-05-16 · [GitHub](https://github.com/Antropocosmist/triz-engineering-solver) · 个人维护

**面向 Claude/AI agent 的 TRIZ 工程矛盾求解技能**

以 SKILL.md 形式提供的 agent 技能：针对工程矛盾（改善 X 使 Y 恶化、物理矛盾）生成 3-5 个带理想度评分的发明方案。内置 Altshuller 39×39 矛盾矩阵（1190 格）、40 条发明原理、Su-Field 分析与 76 条标准解、ARIZ-85C 深度流程和 8 条演化趋势。决策点以结构化资源查表为主，超范围问题显式拒绝并给出重定向建议。通过 git clone 安装到 Claude Code 技能目录，或由其他 agent 运行时指向 SKILL.md 使用。

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

- 完整 39×39 矛盾矩阵（1190 格，经锚点校验）与 40 条发明原理
- Su-Field 分析含 76 条标准解（5 类分类法）
- ARIZ-85C 深度流程：快速路径未达标时升级处理
- 超范围问题拒绝并重定向（refuse-with-reframe）

## 适用场景

- 工程权衡陷入僵局时生成非折衷的发明方案
- 用系统化方法处理物理矛盾（分离原理）
- 技术路线图问题参考工程系统演化 8 趋势

## 场景标签

 · 领域:工程方法论/知识资源

## 证据(README 行号)

> L3: A Claude / AI-agent skill for solving engineering problems with Altshuller's **TRIZ** (Theory of Inventive Problem S
> L44: For other agent runtimes (Anthropic SDK, OpenAI Assistants, LangGraph, custom): point the agent's system prompt or 

## 星数曲线

```mermaid
xychart-beta
    title "Antropocosmist/triz-engineering-solver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `73d3f1c9d68a` · [字段定义](../../DATASET.md)*
