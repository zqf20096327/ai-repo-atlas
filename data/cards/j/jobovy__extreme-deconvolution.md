# jobovy/extreme-deconvolution

⭐ 85 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/jobovy/extreme-deconvolution) · 个人维护

**从噪声异质数据估计分布的高斯混合去卷积库**

实现 extreme-deconvolution 算法：在观测含噪声、异质且不完整（含协方差不确定度）的条件下，用高斯混合推断 d 维分布函数。核心为 C 库，提供 Python、R、IDL 包装器调用底层 C 代码；支持 OpenMP 多线程（OMP_NUM_THREADS 控制）、数据点权重、对角协方差等选项。算法源自 Bovy, Hogg & Roweis 2011 论文（Ann. Appl. Stat.），代码在天文及天文以外领域均有应用。安装需先装 GSL，通过 git clone 后 make 编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从含噪声与协方差不确定度的观测推断高斯混合分布
- C 核心库，提供 Python/R/IDL 包装器
- OpenMP 多线程支持，可用环境变量控制线程数
- 支持数据点权重与对角（不相关）数据不确定度

## 适用场景

- 天文观测数据中恢复被测误差模糊的底层分布
- 对带个体不确定度的异质样本做密度估计
- 在 Python/R/IDL 高层环境中调用快速 C 实现

## 场景标签

 · 领域:统计机器学习/天文数据分析

## 证据(README 行号)

> L10: Extreme-deconvolution (XD) is a general algorithm to infer a d-dimensional distribution function from a set of hete
> L12: The extreme-deconvolution algorithm is available here as a dynamic C-library that your programs can link to, or thr
> L160: The algorithm that the code implements is described in the paper *Extreme deconvolution: inferring complete distri

## 星数曲线

```mermaid
xychart-beta
    title "jobovy/extreme-deconvolution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-31 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `35f6e937c793` · [字段定义](../../DATASET.md)*
