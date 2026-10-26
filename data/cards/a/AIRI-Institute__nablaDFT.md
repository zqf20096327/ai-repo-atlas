# AIRI-Institute/nablaDFT

⭐ 241 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/AIRI-Institute/nablaDFT) · [官网](https://doi.org/10.1039/D2CP03966D) · 组织维护

**药物类分子量子化学数据集与神经网络势基准（1,936,931 分子）**

面向神经网络势（NNP）研究的量子化学数据集与基准：基于 MOSES 子集收录约 193 万分子、1,267 万构象，提供能量、力、17 种分子性质、DFT 哈密顿与重叠矩阵及波函数文件（ωB97X-D/def2-SVP，Psi4 计算），并含弛豫轨迹。基准覆盖分子性质预测、哈密顿预测与构象优化任务，配套可扩展训练框架实现 10 个模型（SchNOrb、PhiSNet、GemNet-OC、QHNet 等）及预训练检查点。以 git clone + pip install 源码方式安装，数据经 wget 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 193 万分子、1,267 万构象，含能量/力/哈密顿与重叠矩阵/波函数
- DFT 水平 ωB97X-D/def2-SVP，Psi4 1.5 计算全部性质
- 覆盖性质预测、哈密顿预测、构象优化三类任务的基准与 MAE 指标表
- 可扩展训练框架内置 10 个模型并提供预训练检查点

## 适用场景

- 训练与评测神经网络势模型用于分子性质/哈密顿预测
- 药物发现相关的构象能量与优化研究
- 下载 DFT 波函数文件做后续量子化学计算

## 场景标签

`模型评测` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L12: This work presents a new dataset and benchmark called $\nabla^2$ DFT that is based on the nablaDFT. It contains twi
> L14: Moreover, $\nabla^2$ DFT is the first dataset that contains relaxation trajectories for a substantial number of dru
> L37: We propose a benchmarking dataset based on a subset of Molecular Sets (MOSES) dataset. Resulting dataset contains 1

## 星数曲线

```mermaid
xychart-beta
    title "AIRI-Institute/nablaDFT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 240 --> 242
    line [241, 241]
```

2026-10-18 241 → 2026-10-26 241（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `94e2f99e930b` · [字段定义](../../DATASET.md)*
