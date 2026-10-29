# msmathcomp/hyperbolic-tsne

⭐ 19 · Python · MIT · 推送 2026-07-29 · [GitHub](https://github.com/msmathcomp/hyperbolic-tsne) · [官网](https://www.computer.org/csdl/journal/tg/5555/01/10432970/1UtXJHM5TZC) · 组织维护

**论文代码：加速双曲空间 t-SNE 降维嵌入方法**

IEEE TVCG 2024 论文《Accelerating hyperbolic t-SNE》的官方代码仓库，提供 hyperbolicTSNE Python 包：将高维数据嵌入双曲空间，使用极坐标四叉树与 Barnes-Hut 近似加速 KL 散度优化。面向希望复现论文实验或对自有高维数据做双曲嵌入的科研用户。构建依赖 C++11/OpenMP 编译器与 Cython 扩展，也提供 Docker 构建方式；仓库附示例 notebook、参数实验脚本及复现论文图表的数据生成与绘图脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hyperbolicTSNE 包支持高维数据的双曲空间 t-SNE 嵌入
- 极坐标四叉树配合 Barnes-Hut 近似加速优化迭代
- 提供 example_basic_usage.ipynb 分步指南与参数实验脚本
- 附复现论文结果的完整脚本链（生成数据→绘图→制表）

## 适用场景

- 对自有高维数据做双曲空间降维可视化
- 复现论文中各数据集（MNIST/WORDNET/PLANARIA 等）的嵌入实验
- 比较不同参数对双曲 t-SNE 结果的影响

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains the code for the paper:
> L64: There are two ways of getting started with the `hyperbolicTSNE` package.

## 星数曲线

```mermaid
xychart-beta
    title "msmathcomp/hyperbolic-tsne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `606c13aca8cf` · [字段定义](../../DATASET.md)*
