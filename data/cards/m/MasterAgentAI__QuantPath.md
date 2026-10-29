# MasterAgentAI/QuantPath

⭐ 21 · Python · NOASSERTION · 推送 2026-04-03 · [GitHub](https://github.com/MasterAgentAI/QuantPath) · 个人维护 · 中文 README

**给 MFE 申请者的录取概率预测与选校 CLI 工具**

面向金融工程（MFE）硕士申请者的命令行工具：基于 13,100+ 条录取记录与 31 个项目数据库，用逐项目逻辑回归（v1）和 GPBoost 混合效应模型（v2，AUC 0.723）输出录取概率、reach/target/safety 分类，并提供五维背景评分（37 子因子）、先修课匹配、学费/薪资 ROI、申请组合预算优化等 15+ 子命令。含幸存者偏差校正（用官方录取率替换截距）。可选接入 Claude 生成 AI 咨询报告；数据以匿名化 GitHub issue 众包回流。安装需 git clone 后 pip install -e .，Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个聚焦项目的 P(admit) 预测与置信区间（v1 逻辑回归为主，v2 GPBoost 为备）
- 自报数据的幸存者偏差校正（King & Zeng 2001）
- 五维背景评分（37 子因子）、差距分析与课程推荐
- 匿名化数据经 GitHub issue 众包回流用于校准

## 适用场景

- 评估自己在 15 个 MFE 项目的录取概率并划分 reach/target/safety
- 在申请预算约束下优化选校组合并比较学费、薪资与 NPV
- 生成 AI 咨询报告与逐月申请行动计划

## 场景标签

 · 领域:教育/录取预测

## 证据(README 行号)

> L3: **MFE admission prediction engine** — GPBoost mixed-effects model on 13,100+ records across 31 programs. Profile sco
> L39: **v2 (fallback)**: GPBoost -- LightGBM gradient boosting with per-program random intercepts. Trained on 11,100+ lab
> L49: |**`quantpath predict`**|**Primary entry point** -- P(admit) for 15 focused programs, reach/target/safety (no trans

## 星数曲线

```mermaid
xychart-beta
    title "MasterAgentAI/QuantPath 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7c87b4c8164c` · [字段定义](../../DATASET.md)*
