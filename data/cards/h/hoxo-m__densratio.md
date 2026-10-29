# hoxo-m/densratio

⭐ 23 · R · NOASSERTION · 推送 2026-05-01 · [GitHub](https://github.com/hoxo-m/densratio) · [官网](http://hoxo-m.github.io/densratio/) · 个人维护

**R 密度比估计包：从两组样本直接估计 p(x)/q(x)**

面向统计分析与机器学习研究者的 R 包，核心函数 densratio() 从两个未知分布的样本直接估计密度比 w(x)=p(x)/q(x)，无需分别估计各分布。提供 uLSIF（默认）、RuLSIF、KLIEP 三种算法，均基于高斯核线性模型，带宽 sigma 由交叉验证自动选择，支持多维矩阵输入。输出对象可对任意输入计算估计的密度比，可用于异常检测、变点检测、协变量偏移适配等场景。可从 CRAN 或 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种估计方法：uLSIF（默认）/RuLSIF/KLIEP
- 高斯核线性模型，sigma 通过交叉验证自动选择
- 支持多维数据样本（matrix 输入）
- 输出对象含 compute_density_ratio() 可对任意输入计算估计值

## 适用场景

- 做异常检测或变点检测时直接估计密度比
- 协变量偏移（covariate shift）场景下的重要性估计
- 两样本分布比较与研究复现

## 场景标签

 · 领域:统计/机器学习

## 证据(README 行号)

> L26: The package **densratio** provides a function `densratio()` that returns
> L115: `densratio()` has `method` argument that you can pass `"uLSIF"`,

## 星数曲线

```mermaid
xychart-beta
    title "hoxo-m/densratio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `73e6c554cbae` · [字段定义](../../DATASET.md)*
