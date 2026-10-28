# fugue-project/tune

⭐ 36 · Python · Apache-2.0 · 推送 2025-12-16 · [GitHub](https://github.com/fugue-project/tune) · 组织维护

**基于 Fugue 的分布式参数调优抽象层，后端无关**

构建于 Fugue 之上的通用参数调优框架：底层 API 不假设目标是机器学习模型，上层 API 提供 Scikit-Learn 兼容模型调优与 Keras 调优；可在 Spark、Dask、本地等 Fugue 支持的任意后端运行，本地测试的调优逻辑无需改代码即可切换到分布式。已集成 HyperOpt（启用贝叶斯优化），Optuna 与 Nevergrad 集成为规划项；支持混合网格/随机/贝叶斯搜索空间及 Successive Halving、Hyperband 的分布式版本。以 pip 安装的 Python 库形式提供，团队正在招募协作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Fugue，可在 Spark、Dask、本地后端间无代码改动切换
- 底层 API 不绑定 ML 模型，视为通用参数调优问题
- 已集成 HyperOpt 贝叶斯优化，可选 Scikit-Learn 组件
- 支持网格/随机/贝叶斯混合搜索空间与分布式 Successive Halving、Hyperband

## 适用场景

- 我在本地小搜索空间验证调优逻辑后切到 Spark/Dask 分布式运行
- 我要对 Scikit-Learn 模型做贝叶斯超参调优
- 我想把第三方优化器接入并仅用其做分布式编排

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L10: Tune is an abstraction layer for general parameter tuning. It is built on Fugue so it can seamlessly run on any bac
> L34: Tune does not follow Scikit-Learn's model selection APIs and does not provide distributed backend for it. **We beli
> L36: Although we didn't base our solution on any of HyperOpt, Optuna, Ray Tune and Nevergrad etc., we are truly inspired

## 星数曲线

```mermaid
xychart-beta
    title "fugue-project/tune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `274e8a2de45b` · [字段定义](../../DATASET.md)*
