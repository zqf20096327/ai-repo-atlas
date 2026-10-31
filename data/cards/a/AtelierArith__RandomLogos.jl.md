# AtelierArith/RandomLogos.jl

⭐ 15 · Julia · MIT · 推送 2025-11-24 · [GitHub](https://github.com/AtelierArith/RandomLogos.jl) · [官网](https://atelierarith.github.io/RandomLogos.jl/dev/) · 个人维护

**Julia 实现的 SVD-IFS 随机分形图案生成器**

用 Julia 重现 Connor Anderson 与 Ryan Farrell 提出的基于 SVD 的 IFS（迭代函数系统）采样算法，生成装饰性分形图形；原算法为 Python 实现，本项目改用 JIT 编译的 JuliaLang。使用方式：安装 Julia 1.9.1 后 git clone 仓库，以 julia --project 运行 Pkg.instantiate 安装依赖并执行示例脚本，更多示例见 README 链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SVD 的 IFS 采样算法生成随机分形对象
- 以 Julia 实现原 Python 算法
- 通过 Julia 项目环境（Pkg.instantiate）运行示例

## 适用场景

- 生成分形艺术图案或随机 logo 素材
- 研究 SVD-IFS 采样算法的 Julia 实现

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: This repository aims to generate fancy fractal objects using an algorithm based on the SVD-based approach for sampli

## 星数曲线

```mermaid
xychart-beta
    title "AtelierArith/RandomLogos.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `22c6b72df348` · [字段定义](../../DATASET.md)*
