# Furox-Art/scientific-computing-system

⭐ 18 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Furox-Art/scientific-computing-system) · [官网](https://furox-art.github.io/scientific-computing-system/) · 个人维护

**零依赖纯 Python 科学计算库，覆盖数值方法到量子模拟 35 个模块**

名为 cds 的纯 Python 科学计算库，仅依赖标准库，提供 34 个子包加 2 个模块：线性代数（SVD/QR/Cholesky）、ODE/PDE 求解器、数值积分、优化、统计与贝叶斯、蒙特卡洛、信号处理、量子态矢量电路、不确定性量化、灵敏度分析、量纲分析、工作流与溯源等；ML 与 NLP 模块自述为教学用途。同时以 PyPI 包与 npm 启动垫片分发，附 CLI（13 个子命令）、34 个可运行示例与 Streamlit 仪表盘（可选）。README 明确记录限制：稠密数值运算比 NumPy 慢约 3 个数量级（基准记录 100×100 矩阵乘法慢约 1155 倍）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心零运行时依赖，仅用 Python 标准库（505 个导出名称）
- 覆盖 ODE/PDE、积分、优化、统计、蒙特卡洛、量子模拟、不确定性量化等 35 个模块
- pip 安装并提供 cds CLI（13 个子命令）与可选 Streamlit 仪表盘
- PyPI 与 npm 通道均提供 Sigstore 溯源证明（2.2.3 起）

## 适用场景

- 在无第三方依赖环境下做数值计算、求解微分方程
- 教学场景中阅读纯 Python 实现的数值算法
- 科学建模配合不确定性量化、灵敏度与溯源记录

## 场景标签

 · 领域:科学计算/数值方法

## 证据(README 行号)

> L37: The import name is **`cds`** (the distribution is `scientific-computing-system`). The zero-dependency core needs no
> L88: |Machine learning|`cds.ml`|MLP, k-NN, k-means, CART, random forest, boosting, PCA (educational, not production)|
> L100: |NLP (educational)|`cds.nlp`|BPE, embeddings, attention, autograd, MiniGPT|

## 星数曲线

```mermaid
xychart-beta
    title "Furox-Art/scientific-computing-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `35d4434be5af` · [字段定义](../../DATASET.md)*
