# izzatum/laplace-hypopinn

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-10-18 · [GitHub](https://github.com/izzatum/laplace-hypopinn) · [官网](https://izzatum.github.io/laplace-hypopinn/) · 个人维护

**基于 PINN 与 Laplace 近似的地震震源定位研究库**

Python/PyTorch 科研软件包：给定速度模型与接收走时，训练受 Eikonal 方程约束的二维走时场 PINN，估计震源位置，并用对角、块对角、KFAC、满秩等八种 Laplace 近似方法探索局部网络权重不确定性。随附 Izzatullah et al. (2022) 论文，提供八个教程 notebook、可配置模型深度宽度、TOML 配置、Python API 与 CLI。教程与测试在 CPU 上运行，校准性未由教学示例确立。

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

- PINN 求解 Eikonal 方程约束的二维走时场并定位震源
- 八种 Laplace 近似方法（diagonal/kfac/full/efb 等）各有教程 notebook
- CLI 与 Python API 支持自定义宽度、方法与 TOML 配置
- 保留论文原始研究 notebook 及历史输出

## 适用场景

- 做地震/微地震震源定位的科研实验
- 比较不同 Laplace 近似方法的不确定性估计
- 复现并扩展 Izzatullah et al. (2022) 论文结果

## 场景标签

`科研工具` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **Laplace HypoPINN** is a Python/PyTorch research package for earthquake and
> L5: Given a velocity model and receiver travel times, it learns a two-dimensional
> L6: travel-time field constrained by the Eikonal equation, estimates the source
> L7: location, and uses Laplace approximations to explore local network-weight uncertainty.

## 星数曲线

```mermaid
xychart-beta
    title "izzatum/laplace-hypopinn 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-19 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `cd9032fc5fca` · [字段定义](../../DATASET.md)*
