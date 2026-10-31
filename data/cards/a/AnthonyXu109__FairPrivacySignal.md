# AnthonyXu109/FairPrivacySignal

⭐ 89 · Python · NOASSERTION · 推送 2026-08-21 · [GitHub](https://github.com/AnthonyXu109/FairPrivacySignal) · [官网](https://doi.org/10.5281/zenodo.20130952) · 个人维护

**隐私规则导致信号缺失下的公平排序基准与信号恢复方法**

面向研究者与工程团队的开源合成基准与参考实现：研究当隐私规则移除个体级行为信号时，排序系统如何保持有用性。核心方法 Policy-Aware Signal Recovery 将训练期的群组统计与交叉拟合的信号重建结合，按可用性策略选择或融合替代信号，下游排序模型不接触受限原始数据。实验以公共服务外展的合成家庭-服务排序为例，报告 NDCG@3、全信号差距闭合率与低信号变化，并包含特征消融、负对照、三种缺失机制、社区留出等压力测试。全部数据为合成，MIT 许可并附 DOI 归档，一条命令可复现全部结果。局限：结果仅在受控合成数据上成立，不声称真实部署效果，曝光分数非正式隐私保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Policy-Aware Signal Recovery：群组统计+交叉拟合重建，按可用性策略选择/融合替代信号
- 五种固定种子合成数据、生成式报告图表、回归测试与一键验证脚本
- 压力测试覆盖特征消融、负对照、三种匹配率缺失机制、社区留出、模型类别等
- MIT 许可、Zenodo DOI 归档，全合成数据无需任何受限数据即可复现

## 适用场景

- 评估隐私规则下排序系统的质量损失与可恢复程度
- 研究数据缺失对不同可观测性人群的分布性影响
- 复现与检查公开的隐私感知信号恢复方法与证据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L61: FairPrivacySignal is an open synthetic testbed and reference implementation for
> L115: |Reproducibility|Five fixed synthetic-data seeds, generated reports and figures, regression tests, and one-command

## 星数曲线

```mermaid
xychart-beta
    title "AnthonyXu109/FairPrivacySignal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-31 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `25f3955ddda4` · [字段定义](../../DATASET.md)*
