# LopezGroup-ICIQ/care

⭐ 94 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/LopezGroup-ICIQ/care) · [官网](https://doi.org/10.1038/s44286-026-00361-8) · 组织维护

**多相催化反应网络自动构建与微动力学模拟框架**

面向多相催化研究的端到端框架：自动生成与处理化学反应网络（CRN），接入多种 ML 原子间势能模型（GAME-Net-UQ、FairChem、MACE、UPET、Orb、SevenNet）评估吸附能与反应能，再经 Julia 后端进行微动力学 ODE 求解，量化催化活性并计算表观动力学与速率/选择性控制度。支持 CHONS+卤素物种体系，提供 care_run 一键流程脚本与 Colab 教程。以 Python 包形式发布，不同 ML 评估器因后端依赖需分环境安装。

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

- 自动生成化学反应网络（SMILES/碳氧截断数/化学空间三种方式）
- 接入 7 种 MLIP 能量评估器（MACE、FairChem、Orb、SevenNet 等）
- Julia 后端微动力学模拟，自动下载安装 Julia 环境
- care_run 脚本一键完成网络生成→能量评估→动力学模拟全流程

## 适用场景

- 我需要为多相催化体系自动构建数千步基元反应的网络
- 我想用机器学习势快速评估反应网络中的能量
- 我要做微动力学模拟并分析速率控制步骤

## 场景标签

 · 领域:计算化学/材料科学

## 证据(README 行号)

> L14: CARE (*Catalytic Automated Reaction Evaluator*) is a framework for the automated generation and manipulation of che
> L98: Once the CRN is energetically evaluated, microkinetic simulations enable you to quantify the performance of the cat

## 星数曲线

```mermaid
xychart-beta
    title "LopezGroup-ICIQ/care 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 92 --> 95
    line [93, 94, 94]
```

2026-10-18 93 → 2026-10-28 94（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1f8e33622bb2` · [字段定义](../../DATASET.md)*
