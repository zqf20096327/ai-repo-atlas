# NYU-DiffusionMRI/SMI

⭐ 30 · MATLAB · 推送 2026-09-25 · [GitHub](https://github.com/NYU-DiffusionMRI/SMI) · 组织维护

**MATLAB 工具箱：估计白质扩散标准模型参数**

面向扩散 MRI 研究者的 MATLAB 工具箱，对白质 Standard Model 做参数估计：先用最小二乘估计扩散信号的旋转不变量，再用基于前向模型生成训练数据的数据驱动机器学习回归（默认三次多项式）估计 SM 参数。输入为 4D 扩散加权数据、FSL 格式协议文件与噪声图，支持多种 b 张量形状与可变回波时间，输出组织分数、扩散率及可选的隔室 T2 值。不适用于灰质；当前实现仅限 MATLAB，相关发展含美国专利。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 旋转不变量 + 机器学习回归的两步参数估计流程
- 支持多 b 值、多种轴对称 b 张量形状与可变回波时间输入
- 输出分数、各向异性、扩散率及（可变 TE 时）隔室 T2 图
- 提供三个 DESIGNER 预处理过的示例数据集与 example.m 脚本

## 适用场景

- 对临床扩散 MRI 数据估计白质微结构参数
- 研究可变 TE / b 张量形状对参数估计的作用
- 生成可用于 MRtrix3 纤维追踪的 ODF 球谐分解

## 场景标签

 · 领域:医学影像/神经科学

## 证据(README 行号)

> L86: Then, the SM parameters are estimated from the rotational invariants of the signal (up to L=4 as default option). U
> L1: # Standard Model Imaging (SMI) toolbox

## 星数曲线

```mermaid
xychart-beta
    title "NYU-DiffusionMRI/SMI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d253e7ec26b4` · [字段定义](../../DATASET.md)*
