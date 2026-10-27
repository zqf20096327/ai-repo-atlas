# astro-informatics/harmonic

⭐ 92 · Jupyter Notebook · GPL-3.0 · 推送 2026-03-18 · [GitHub](https://github.com/astro-informatics/harmonic) · [官网](https://astro-informatics.github.io/harmonic/) · 组织维护

**给科研/统计用户：机器学习辅助的贝叶斯证据（边际似然）估计库**

Python 实现的 learned harmonic mean estimator（McEwen et al. 2021），用于计算贝叶斯模型选择所需的边际似然（贝叶斯证据）。仅需后验样本，对 MCMC 采样方法不敏感；可与 emcee、NumPyro 等集成，支持仿射不变集成采样器；支持 normalizing flow 模型与 Savage-Dickey 密度比估计。通过 pip 或源码安装，GPL-3 许可附加非商业使用条件，附 6 篇 arXiv 论文引用要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 learned harmonic mean estimator 计算贝叶斯证据
- 仅需后验样本，对 MCMC 采样技术不可知
- 支持与 emcee / NumPyro 等 MCMC 代码搭配使用
- 支持 normalizing flow 模型与 Savage-Dickey 密度比估计

## 适用场景

- 贝叶斯模型比较时计算边际似然（证据）
- 在 emcee / NumPyro 等采样流程之后做模型选择
- 仿真推断（SBI）项目中的贝叶斯模型比较

## 场景标签

 · 领域:统计/贝叶斯推断（天体物理背景）

## 证据(README 行号)

> L35: ``harmonic`` is an open source, well tested and documented Python implementation of the *learned harmonic mean esti
> L39: While ``harmonic`` requires only posterior samples, and so is agnostic to the technique used to perform Markov chai

## 星数曲线

```mermaid
xychart-beta
    title "astro-informatics/harmonic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-27 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1ea8d525e016` · [字段定义](../../DATASET.md)*
