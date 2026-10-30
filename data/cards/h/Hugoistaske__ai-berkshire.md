# Hugoistaske/ai-berkshire

⭐ 23 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/Hugoistaske/ai-berkshire) · [官网](https://github.com/Hugoistaske) · 个人维护 · 中文 README

**基于 Claude Code 的价值投资研究 Skill 合集与金融验算工具**

面向个人投资者的 Claude Code Skill 合集：将巴菲特、芒格、段永平、李录四位投资人方法论结构化为 5 个研究命令（四大师综合分析、多 Agent 并行团队、买入前 Checklist、产业链扫描、未上市公司研究），强制输出通过/不通过/灰色的结论与分层价格区间。附带 Python 金融严谨性工具，用 decimal.Decimal 做市值验算、多源交叉验证、三情景估值与 Benford 定律检测。需先安装 Claude Code，复制 skills 文件到其 commands 目录后调用。README 声明仅供学习研究，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个 Skill：综合分析/多Agent团队/Checklist/产业链/未上市公司研究
- 多 Agent 并行研究同一公司，4 视角独立评分后综合
- financial_rigor.py 提供市值验算、多源交叉验证、Benford 定律检测等精确计算
- 内置信息丰富度 A/B/C 评级、8 条快速否决红线等反偏见机制

## 适用场景

- 用 Claude Code 对一家上市公司做多视角深度投资研究
- 一次筛选多家公司，按统一 Checklist 决定是否深入研究
- 对一个投资主题做产业链全景扫描
- 对未上市公司做多方法交叉估值

## 场景标签

`金融量化` `多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L7: **AI Berkshire** 是一套基于 Claude Code 的投资研究 Skill 合集，将巴菲特、芒格、段永平、李录四位价值投资大师的方法论系统化、结构化，通过 AI Agent 实现专业级投资研究。
> L142: |`/investment-research`|四大师综合深度分析|对一家上市公司进行全方位投资研究|

## 星数曲线

```mermaid
xychart-beta
    title "Hugoistaske/ai-berkshire 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `60ba36a0d389` · [字段定义](../../DATASET.md)*
