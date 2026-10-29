# microsoft/working-with-ai

⭐ 45 · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/microsoft/working-with-ai) · [官网](https://arxiv.org/abs/2507.07935) · 组织维护

**NeurIPS 论文数据：生成式 AI 对各职业适用度的度量结果**

微软研究者论文《Working with AI: Measuring the Applicability of Generative AI to Occupations》(NeurIPS 2026) 的结果数据仓库：基于 2024 年 1–9 月美国 Bing Copilot 对话数据，经 LLM 分类管道映射到 O*NET 中间工作活动（IWA）与 785 个 SOC 职业代码，提供使用份额、完成率、影响范围、正反馈比例及 AI 适用度得分等 CSV 指标，覆盖约 1.498 亿劳动者；数据为聚合形式，不含个人可识别信息，限 CC BY 4.0 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IWA 级与 SOC 职业级（785 个代码）两组聚合指标 CSV
- AI 适用度得分=完成率×影响范围×覆盖的用户侧与 AI 侧均值
- v1.1 新增体力任务分类与非体力 AI 适用度得分
- 提供复现得分的 pandas 计算代码片段

## 适用场景

- 复现论文中 AI 适用度分析或做进一步职业研究
- 将 AI 适用度得分与其他公开职业数据（BLS/O*NET）链接分析
- 了解美国消费级 LLM 在各工作活动中的实际使用与成功情况

## 场景标签

 · 领域:AI 社会影响/劳动经济研究

## 证据(README 行号)

> L4: > Kiran Tomlinson, Sonia Jaffe, Will Wang, Scott Counts, and Siddharth Suri. Working with AI: Measuring the Applicab
> L6:  In particular, they include our metrics aggregated at the O*NET intermediate work activity (IWA) and occupation (de

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/working-with-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-29 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `261000a46a4b` · [字段定义](../../DATASET.md)*
