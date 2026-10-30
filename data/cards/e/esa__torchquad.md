# esa/torchquad

⭐ 229 · Python · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/esa/torchquad) · [官网](https://www.esa.int/gsp/ACT/open_source/torchquad/) · 组织维护

**面向科研与 ML 社区的 GPU 高维数值积分库**

ESA 维护的 Python 数值积分模块，基于 autoray 构建，支持 PyTorch、JAX、TensorFlow 与 NumPy 四种后端，用户可按需选择数值库并获得完全可微分的积分计算。提供 Monte Carlo、拟 Monte Carlo（Sobol）、Newton-Cotes（Trapezoid/Simpson/Boole）、Gauss-Legendre 等积分方法，面向物理、金融、医学统计等需要高维积分的科研群体与机器学习社区。无强制后端依赖，可 CPU 运行但针对 GPU 优化，GPU 支持仅在 NVIDIA CUDA 上测试，JAX/TensorFlow 的 GPU 构建仅限 Linux/WSL2。支持多 GPU（进程级）与批量向量化积分，附 JOSS 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 API 跨 PyTorch/JAX/TensorFlow/NumPy 四种数值后端，可选完全可微分
- 多种确定性与随机积分方法（Newton-Cotes、Gauss-Legendre、Monte Carlo、Sobol QMC）
- 无强制后端硬依赖，pip/uv/conda 均可安装，需 Python 3.10+
- 支持多 GPU（CUDA_VISIBLE_DEVICES + 独立进程）与批量向量化积分

## 适用场景

- 在 GPU 上计算物理、金融、医学统计中的高维积分
- 机器学习流程中做可微分的数值积分（如归一化常数计算）
- 对比 CPU/GPU 与不同积分方法的精度和运行时间

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L46: The torchquad module allows utilizing GPUs for efficient numerical integration with PyTorch and other numerical Pyt
> L53: * autoray, which means the implemented quadrature supports NumPy and can be used for machine learning with modules 

## 星数曲线

```mermaid
xychart-beta
    title "esa/torchquad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 228 --> 230
    line [229, 229]
```

2026-10-18 229 → 2026-10-30 229（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a8aee9ba33b2` · [字段定义](../../DATASET.md)*
