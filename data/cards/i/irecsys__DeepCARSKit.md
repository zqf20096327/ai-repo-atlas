# irecsys/DeepCARSKit

⭐ 24 · Python · MIT · 推送 2026-06-02 · [GitHub](https://github.com/irecsys/DeepCARSKit) · [官网](https://carskit.github.io/) · 个人维护

**基于深度学习的上下文感知推荐系统库（Python/PyTorch）**

构建于 RecBole v1.0.0 之上的上下文感知推荐库，是 2015 年 Java 版 CARSKit 的深度学习后续。实现基于因子分解机（FM）与神经协同过滤（NeuCF/NeuMF）及 NeuCMF 框架多种变体的上下文感知模型；支持 hold-out 与 N 折交叉验证评估，可按（用户， 上下文）组合输出 top-N 推荐及 precision/recall/NDCG/MRR 等指标，自动保存最优日志，GPU 加速需 CUDA 9.2+。当前仅可通过 git clone 源码使用，内置 DePaulMovie 与 TripAdvisor 数据集，面向推荐系统研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 FM、NeuCF/NeuMF 及 NeuCMF 框架多变体的上下文感知推荐模型
- hold-out 与 N 折交叉验证，按（用户， 上下文）组合输出推荐与 NDCG/MRR 等指标
- 自动保存最优日志，继承 RecBole 的 GPU 加速
- 内置 DePaulMovie 与 TripAdvisor 两个数据集

## 适用场景

- 研究上下文感知推荐算法并进行标准评估
- 复现与对比 NeuCMF 系列模型
- 在自己的数据集上训练上下文感知推荐模型

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L19: be out-dated. Therefore, we develop and release DeepCARSKit which was built upon the RecBole v1.0.0 recommendation 
> L23: + **Implemented Deep Context-Aware Recommendation Models.** Currently, we support the CARS models built based on fa

## 星数曲线

```mermaid
xychart-beta
    title "irecsys/DeepCARSKit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d073979dc65f` · [字段定义](../../DATASET.md)*
