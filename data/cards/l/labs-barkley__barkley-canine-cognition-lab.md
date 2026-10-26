# labs-barkley/barkley-canine-cognition-lab

⭐ 42 · Jupyter Notebook · NOASSERTION · 推送 2026-08-25 · [GitHub](https://github.com/labs-barkley/barkley-canine-cognition-lab) · [官网](https://getbarkley.com) · 个人维护

**面向个体犬只纵向行为建模的研究框架与合成数据演示**

Barkley Labs 的研究原型仓库，论证以个体自身纵向基线（而非品种平均水平）作为参考系来检测犬只行为的缓慢漂移。提供三个可运行的 Jupyter notebook（个体基线 vs 品种平均、时间漂移检测的 Rolling Z-score/CUSUM、缺失数据作为行为信号），随附合成数据集、Neo4j DogGraph 演示与术语表。声明仅使用合成数据，非临床/兽医诊断工具，也未验证检测性能。寻找真实数据研究合作方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 个体基线参考系检测品种级模型无法察觉的行为漂移
- 三个 notebook：基线对比、CUSUM/滚动Z-score 漂移检测、缺失数据编码
- 内置合成数据集（可由脚本再生成）
- DogGraph 图表示与 Neo4j/Streamlit 自托管演示

## 适用场景

- 行为信息学研究者复现个体基线建模方法
- 探索时间序列漂移检测与缺失数据编码技术
- 作为纵向个体建模研究的概念框架参考

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: **This repository is a technical demonstrator of the DogGraph architecture using synthetic data. It is designed for
> L69: |`02`|Temporal Behavioral Drift Detection|When does gradual change become a detectable signal?|Rolling Z-score, CUS
> L122: ✅ A technical demonstrator using synthetic data only

## 星数曲线

```mermaid
xychart-beta
    title "labs-barkley/barkley-canine-cognition-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `59740d189381` · [字段定义](../../DATASET.md)*
