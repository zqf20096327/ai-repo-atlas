# Moai-Team-LLC/agentic-product-standard

⭐ 14 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/Moai-Team-LLC/agentic-product-standard) · 组织维护

**面向生产级 agentic 产品的工程标准与 Claude Code 技能集**

提供一套构建生产级 agentic 产品的规范文档（STANDARD.md 产品级、AGENT_STANDARD.md 单 agent 级），内容包括六项原则、自主性阶梯（L0-L4）、监督模式（O0-O2）、9 层 harness、33 项 Definition of Done 与 CI 一致性检查。同时附带两个 Claude Code 技能（agent-builder 与 agentic-product-architect，含 12 个子技能），可经 npx 或 setup.sh 安装进编辑器。setup.sh 可选搭建参考实现 AgenticMind（需 Bun ≥1.3 与 Docker，技能本身不需要）。面向构建 agent 产品的工程团队，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 产品级与单 agent 级两份标准文档，含自主性阶梯与监督模式两轴
- 两个 Claude Code 技能：agent-builder 与 agentic-product-architect（12 个子技能）
- npx skills 一条命令安装技能，或 setup.sh 一键安装并可选搭建 AgenticMind
- 配套 5 个参考实现仓库（Ops/Mind/Performance/Gateway/Assurance），family.sh 可本地拉起

## 适用场景

- 我在设计多 agent 产品时按标准确定自主性等级与人工监督边界
- 把 agent 工程规范装进 Claude Code，在编码与评审时自动加载指导
- 按 33 项 DoD 与 CI 一致性检查评估 agent 是否达到生产级

## 场景标签

 · 领域:AI 工程/标准与技能

## 证据(README 行号)

> L3: ### A canonical standard for building production-grade agentic products — plus a Claude Code skill set that operatio
> L20: Most teams ship agent demos. Few ship agents that survive contact with production. The difference is almost never t
> L47: ├── STANDARD.md                          ← the canonical standard (product level)

## 星数曲线

```mermaid
xychart-beta
    title "Moai-Team-LLC/agentic-product-standard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `43b6b26252f9` · [字段定义](../../DATASET.md)*
