# khakhasshi/LLM_QUANT_FACTORY

⭐ 70 · Python · NOASSERTION · 推送 2026-08-05 · [GitHub](https://github.com/khakhasshi/LLM_QUANT_FACTORY) · 个人维护 · 中文 README

**A 股多因子研究工作台：LLM 辅助因子发现与受约束组合回测**

面向 A 股截面多因子研究的源码可用单体仓库：数据工程层审计不可变日频快照并构建 DuckDB/Parquet 面板；研究平台层提供 AutoAlpha 连续因子研究、LLM 辅助的 AutoCombine 组合研究、不调用 LLM 的 QuantCombine 确定性组合优化（SFFS、NSGA-II）、结构化 LLM 研究团队、因子知识库、截面选股器与手动纯多回测。LLM 仅提出假设与受控表达式，回测、统计检验、风险门禁由确定性组件执行。要求 macOS/Linux、Python 3.12+、uv 与自有授权 A 股数据；当前验证数据为 non-PIT 研究代理数据，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AutoAlpha 连续因子研究流水线：机制诊断→候选生成→时序校验→纯多评价→审计落库
- QuantCombine 不调用 LLM，用 SFFS/NSGA-II/Pareto 排序做因子筛选与非负权重优化
- 因子知识库保存公式与 AST、机制类型、行为簇、生命周期与失效标签
- 隐藏测试细节不进入 LLM 上下文，生产候选须人工审批

## 适用场景

- 在自有授权 A 股数据上做可审计的因子发现与组合研究
- 用确定性优化引擎做纯多组合权重筛选与回测
- 管理因子知识库并识别换皮参数因子

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L19: LLM_QUANT_FACTORY 的目标不是让大语言模型直接“决定买什么”，而是把模型放在一个可审计、可证伪、
> L20: 受确定性协议约束的研究系统里。LLM 负责提出机制假设、生成受控表达式和形成结构化研究意见；
> L47: 不调用 LLM，使用 SFFS、NSGA-II、自适应采样和 Pareto 排序完成因子筛选、子集搜索与非负权重

## 星数曲线

```mermaid
xychart-beta
    title "khakhasshi/LLM_QUANT_FACTORY 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-25 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c65e214244bf` · [字段定义](../../DATASET.md)*
