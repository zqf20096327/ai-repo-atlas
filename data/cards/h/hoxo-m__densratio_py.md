# hoxo-m/densratio_py

⭐ 135 · Python · MIT · 推送 2026-05-05 · [GitHub](https://github.com/hoxo-m/densratio_py) · [官网](https://github.com/hoxo-m/densratio_py) · 组织维护

**密度比估计 Python 库：从两组样本估计 p(x)/q(x)**

提供 densratio() 及 uLSIF/RuLSIF/KLIEP 方法封装，从两个未知分布的样本直接估计密度比 w(x)=p(x)/q(x)，基于线性高斯 RBF 核模型，带宽经交叉验证自动选择，返回对象可对新样本计算密度比。支持 alpha 相对密度比及 PE/KL 散度计算，支持多维数据输入。计算内核可选 numpy 或 numba（单线程/多线程）。适用于离群检测、协变量偏移适应等场景，多篇论文使用该包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 uLSIF（默认）/RuLSIF/KLIEP 三种估计方法
- alpha 相对密度比及 PE/KL 散度计算
- 带宽 sigma 经交叉验证自动选择
- 高斯核计算引擎可选 numpy 或 numba（cpu/parallel）

## 适用场景

- 基于内点样本做离群检测
- 协变量偏移下的重要性加权
- 比较两个分布并输出散度度量

## 场景标签

 · 领域:机器学习/统计计算

## 证据(README 行号)

> L11: **Density ratio estimation** is described as follows: for given two data
> L21: The package **densratio** provides `densratio()` and method-specific
> L133: - `uLSIF(x, y, ...)` estimates the ordinary density ratio

## 星数曲线

```mermaid
xychart-beta
    title "hoxo-m/densratio_py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-30 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0f932360c2cf` · [字段定义](../../DATASET.md)*
